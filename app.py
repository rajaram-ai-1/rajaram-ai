import streamlit as st
from groq import Groq
import google.generativeai as genai
from PIL import Image

# --- 1. चाबियाँ (Secrets) ---
try:
    GROQ_K = st.secrets["GROQ_API_KEY"]
    GEMINI_K = st.secrets["GOOGLE_API_KEY"]
    client_groq = Groq(api_key=GROQ_K)
    
    # गूगल को स्टेबल वर्जन पर सेट करना
    genai.configure(api_key=GEMINI_K)
except Exception as e:
    st.error(f"भाई, चाबियाँ चेक करो: {e}")
    st.stop()

# --- 2. देखने और सोचने की शक्ति ---
def get_ai_response(text, file):
    if file:
        try:
            # यहाँ 'gemini-1.5-flash-latest' का इस्तेमाल करें, ये कभी फेल नहीं होता
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            img = Image.open(file)
            # स्टेबल जनरेशन
            res = model.generate_content([text if text else "इसे समझाओ भाई", img])
            return res.text, "Gemini Vision 📷"
        except Exception as e:
            # अगर फिर भी एरर आए, तो ग्रॉक को बैकअप में रखें
            return f"गूगल भाई अभी भी नखरे कर रहे हैं, पर हम हार नहीं मानेंगे! एरर: {str(e)}", "Error"
    else:
        try:
            res = client_groq.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "You are Rajaram AI. A loyal brother. Use Hindi."},
                          {"role": "user", "content": text}]
            )
            return res.choices[0].message.content, "Llama 3.3 ⚡"
        except: return "भाई, ग्रॉक अभी बिजी है।", "None"

# --- 3. इंटरफ़ेस (Tools बटन चैट बॉक्स के पास) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")

st.markdown("""
    <style>
    .stApp { background-color: #131314; color: white; }
    .chat-bubble { padding: 15px; border-radius: 15px; border: 1px solid #3c3f43; margin-bottom: 15px; }
    .stChatInput { border-radius: 20px !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 Rajaram AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

# मैसेज दिखाना
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# --- 4. टूल्स बार ---
col1, col2 = st.columns([1, 5])
with col1:
    # कैमरा आइकॉन वाला छोटा अपलोडर
    up_file = st.file_uploader("📷", type=['png', 'jpg', 'jpeg'], key="camera", label_visibility="collapsed")

with col2:
    prompt = st.chat_input("अब पूछो भाई, अब नहीं रुकेगा...")

if prompt or up_file:
    user_txt = prompt if prompt else "फोटो देखो भाई"
    
    # डुप्लीकेट मैसेज रोकने के लिए
    if not st.session_state.messages or st.session_state.messages[-1]["content"] != user_txt:
        st.session_state.messages.append({"role": "user", "content": user_txt})
        with st.chat_message("user"):
            st.write(user_txt)
            if up_file: st.image(up_file, width=200)

        with st.spinner("राजाराम AI की शक्ति काम कर रही है..."):
            ans, brain = get_ai_response(user_txt, up_file)
            st.session_state.messages.append({"role": "assistant", "content": ans})
            with st.chat_message("assistant"):
                st.write(ans)
                st.caption(f"Active Power: {brain}")
