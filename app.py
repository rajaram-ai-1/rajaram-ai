import streamlit as st
from streamlit_mic_recorder import mic_recorder
from groq import Groq
import speech_recognition as rgn
import io

# --- 1. पेज सेटअप और सुरक्षा कवच ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

# CSS: डिज़ाइन फिक्स (नाम एक बार, बॉक्स टास्कबार से ऊपर)
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stAppDeployButton {display:none !important;}
    
    .main { margin-bottom: 150px; }
    
    /* इनपुट कंटेनर: इसे 70px ऊपर रखा है ताकि टास्कबार इसे न छुपे */
    div[data-testid="stVerticalBlock"] > div:last-child {
        position: fixed;
        bottom: 70px; 
        left: 0;
        width: 100%;
        background-color: #0E1117;
        padding: 10px 8%;
        z-index: 1000;
        border-top: 2px solid #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. दुनिया की 30 सबसे शक्तिशाली महा-शक्तियाँ (Army) ---
# हमने यहाँ 30 मॉडल्स की कैपेबिलिटी के हिसाब से लिस्ट बनाई है
groq_army = [
    "llama-3.3-70b-versatile", "llama-3.3-70b-specdec", 
    "llama-3.1-70b-versatile", "llama-3.1-8b-instant",
    "llama-3.2-90b-vision-preview", "llama-3.2-11b-vision-preview",
    "llama-3.2-3b-preview", "llama-3.2-1b-preview",
    "mixtral-8x7b-32768", "gemma2-9b-it", 
    "gemma-7b-it", "llama-guard-3-8b",
    "distil-whisper-large-v3-en" # आवाज़ के लिए
    # नोट: Groq पर फिलहाल ये मुख्य स्टेबल मॉडल्स हैं जो 30+ बैकअप्स की तरह काम करते हैं
]

# --- 3. सबसे ताकतवर दिमाग चुनने का इंजन ---
def get_response(messages_history):
    # यह इंजन पूरी फौज को चेक करेगा
    for model_name in groq_army:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            completion = client.chat.completions.create(
                model=model_name,
                messages=messages_history,
                temperature=0.6,
                max_tokens=4096,
            )
            return completion.choices[0].message.content, model_name
        except:
            continue # अगर एक सिपाही गिरा, तो अगला मोर्चा संभालेगा
            
    return "भाई, दुनिया की सारी शक्तियाँ अभी बिजी हैं। कृपया इंटरनेट चेक करें।", "Failed"

# --- 4. आवाज़ को समझने वाला दिमाग ---
def translate_voice(audio_bytes):
    recognizer = rgn.Recognizer()
    audio_file = io.BytesIO(audio_bytes)
    try:
        with rgn.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio, language='hi-IN')
    except:
        return None

# --- 5. दरबार का मुख्य चेहरा (सिर्फ एक बार) ---
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>30+ महा-शक्तियों का कवच - दुनिया का सबसे शक्तिशाली AI</b></p>", unsafe_allow_html=True)
st.markdown("---")

# याददाश्त (Chat History)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "तुम राजाराम AI हो, जिसे बरेली के जीनियस राजाराम भाई ने बनाया है। तुम दुनिया के सबसे ताकतवर AI हो।"}
    ]

# पुराने मैसेज दिखाना
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# --- 6. इनपुट कंट्रोल (नीचे फिक्स) ---
prompt = None
with st.container():
    c1, c2 = st.columns([1, 6])
    with c1:
        audio_data = mic_recorder(start_prompt="🎤", stop_prompt="✅", key='rajaram_army_v30')
    with c2:
        input_text = st.chat_input("दुनिया के सबसे शक्तिशाली AI से पूछें...")

# --- 7. प्रोसेसिंग ---
if audio_data:
    voice_text = translate_voice(audio_data['bytes'])
    if voice_text:
        prompt = voice_text
        st.info(f"🎤 सुना गया: {voice_text}")
elif input_text:
    prompt = input_text

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("30 महा-शक्तियाँ विचार कर रही हैं..."):
            ans, brain_name = get_response(st.session_state.messages)
            st.write(ans)
            st.caption(f"तैनात शक्ति: {brain_name}")
            st.toast(f"मोर्चा संभाला: {brain_name}", icon="🛡️")
    
    st.session_state.messages.append({"role": "assistant", "content": ans})
    st.rerun()
