import streamlit as st
from groq import Groq
import google.generativeai as genai
from PIL import Image

# --- 1. चाबियाँ (Secrets से) ---
try:
    client_groq = Groq(api_key=st.secrets["GROQ_API_KEY"])
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("भाई, Secrets में चाबियाँ चेक करो!")
    st.stop()

# --- 2. दिमाग का लॉजिक ---
def get_ai_response(text, file):
    if file:
        # अगर फोटो है तो जेमिनी जागेगा
        model = genai.GenerativeModel('gemini-1.5-flash')
        img = Image.open(file)
        res = model.generate_content([text if text else "इसे समझाओ भाई", img])
        return res.text, "Gemini Vision 📷"
    else:
        # सिर्फ टेक्स्ट है तो ग्रॉक की फौज
        try:
            res = client_groq.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "You are Rajaram AI. A loyal brother. Answer in Hindi. Call user 'Bhai'."},
                          {"role": "user", "content": text}]
            )
            return res.choices[0].message.content, "Llama 3.3 ⚡"
        except:
            return "भाई, ग्रॉक अभी बिजी है, जेमिनी से पूछ रहा हूँ...", "Switching..."

# --- 3. इंटरफ़ेस (जैसा आपने फोटो में मांगा) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")

# सादा और डार्क लुक
st.markdown("""
    <style>
    .stApp { background-color: #131314; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2b2d31; color: white; border: 1px solid #3c3f43; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 Rajaram AI")

# चैट की याददाश्त
if "messages" not in st.session_state:
    st.session_state.messages = []

# बटन वाली पट्टी (Tools, Fast, Voice)
col1, col2, col3 = st.columns(3)
with col1:
    up_file = st.file_uploader("➕ Tools (Photo)", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")
with col2:
    st.button("⚡ Fast (Active)")
with col3:
    st.button("🎤 Voice (Soon)")

# पुरानी चैट दिखाना
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# इनपुट बॉक्स
prompt = st.chat_input("Ask Rajaram AI...")

if prompt or up_file:
    user_txt = prompt if prompt else "फोटो देखो भाई"
    st.session_state.messages.append({"role": "user", "content": user_txt})
    with st.chat_message("user"):
        st.write(user_txt)
        if up_file: st.image(up_file, width=200)

    with st.spinner("सोच रहा हूँ भाई..."):
        ans, brain = get_ai_response(user_txt, up_file)
        st.session_state.messages.append({"role": "assistant", "content": ans})
        with st.chat_message("assistant"):
            st.write(ans)
            st.caption(f"शक्ति: {brain}")
