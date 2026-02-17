import streamlit as st
from groq import Groq
import random
from gtts import gTTS
import base64
import os

# --- 1. शाही सेटअप ---
st.set_page_config(page_title="Rajaram AI 30-Brains", layout="centered")
st.markdown("<style>.main { background-color: #0b141a; color: white; }</style>", unsafe_allow_html=True)

# --- 2. 30 महा-शक्तिशाली दिमागों की फौज ---
MODELS_ARMY = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "llama-3.2-11b-vision-preview", # टॉप 3 मुख्य दिमाग
    "llama-3.1-8b-instant", "llama-3.2-3b-preview", "llama-3.2-1b-preview",
    "mixtral-8x7b-32768", "gemma2-9b-it", "llama3-70b-8192", "llama3-8b-8192",
    "distil-grenache-8b-llama-3.1", "qwen-2.5-72b", "deepseek-v3", "phi-3-medium",
    "qwen-2.5-coder-32b", "codellama-70b", "meta-llama-guard-3-8b", "hermes-3-llama-3.1-8b",
    "wizardlm-2-8x22b", "mixtral-8x22b-v0.1", "stable-beluga-70b", "falcon-180b",
    "mistral-large-2", "claude-3-haiku-open", "nous-hermes-2-mixtral", "openchat-3.5-0106",
    "llama-3.3-70b-specdec", "gemma-7b-it", "soliloquy-l3-8b", "stable-lm-3b"
]

# --- 3. बोलने की शक्ति ---
def shakti_speak(text):
    try:
        tts = gTTS(text=text, lang='hi')
        tts.save("reply.mp3")
        with open("reply.mp3", "rb") as f:
            data = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio src="data:audio/mp3;base64,{data}" autoplay="true"></audio>', unsafe_allow_html=True)
    except: pass

# --- 4. मुख्य इंजन (Failover System के साथ) ---
def main():
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 राजाराम AI (30 दिमागों की शक्ति)</h1>", unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    prompt = st.chat_input("अपना आदेश दें, राजाराम भाई...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)

        # --- दिमाग चुनने और फेल होने पर बदलने का लॉजिक ---
        success = False
        attempts = 0
        temp_army = MODELS_ARMY.copy()
        random.shuffle(temp_army) # दिमागों को मिला दिया

        while not success and attempts < 5: # 5 बार तक दूसरा दिमाग ट्राई करेगा
            selected_brain = temp_army[attempts]
            try:
                client = Groq(api_key=st.secrets["GROQ_API_KEY"])
                completion = client.chat.completions.create(
                    model=selected_brain,
                    messages=[{"role": "system", "content": "तुम राजाराम भाई की AI हो। हिंदी में छोटा जवाब दो।"}] + 
                             [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                )
                ans = completion.choices[0].message.content
                
                with st.chat_message("assistant"):
                    st.markdown(ans)
                    st.caption(f"सक्रिय दिमाग: {selected_brain}")
                    shakti_speak(ans)
                
                st.session_state.messages.append({"role": "assistant", "content": ans})
                success = True
            except Exception as e:
                attempts += 1
                # अगर दिमाग खराब हुआ, तो यहाँ चुपचाप दूसरा चुना जाएगा
                continue 

        if not success:
            st.error("भाई, आज सभी 30 दिमाग व्यस्त हैं। कृपया थोड़ी देर बाद पूछें।")

if __name__ == "__main__":
    main()
                                                       
