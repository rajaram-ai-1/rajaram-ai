import streamlit as st
from groq import Groq

# --- 1. सुरक्षा कवच ---
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_API_KEY)
except:
    st.error("Secrets में चाबी डालें भाई!")
    st.stop()

# --- 2. Gemini 3 जैसा लुक (CSS) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

st.markdown("""
    <style>
    /* पूरे ऐप का बैकग्राउंड डार्क */
    .stApp { background-color: #131314; color: #e3e3e3; }
    
    /* चैट मैसेज का स्टाइल */
    .chat-container { margin-bottom: 100px; }
    .user-msg { background-color: #2b2d31; padding: 15px; border-radius: 15px; margin: 10px 0; border: 1px solid #3c3f43; }
    .ai-msg { background-color: transparent; padding: 15px; margin: 10px 0; }

    /* नीचे वाला जादुई चैटबॉक्स (जैसा आपने फोटो में दिखाया) */
    .fixed-bottom {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        background-color: #1e1f20;
        border-radius: 30px;
        padding: 10px 20px;
        display: flex;
        align-items: center;
        border: 1px solid #3c3f43;
        z-index: 1000;
    }
    
    /* इनपुट बॉक्स को साफ़ करना */
    .stChatInputContainer {
        padding-bottom: 30px !important;
        background-color: transparent !important;
    }
    .stChatInput div {
        background-color: #1e1f20 !important;
        border: 1px solid #3c3f43 !important;
        border-radius: 25px !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. चैट इंटरफ़ेस ---
st.markdown("<h2 style='text-align: center; color: #8e9196;'>Rajaram AI</h2>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# मैसेज दिखाना
for msg in st.session_state.messages:
    role_class = "user-msg" if msg["role"] == "user" else "ai-msg"
    with st.container():
        st.markdown(f"<div class='{role_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# --- 4. इनपुट बार (Tools + Input + Fast + Mic) ---
# Streamlit का डिफ़ॉल्ट इनपुट बॉक्स आपकी फोटो जैसा ही काम करेगा
prompt = st.chat_input("Ask Rajaram AI...")

if prompt:
    # यूजर का मैसेज
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun() # स्क्रीन रिफ्रेश करने के लिए

# फोटो वाले आइकॉन दिखाने के लिए संकेत
st.markdown("""
    <div style='display: flex; justify-content: space-around; color: #8e9196; font-size: 14px; margin-top: 10px;'>
        <span>➕ Tools</span>
        <span>Fast ⚡</span>
        <span>🎤 Voice</span>
    </div>
    """, unsafe_allow_html=True)
