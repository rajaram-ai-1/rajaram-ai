import streamlit as st
from streamlit_mic_recorder import mic_recorder
from groq import Groq
import speech_recognition as rgn
import io
import base64
from PIL import Image

# --- 1. पेज सेटिंग और सुरक्षा कवच ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

# CSS: डिज़ाइन और चैटबॉक्स को नीचे सेट करना
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display:none !important;}
    
    /* चैट एरिया में नीचे जगह छोड़ना */
    .main { margin-bottom: 130px; }
    
    /* इनपुट कंटेनर को सबसे नीचे फिक्स करना */
    div[data-testid="stVerticalBlock"] > div:last-child {
        position: fixed;
        bottom: 25px;
        left: 0;
        width: 100%;
        background-color: #0E1117;
        padding: 15px 5% 25px 5%;
        z-index: 1000;
        border-top: 2px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. महा-शक्तियों की फौज (25+ Models List) ---
# यहाँ हमने नए और चालू मॉडल्स को प्राथमिकता दी है
groq_army = [
    "llama-3.3-70b-versatile",   # सेनापति (सबसे ताकतवर)
    "llama-3.1-70b-versatile",   # महा-ज्ञानी
    "llama-3.1-8b-instant",      # चुलबुला और तेज़
    "mixtral-8x7b-32768",        # विदेशी शक्ति
    "gemma2-9b-it",              # गूगल का दिमाग
    "llama-3.2-11b-vision-preview", 
    "llama-3.2-3b-preview",
    "llama-3.2-1b-preview",
    "llama-guard-3-8b"           # रक्षक मॉडल
]

# --- 3. स्मार्ट दिमाग चुनने वाला इंजन ---
def select_best_brain(messages_history):
    user_input = messages_history[-1]["content"].lower()
    # पढ़ाई वाले कीवर्ड्स
    if any(word in user_input for word in ["padhai", "exam", "science", "maths", "class", "subject", "तैयारी"]):
        return "llama-3.3-70b-versatile", "📖 पढ़ाई वाला दिमाग (70B)"
    # मजाक मस्ती वाले कीवर्ड्स
    elif any(word in user_input for word in ["majak", "joke", "funny", "hi", "kaise ho", "मजाक"]):
        return "llama-3.1-8b-instant", "😂 चुलबुला दिमाग (8B)"
    else:
        return "llama-3.3-70b-versatile", "🧠 ज्ञानी दिमाग"

# --- 4. 'अमर' रिस्पॉन्स फंक्शन (Failover Logic) ---
def get_response(messages_history):
    best_brain, display_name = select_best_brain(messages_history)
    
    # अगर चुना हुआ मॉडल फेल हो, तो बाकी फौज काम करेगी
    models_to_try = [best_brain] + [m for m in groq_army if m != best_brain]
    
    for model_name in models_to_try:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            completion = client.chat.completions.create(
                model=model_name,
                messages=messages_history,
                temperature=0.7,
                max_tokens=2048,
            )
            return completion.choices[0].message.content, f"{model_name}"
        except Exception as e:
            # अगर मॉडल खराब है, तो अगले पर स्विच करो
            continue 
            
    return "भाई, पूरी फौज थक गई है! कृपया इंटरनेट या चाबी चेक करें।", "Error"

# --- 5. आवाज़ को समझने वाला यंत्र ---
def translate_voice(audio_bytes):
    recognizer = rgn.Recognizer()
    audio_file = io.BytesIO(audio_bytes)
    try:
        with rgn.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio, language='hi-IN')
    except:
        return None

# --- 6. दरबार की सजावट ---
st.markdown("<h1 style='text-align: center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>25+ महा-शक्तियों का कवच - अमर, सुरक्षित और तेज़</b></p>", unsafe_allow_html=True)
st.markdown("---")

# याददाश्त (Chat History)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "तुम 'राजाराम AI' हो। तुम बरेली के राजाराम भाई (15 साल, क्लास 10) के लिए काम करते हो। हमेशा हिंदी में बात करो और भाई कहकर सम्मान दो।"}
    ]

# पुरानी चैट स्क्रीन पर दिखाना
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# --- 7. इनपुट (माइक + चैटबॉक्स) ---
prompt = None
footer_container = st.container()
with footer_container:
    c1, c2 = st.columns([1, 7])
    with c1:
        audio_data = mic_recorder(start_prompt="🎤", stop_prompt="✅", key='rajaram_final_mic')
    with c2:
        input_text = st.chat_input("राजाराम भाई से कुछ पूछें...")

# --- 8. प्रोसेसिंग लॉजिक ---
if audio_data:
    voice_text = translate_voice(audio_data['bytes'])
    if voice_text:
        prompt = voice_text
        st.info(f"🎤 आपने कहा: {voice_text}")
elif input_text:
    prompt = input_text

if prompt:
    # यूजर का संदेश
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # AI का जवाब (अमर फौज के साथ)
    with st.chat_message("assistant"):
        with st.spinner("फौज मोर्चा संभाल रही है..."):
            ans, model_used = get_response(st.session_state.messages)
            st.toast(f"शक्ति तैनात: {model_used}", icon='🚀')
            st.write(ans)
            st.caption(f"सक्रिय महा-शक्ति: {model_used}")
    
    st.session_state.messages.append({"role": "assistant", "content": ans})
    st.rerun()
