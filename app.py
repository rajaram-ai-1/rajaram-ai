import streamlit as st
from streamlit_mic_recorder import mic_recorder
from groq import Groq
import speech_recognition as rgn
import io
import base64
from PIL import Image

# --- 1. पेज सेटअप और टाइटल ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")
st.title("👑 Rajaram AI")
st.markdown("##### 25+ महा-शक्तियों का कवच - अमर, सुरक्षित और तेज़")

# --- 2. CSS: चैटबॉक्स को नीचे (Bottom) चिपकाने के लिए ---
st.markdown("""
    <style>
    .main { margin-bottom: 100px; }
    div[data-testid="stVerticalBlock"] > div:last-child {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #0E1117;
        padding: 10px 5% 20px 5%;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. दिमाग (Meta Llama / Groq) का फंक्शन ---
def get_response(messages):
    try:
        # पक्का करें कि आपने Streamlit Secrets में अपनी Key डाली है
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"माफ़ करना भाई, एरर आया है: {str(e)}"

# --- 4. आवाज़ को टेक्स्ट में बदलने वाला फंक्शन ---
def translate_voice(audio_bytes):
    recognizer = rgn.Recognizer()
    audio_file = io.BytesIO(audio_bytes)
    try:
        with rgn.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio, language='hi-IN')
    except:
        return None

# --- 5. चैट हिस्ट्री (याददाश्त) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# पुराने मैसेज दिखाना
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 6. इनपुट एरिया (माइक + बॉक्स) ---
# यह हिस्सा स्क्रीन के नीचे रहेगा
container = st.container()
with container:
    cols = st.columns([1, 6])
    with cols[0]:
        # माइक बटन
        audio_data = mic_recorder(start_prompt="🎤", stop_prompt="✅", key='rajaram_mic')
    with cols[1]:
        # टाइपिंग बॉक्स
        prompt = st.chat_input("rajaram ai se puche...")

# --- 7. असली काम (Logic) ---

# अगर आवाज़ रिकॉर्ड हुई है
if audio_data:
    voice_text = translate_voice(audio_data['bytes'])
    if voice_text:
        prompt = voice_text
        st.info(f"🎤 आपने कहा: {voice_text}")

# अगर कोई मैसेज (टाइप किया हुआ या बोला हुआ) मिला है
if prompt:
    # यूजर का मैसेज दिखाओ और सेव करो
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI का जवाब लाओ
    with st.chat_message("assistant"):
        with st.spinner("राजाराम AI सोच रहा है..."):
            full_response = get_response(st.session_state.messages)
            st.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.rerun()
    
# 1. पेज सेटिंग (सबसे ऊपर)
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

# --- राजाराम भाई का 'दिमाग' चुनने वाला इंजन (नया जोड़ा गया) ---
def select_best_brain(messages_history):
    user_input = messages_history[-1]["content"].lower()
    if any(word in user_input for word in ["padhai", "maths", "science", "exam", "book", "class", "study"]):
        return "llama-3.3-70b-versatile", "📖 पढ़ाई वाला दिमाग (Llama 70B)"
    elif any(word in user_input for word in ["majak", "joke", "funny", "hi", "hello", "kaise ho"]):
        return "llama-3.1-8b-instant", "😂 चुलबुला दिमाग (Llama 8B)"
    else:
        return "llama-3.3-70b-versatile", "🧠 ज्ञानी दिमाग (Mixtral)"

# 2. सुरक्षा कवच (स्टाइलिंग)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display:none !important;}
    div[data-testid="stStatusWidget"] {display:none !important;}
    button[title="Manage app"] {display: none !important;}
    .viewerBadge_container__1QS13 {display: none !important;}
    </style>
    """, unsafe_allow_html=True)

# 3. तिजोरी से चाबी निकालना
try:
    if "GROQ_API_KEY" in st.secrets:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    else:
        st.error("❌ भाई, Secrets में 'GROQ_API_KEY' नहीं मिली!")
        st.stop()
except Exception as e:
    st.error(f"❌ कनेक्शन एरर: {e}")
    st.stop()

# 4. 25+ शक्तिशाली दिमागों की महा-फौज (आपकी लिस्ट सुरक्षित है)
groq_army = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", 
    "llama-3.2-90b-vision-preview", "llama-3.2-11b-vision-preview",
    "llama-3.2-3b-preview", "llama-3.2-1b-preview",
    "llama-3.1-8b-instant", "llama3-70b-8192", 
    "llama3-8b-8192", "mixtral-8x7b-32768", 
    "gemma2-9b-it", "gemma-7b-it",
    "llama-guard-3-8b", "distil-whisper-large-v3-en"
]

# 5. रिस्पॉन्स फंक्शन (इसे मैंने आपके पुराने कोड में फिट कर दिया है)
def get_response(messages_history):
    # स्मार्ट तरीके से दिमाग चुनना
    best_brain, brain_display_name = select_best_brain(messages_history)
    
    try:
        completion = client.chat.completions.create(
            model=best_brain,
            messages=messages_history,
            temperature=0.7,
            max_tokens=2048,
        )
        return completion.choices[0].message.content, brain_display_name
    except Exception as e:
        return f"माफ़ करना भाई, गड़बड़ हो गई: {e}", "Error"
def get_meta_vision_response(user_prompt, image_file): 
         (
    )
# 6. दरबार की सजावट
st.markdown("<h1 style='text-align: center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>25+ महा-शक्तियों का कवच - अमर ,सुरक्षित और तेज़</b></p>", unsafe_allow_html=True)

# 7. याददाश्त
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "तुम 'राजाराम AI' हो। और यह आपके लिए बरेली के राजाराम भाई ने बनाया है जो 15 साल के क्लास 10 के स्टूडेंट हैं, वे बहुत इंटेलिजेंट हैं।आपको पढ़ाई को गंभीरता से लेना चाहिए। अगर कोई कहे कि मुझे इस क्लास के इस सब्जेक्ट की तैयारी कराओ, तो उसे टीचर की तरह समझाओ। हमेशा हिंदी में बात करो और 'भाई' कहकर सम्मान दो।"}
    ]

# पुरानी चैट दिखाना
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
# --- यहाँ से नया कोड शुरू (इसे 'for' लूप के ठीक नीचे पेस्ट करें) ---

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.spinner("फौज मोर्चा संभाल रही है..."):
        # यहाँ आपका 'answer' और 'used_id' सही से सेट हो गया है
        answer, used_id = get_response(st.session_state.messages)
        st.toast(f"अभी {used_id} एक्टिव है!", icon='🔥')
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)
            st.caption(f"सक्रिय शक्ति: {used_id}")
        
        st.rerun()
