import streamlit as st
from groq import Groq
import google.generativeai as genai
from PIL import Image

# --- 1. चाबियाँ (Secrets) ---
try:
    GROQ_K = st.secrets["GROQ_API_KEY"]
    GEMINI_K = st.secrets["GOOGLE_API_KEY"]
    client_groq = Groq(api_key=GROQ_K)
    genai.configure(api_key=GEMINI_K)
except:
    st.error("भाई, Secrets में चाबियाँ चेक करो!")
    st.stop()

# --- 2. दिमाग (404 एरर फिक्स के साथ) ---
def get_ai_response(text, file):
    if file:
        try:
            # यहाँ 'gemini-1.5-flash' का सीधा उपयोग बिना किसी वर्जन के
            model = genai.GenerativeModel('gemini-1.5-flash')
            img = Image.open(file)
            res = model.generate_content([text if text else "इसे समझाओ भाई", img])
            return res.text, "Gemini Vision 📷"
        except Exception as e:
            return f"गूगल ने मना कर दिया: {str(e)}", "Error"
    else:
        try:
            res = client_groq.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "You are Rajaram AI. Loyal brother. Use Hindi."},
                          {"role": "user", "content": text}]
            )
            return res.choices[0].message.content, "Llama 3.3 ⚡"
        except: return "भाई, ग्रॉक बिजी है।", "None"

# --- 3. इंटरफ़ेस (Gemini 3 Style - No Loop) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")

st.markdown("""
    <style>
    .stApp { background-color: #131314; color: white; }
    .chat-container { padding-bottom: 120px; }
    /* चैट बॉक्स को नीचे फिक्स करना */
    .stChatInputContainer { background-color: #131314 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 Rajaram AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

# मैसेज दिखाना
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# --- 4. टूल्स बटन अब चैट बॉक्स के ठीक ऊपर ---
col1, col2 = st.columns([1, 4])
with col1:
    up_file = st.file_uploader("📷", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")
with col2:
    prompt = st.chat_input("Ask Rajaram AI...")

# जब यूजर कुछ भेजे
if prompt or up_file:
    # अगर ये पिछले मैसेज जैसा ही है, तो दोबारा न चलाएं (Loop Protection)
    user_txt = prompt if prompt else "फोटो देखो भाई"
    
    if not st.session_state.messages or st.session_state.messages[-1]["content"] != user_txt:
        st.session_state.messages.append({"role": "user", "content": user_txt})
        with st.chat_message("user"):
            st.write(user_txt)
            if up_file: st.image(up_file, width=150)

        with st.spinner("सोच रहा हूँ भाई..."):
            ans, brain = get_ai_response(user_txt, up_file)
            st.session_state.messages.append({"role": "assistant", "content": ans})
            with st.chat_message("assistant"):
                st.write(ans)
                st.caption(f"Power: {brain}")
                st.write("➕ ❤️ 📷 🎥 🎤")
