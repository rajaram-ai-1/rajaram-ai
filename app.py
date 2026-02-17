import streamlit as st
from groq import Groq
import random
from streamlit_mic_recorder import mic_recorder
from gtts import gTTS
import base64
def shakti_listen():
    audio = mic_recorder(start_prompt="🎤 बोलना शुरू करें", stop_prompt="🛑 रुकें", key='recorder')
    if audio:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        transcription = client.audio.transcriptions.create(
            file=("user_voice.wav", audio['bytes']),
            model="whisper-large-v3",
            language="hi"
        )
        return transcription.text
    return None

def shakti_speak(text):
    tts = gTTS(text=text, lang='hi')
    tts.save("reply.mp3")
    with open("reply.mp3", "rb") as f:
        data = base64.b64encode(f.read()).decode()
        st.markdown(f'<audio src="data:audio/mp3;base64,{data}" autoplay="true"></audio>', unsafe_allow_html=True)
# --- 1. शाही कवच और डिज़ाइन (CSS) ---
st.set_page_config(page_title="Rajaram AI 👑", layout="centered")

st.markdown("""
    <style>
    header, footer, #MainMenu {visibility: hidden !important;}
    .stAppDeployButton {display:none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    .main { background-color: #0b141a; color: white; }
    
    .user-bubble {
        background-color: #005c4b; color: white; padding: 15px;
        border-radius: 15px 15px 2px 15px; margin-bottom: 15px;
        border-right: 5px solid gold;
    }
    .ai-bubble {
        background-color: #202c33; color: white; padding: 15px;
        border-radius: 15px 15px 15px 2px; margin-bottom: 15px;
        border-left: 5px solid gold;
    }
    div[data-testid="stBottom"] { background-color: #111b21 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 30 दिमागों की फौज (Updated & Active Models) ---
# इसमें मैंने सिर्फ वो मॉडल्स रखे हैं जो अभी चल रहे हैं
MODELS_ARMY = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "llama-3.1-8b-instant",
    "gemma2-9b-it", "llama-3.2-11b-vision-preview", "llama3-70b-8192", 
    "llama3-8b-8192", "distil-whisper-large-v3-en", "gemma-7b-it"
]

# --- 3. महा-निर्देश (46 शक्तियाँ) ---
MAHA_PROMPT = "तुम राजाराम AI हो। स्वामी राजाराम भाई बरेली वाले। तुम्हारी 46 शक्तियाँ सक्रिय हैं। हमेशा हिंदी में भाई कहकर बात करो।"

# --- 4. मुख्य इंजन: ऑटो-स्विच और फेल-सेफ के साथ ---
def get_ai_response(messages):
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    
    # दिमागों की लिस्ट को रैंडम करना ताकि लोड बँटा रहे
    shuffled_brains = MODELS_ARMY.copy()
    random.shuffle(shuffled_brains)
    
    # हर दिमाग को आज़माने की कोशिश करना
    for brain in shuffled_brains:
        try:
            completion = client.chat.completions.create(
                model=brain,
                messages=[{"role": "system", "content": MAHA_PROMPT}] + messages,
                temperature=0.8
            )
            return completion.choices[0].message.content, brain
        except Exception as e:
            # अगर ये दिमाग खराब है, तो अगले दिमाग पर जाओ
            continue
            
    return "राजाराम भाई, सभी 30 दिमागों पर बाहरी हमला हुआ है। कृपया कुछ देर बाद कोशिश करें।", "Error"

# --- 5. दरबार (Interface) ---
def main():
   def main():
    st.title("👑 राजाराम AI LIVE")
    
    # यहाँ माइक बटन आएगा
    user_voice_input = shakti_listen()
    
    # अगर आपने कुछ बोला है, तो उसे चैट इनपुट मान लिया जाएगा
    if user_voice_input:
        prompt = user_voice_input
        # इसके आगे का आपका पुराना कोड (Groq वाला) अपने आप चलेगा...
       
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 राजाराम AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>30 दिमाग फेल-सेफ सिस्टम सक्रिय</p>", unsafe_allow_html=True)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # इतिहास दिखाओ
    for chat in st.session_state.chat_history:
        cls = "user-bubble" if chat["role"] == "user" else "ai-bubble"
        label = "राजाराम भाई" if chat["role"] == "user" else f"AI (शक्ति: {chat.get('brain', 'मुख्य')})"
        st.markdown(f"<div class='{cls}'><b>{label}:</b><br>{chat['content']}</div>", unsafe_allow_html=True)

    # आदेश इनपुट
    prompt = st.chat_input("आदेश दें, राजाराम भाई...")

    if prompt:
        # यूजर का मैसेज दिखाओ
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        st.rerun()

    # AI का जवाब (अगर आखिरी मैसेज यूजर का है)
    if st.session_state.chat_history and st.session_state.chat_history[-1]["role"] == "user":
        with st.spinner("30 दिमाग मंथन कर रहे हैं..."):
            # सिर्फ यूजर और असिस्टेंट की बातचीत भेजना (बिना सिस्टम प्रॉम्प्ट के, वो अंदर जुड़ जाएगा)
            clean_messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history]
            
            ans, brain_used = get_ai_response(clean_messages)
            
            st.session_state.chat_history.append({"role": "assistant", "content": ans, "brain": brain_used})
            st.rerun()

if __name__ == "__main__":
    main()
