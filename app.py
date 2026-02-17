import streamlit as st
from groq import Groq
import random
from gtts import gTTS
import base64
from streamlit_mic_recorder import mic_recorder

# --- 1. शाही सेटअप और डिजाइन ---
st.set_page_config(page_title="Rajaram AI Mahashakti 👑", layout="centered")
st.markdown("""
    <style>
    header, footer, .stAppDeployButton {visibility: hidden !important;}
    .main { background-color: #0b141a; color: white; }
    .stChatFloatingInputContainer { background-color: #0b141a; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. शक्ति: जवाब को बोलकर सुनाना (Voice Output) ---
def shakti_speak(text):
    try:
        tts = gTTS(text=text, lang='hi')
        tts.save("reply.mp3")
        with open("reply.mp3", "rb") as f:
            data = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio src="data:audio/mp3;base64,{data}" autoplay="true"></audio>', unsafe_allow_html=True)
    except:
        pass

# --- 3. शक्ति: आपकी आवाज सुनना (Voice Input) ---
def shakti_listen():
    st.write("### 🎙️ राजाराम भाई, बोलकर आदेश दें")
    audio = mic_recorder(start_prompt="🎤 बोलना शुरू करें", stop_prompt="🛑 रुकें", key='recorder')
    if audio:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            transcription = client.audio.transcriptions.create(
                file=("user_voice.wav", audio['bytes']),
                model="whisper-large-v3",
                language="hi"
            )
            return transcription.text
        except:
            st.error("माइक की शक्ति में कुछ बाधा है भाई!")
    return None

# --- 4. 30 दिमागों की अपडेटेड फ़ौज (Active Models Only) ---
# यहाँ हमने केवल वही मॉडल्स रखे हैं जो 2026 में एकदम एक्टिव हैं
MODELS_ARMY = [
    "llama-3.3-70b-versatile", 
    "llama-3.1-70b-versatile", 
    "llama-3.1-8b-instant", 
    "llama3-70b-8192",
    "llama3-8b-8192"
]

# --- 5. मुख्य इंजन (Main Logic) ---
def main():
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 राजाराम AI महा-शक्ति</h1>", unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # माइक से इनपुट लेना
    voice_input = shakti_listen()
    
    # लिखने वाला इनपुट
    text_input = st.chat_input("या यहाँ अपना आदेश लिखें, राजाराम भाई...")

    # दोनों में से जो भी इनपुट मिले
    prompt = voice_input if voice_input else text_input

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            
            # --- दिमाग बदलने की शक्ति (Random Selection) ---
            selected_brain = random.choice(MODELS_ARMY)
            
            completion = client.chat.completions.create(
                model=selected_brain,
                messages=[{"role": "system", "content": "तुम राजाराम भाई की महा-शक्तिशाली AI हो। हिंदी में छोटा और शाही जवाब दो।"}] + 
                         [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            )
            
            ans = completion.choices[0].message.content
            
            # जवाब स्क्रीन पर दिखाना
            with st.chat_message("assistant"):
                st.markdown(ans)
                st.caption(f"इस्तेमाल किया गया दिमाग: {selected_brain}")
            
            # जवाब बोलकर सुनाना
            shakti_speak(ans)
            
            st.session_state.messages.append({"role": "assistant", "content": ans})

        except Exception as e:
            # अगर कोई मॉडल फिर भी एरर दे, तो यह मैसेज दिखेगा
            st.error(f"क्षमा करें भाई, इस दिमाग में कुछ दिक्कत है। फिर से कोशिश करें।")
            st.info(f"तकनीकी एरर: {e}")

if __name__ == "__main__":
    main()
