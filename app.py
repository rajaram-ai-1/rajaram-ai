import streamlit as st
from groq import Groq
import random
from gtts import gTTS
import base64

# --- 1. शाही लुक और डिज़ाइन ---
st.set_page_config(page_title="Rajaram AI 👑", layout="centered")
st.markdown("""
    <style>
    header, footer, .stAppDeployButton {visibility: hidden !important;}
    .main { background-color: #0b141a; color: white; }
    .stChatFloatingInputContainer { background-color: #0b141a; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. बोलने की शक्ति (Voice Power) ---
def shakti_speak(text):
    try:
        # हिंदी आवाज़ बनाना
        tts = gTTS(text=text, lang='hi')
        tts.save("reply.mp3")
        with open("reply.mp3", "rb") as f:
            data = base64.b64encode(f.read()).decode()
            # ऑटो-प्ले ऑडियो कोड
            st.markdown(f'<audio src="data:audio/mp3;base64,{data}" autoplay="true"></audio>', unsafe_allow_html=True)
    except Exception as e:
        st.error("बोलने में दिक्कत आई भाई!")

# --- 3. 30 दिमागों की फौज (30 Brains List) ---
# यहाँ अलग-अलग शक्तिशाली मॉडल्स के नाम हैं जो रोटेशन में चलेंगे
MODELS_ARMY = [
    "llama-3.3-70b-versatile", 
    "llama-3.1-70b-versatile", 
    "gemma2-9b-it", 
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]

# --- 4. मुख्य इंजन ---
def main():
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 राजाराम AI LIVE</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>30 दिमागों की शक्ति के साथ...</p>", unsafe_allow_html=True)

    # चैट हिस्ट्री को याद रखना
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # पुरानी चैट दिखाना
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # आदेश इनपुट (लिखने वाला)
    prompt = st.chat_input("अपना आदेश लिखें, राजाराम भाई...")

    if prompt:
        # 1. यूजर का मैसेज दिखाओ
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 2. AI का दिमाग चुनना और जवाब लाना
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            
            # 30 दिमागों
