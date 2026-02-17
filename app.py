import streamlit as st
from groq import Groq
import random
from gtts import gTTS
import base64
from streamlit_mic_recorder import mic_recorder

# --- 1. शाही सेटअप (Design) ---
st.set_page_config(page_title="Rajaram AI 👑", layout="centered")
st.markdown("""
    <style>
    header, footer, .stAppDeployButton {visibility: hidden !important;}
    .main { background-color: #0b141a; color: white; }
    .stTextInput>div>div>input { color: gold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. लाइव बोलने की शक्ति (Shakti Speak) ---
def shakti_speak(text):
    try:
        tts = gTTS(text=text, lang='hi')
        tts.save("reply.mp3")
        with open("reply.mp3", "rb") as f:
            data = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio src="data:audio/mp3;base64,{data}" autoplay="true"></audio>', unsafe_allow_html=True)
    except:
        pass

# --- 3. लाइव सुनने की शक्ति (Shakti Listen) ---
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
            st.error("माइक की शक्ति काम नहीं कर रही!")
    return None

# --- 4. 30 दिमागों की फ़ौज (Models Army) ---
# यहाँ हमने दुनिया के सबसे बेहतरीन मॉडल्स रखे हैं जो बदल-बदल कर जवाब देंगे
MODELS_ARMY = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", 
    "llama-3.1-8b-instant", "gemma2-9b-it", 
    "mixtral-8x7b-32768", "llama3-70b-8192"
]

def main():
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 राजाराम AI LIVE</h1>", unsafe_allow_html=True)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # --- लाइव इनपुट (माइक या टाइपिंग) ---
    voice_input = shakti_listen()
    text_input = st.chat_input("यहाँ लिखें, राजाराम भाई...")

    # दिमाग बदलने वाला लॉजिक: अगर आवाज़ मिली तो वो, नहीं तो टाइप किया हुआ
    prompt = voice_input if voice_input else text_input

    if prompt:
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            
            # --- दिमाग बदलने की शक्ति (Random Choice) ---
            selected_brain = random.choice(MODELS_ARMY)
            
            completion = client.chat.completions.create(
                model=selected_brain,
                messages=[{"role": "system", "content": "तुम राजाराम भाई की महा-शक्तिशाली AI हो। हमेशा हिंदी में भाई कहकर छोटा जवाब दो।"}] + 
                         [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history]
            )
            
            ans = completion.choices[0].message.content
            st.session_state.chat_history.append({"role": "assistant", "content": ans})
            
            # जवाब दिखाओ और लाइव बोलकर सुनाओ
            st.write(f"**दिमाग ({selected_brain}):** {ans}")
            shakti_speak(ans)
            
            # स्क्रीन को ताज़ा (Refresh) करें
            st.rerun()

        except Exception as e:
            st.error("कनेक्शन में दिक्कत है भाई! कृपया Secrets चेक करें।")

if __name__ == "__main__":
    main()
