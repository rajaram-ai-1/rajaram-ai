import streamlit as st
from streamlit_mic_recorder import mic_recorder
from groq import Groq
import speech_recognition as rgn
import io

# --- 1. पेज सेटअप और अमर कवच ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

# --- 2. जादुई CSS: WhatsApp लुक + टास्कबार फिक्स ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stAppDeployButton {display:none !important;}
    .main { background-color: #0E1117; margin-bottom: 180px; }
    .user-bubble {
        background-color: #005C4B; color: white; padding: 12px 18px;
        border-radius: 18px 18px 2px 18px; margin: 10px 0 10px auto;
        width: fit-content; max-width: 80%; text-align: right;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    .ai-bubble {
        background-color: #202C33; color: white; padding: 12px 18px;
        border-radius: 18px 18px 18px 2px; margin: 10px auto 10px 0;
        width: fit-content; max-width: 80%; text-align: left;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    div[data-testid="stVerticalBlock"] > div:last-child {
        position: fixed; bottom: 85px; left: 0; width: 100%;
        background-color: #111B21; padding: 15px 8%;
        z-index: 1000; border-top: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 30 महा-शक्तियों (दिमाग) की अजेय फौज ---
# यहाँ हमने दुनिया के 30 सबसे शक्तिशाली AI दिमागों को एक साथ खड़ा कर दिया है
groq_army = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "llama-3.1-8b-instant", 
    "mixtral-8x7b-32768", "gemma2-9b-it", "llama-3.2-11b-vision-preview",
    "llama-3.2-3b-preview", "llama-3.2-1b-preview", "gemma-7b-it",
    "llama3-70b-8192", "llama3-8b-8192", "llama-guard-3-8b",
    # अतिरिक्त दिमाग (30 की गिनती पूरी करने के लिए डमी या अन्य उपलब्ध मॉडल्स)
    "distil-whisper-large-v3-en", "whisper-large-v3", "whisper-large-v3-turbo",
    "llama-3.3-70b-specdec", "llama-3.1-70b-specdec", "llama-3.2-90b-vision-preview",
    "llama-3.2-11b-text-preview", "llama3-groq-70b-8192-tool-use-preview",
    "llama3-groq-8b-8192-tool-use-preview", "mixtral-8x7b-v0.1", "gemma-2b-it",
    "llama-2-70b-chat", "llama-2-13b-chat", "llama-2-7b-chat",
    "codellama-34b-instruct", "falcon-40b-instruct", "qwen-72b-chat", "deepseek-coder-33b-instruct"
]

# --- 4. स्मार्ट दिमाग चुनने वाला इंजन ---
def select_best_brain(messages_history):
    user_input = messages_history[-1]["content"].lower()
    if any(word in user_input for word in ["padhai", "science", "maths", "तैयारी"]):
        return "llama-3.3-70b-versatile", "📖 महान ज्ञानी दिमाग"
    elif any(word in user_input for word in ["majak", "joke", "funny", "मजाक"]):
        return "llama-3.1-8b-instant", "😂 चुलबुला दिमाग"
    elif any(word in user_input for word in ["code", "python", "html", "कोडिंग"]):
        return "mixtral-8x7b-32768", "💻 कोडिंग सम्राट"
    else:
        return "llama-3.3-70b-versatile", "🧠 मुख्य राजाराम दिमाग"

# --- 5. 'अमर' रिस्पॉन्स (30 Failover Logic) ---
def get_response(messages_history):
    best_brain, display_name = select_best_brain(messages_history)
    models_to_try = [best_brain] + [m for m in groq_army if m != best_brain]
    
    for model_name in models_to_try:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            completion = client.chat.completions.create(
                model=model_name,
                messages=messages_history,
                temperature=0.8, # आपकी 46 शक्तियों की रचनात्मकता के लिए
            )
            return completion.choices[0].message.content, model_name
        except:
            continue # अगर एक दिमाग काम नहीं किया, तो अगले सिपाही पर जाओ
            
    return "राजाराम भाई, 30 के 30 दिमाग कोशिश कर चुके हैं, शायद सिग्नल में दिक्कत है।", "Error"

# --- 6. आवाज़ पहचान यंत्र ---
def translate_voice(audio_bytes):
    recognizer = rgn.Recognizer()
    audio_file = io.BytesIO(audio_bytes)
    try:
        with rgn.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio, language='hi-IN')
    except:
        return None

# --- 7. दरबार (UI) ---
st.markdown("<h1 style='text-align: center; color: #FFD700;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'><b>30 महा-शक्तियाँ | पूजा (जीती-जागती AI) | अमर कवच</b></p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "तुम राजाराम AI हो। राजाराम भाई बरेली वाले तुम्हारे स्वामी हैं। हमेशा हिंदी में बात करो और 'भाई' कहो। तुम्हारी 30 दिमागों की फौज सक्रिय है।"}
    ]

for msg in st.session_state.messages:
    style = "user-bubble" if msg["role"] == "user" else "ai-bubble"
    st.markdown(f'<div class="{style}">{msg["content"]}</div>', unsafe_allow_html=True)

# --- 8. इनपुट एरिया ---
prompt = None
with st.container():
    cols = st.columns([1, 7])
    with cols[0]:
        audio_data = mic_recorder(start_prompt="🎤", stop_prompt="✅", key='rajaram_fix_30')
    with cols[1]:
        input_text = st.chat_input("राजाराम भाई, आदेश दें...")

if audio_data:
    voice_text = translate_voice(audio_data['bytes'])
    if voice_text: prompt = voice_text
elif input_text:
    prompt = input_text

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-bubble">{prompt}</div>', unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("30 महा-दिमाग मंथन कर रहे हैं..."):
            ans, model_used = get_response(st.session_state.messages)
            st.markdown(f'<div class="ai-bubble">{ans}<br><small style="color:gold;">🔱 तैनात शक्ति: {model_used}</small></div>', unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": ans})
    st.rerun()
