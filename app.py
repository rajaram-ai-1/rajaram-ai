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

    /* दाईं ओर यूजर का मैसेज */
    .user-bubble {
        background-color: #005C4B; color: white; padding: 12px 18px;
        border-radius: 18px 18px 2px 18px; margin: 10px 0 10px auto;
        width: fit-content; max-width: 80%; text-align: right;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    /* बाईं ओर AI का मैसेज */
    .ai-bubble {
        background-color: #202C33; color: white; padding: 12px 18px;
        border-radius: 18px 18px 18px 2px; margin: 10px auto 10px 0;
        width: fit-content; max-width: 80%; text-align: left;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }

    /* इनपुट एरिया: टास्कबार से ऊपर (50px) */
    div[data-testid="stVerticalBlock"] > div:last-child {
        position: fixed;
        bottom: 85px; left: 0; width: 100%;
        background-color: #111B21; padding: 15px 8%;
        z-index: 1000; border-top: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 30 महा-शक्तियों की विशाल फौज ---
groq_army = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "llama-3.1-8b-instant",
    "mixtral-8x7b-32768", "gemma2-9b-it", "llama-3.2-11b-vision-preview",
    "llama-3.2-3b-preview", "llama-3.2-1b-preview", "gemma-7b-it",
    "llama3-70b-8192", "llama3-8b-8192", "llama-guard-3-8b"
    # (पायथन लूप में यह पूरी फौज की तरह काम करता है)
]

# --- 4. स्मार्ट दिमाग चुनने वाला इंजन (आपका सिस्टम) ---
def select_best_brain(messages_history):
    user_input = messages_history[-1]["content"].lower()
    # पढ़ाई वाले कीवर्ड्स
    if any(word in user_input for word in ["padhai", "exam", "science", "maths", "class", "subject", "तैयारी", "school"]):
        return "llama-3.3-70b-versatile", "📖 पढ़ाई वाला दिमाग (70B)"
    # मजाक मस्ती वाले कीवर्ड्स
    elif any(word in user_input for word in ["majak", "joke", "funny", "hi", "kaise ho", "मजाक", "hello"]):
        return "llama-3.1-8b-instant", "😂 चुलबुला दिमाग (8B)"
    else:
        return "llama-3.3-70b-versatile", "🧠 ज्ञानी दिमाग"

# --- 5. 'अमर' रिस्पॉन्स फंक्शन (Failover Logic) ---
def get_response(messages_history):
    best_brain, display_name = select_best_brain(messages_history)
    
    # फेलओवर लिस्ट बनाना
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
            return completion.choices[0].message.content, model_name
        except:
            continue # अगर एक खराब हुआ तो दूसरे सिपाही पर जाओ
            
    return "भाई, पूरी फौज थक गई है! नेट चेक करें।", "Error"

# --- 6. आवाज़ को समझने वाला यंत्र ---
def translate_voice(audio_bytes):
    recognizer = rgn.Recognizer()
    audio_file = io.BytesIO(audio_bytes)
    try:
        with rgn.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio, language='hi-IN')
    except:
        return None

# --- 7. दरबार की सजावट (UI) ---
st.markdown("<h1 style='text-align: center; color: #00A884;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>30+ महा-शक्तियाँ | स्मार्ट दिमाग इंजन | अमर कवच</b></p>", unsafe_allow_html=True)
st.markdown("---")

# याददाश्त (Chat History)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "तुम राजाराम AI हो, जिसे बरेली के राजाराम भाई ने बनाया है। हमेशा हिंदी में बात करो और भाई कहकर सम्मान दो।"}
    ]

# चैट स्क्रीन पर दिखाना (WhatsApp Style)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
    elif msg["role"] == "assistant":
        st.markdown(f'<div class="ai-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

# --- 8. इनपुट एरिया (माइक + बॉक्स) ---
prompt = None
footer_container = st.container()
with footer_container:
    cols = st.columns([1, 7])
    with cols[0]:
        audio_data = mic_recorder(start_prompt="🎤", stop_prompt="✅", key='rajaram_final_fix')
    with cols[1]:
        input_text = st.chat_input("राजाराम Ai  से पूछें...")

# प्रोसेसिंग लॉजिक
if audio_data:
    voice_text = translate_voice(audio_data['bytes'])
    if voice_text:
        prompt = voice_text
        st.info(f"🎤 सुना गया: {voice_text}")
elif input_text:
    prompt = input_text

if prompt:
    # यूजर मैसेज
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-bubble">{prompt}</div>', unsafe_allow_html=True)

    # AI मैसेज (फौज के साथ)
    with st.chat_message("assistant"):
        with st.spinner("30 महा-शक्तियाँ विचार कर रही हैं..."):
            ans, model_used = get_response(st.session_state.messages)
            st.markdown(f'<div class="ai-bubble">{ans}<br><small style="color:gray;">🛡️ शक्ति तैनात: {model_used}</small></div>', unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": ans})
    
    st.rerun()
