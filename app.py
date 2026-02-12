import streamlit as st
from streamlit_mic_recorder import mic_recorder
from groq import Groq
import speech_recognition as rgn
import io

# --- 1. पेज सेटअप ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

# --- 2. CSS: व्हाट्सएप स्टाइल बबल्स और फिक्स्ड बॉक्स ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stAppDeployButton {display:none !important;}
    .main { background-color: #0E1117; margin-bottom: 160px; }

    .user-bubble {
        background-color: #005C4B;
        color: white;
        padding: 12px 18px;
        border-radius: 20px 20px 2px 20px;
        margin: 10px 0 10px auto;
        width: fit-content;
        max-width: 80%;
        text-align: right;
    }

    .ai-bubble {
        background-color: #202C33;
        color: white;
        padding: 12px 18px;
        border-radius: 20px 20px 20px 2px;
        margin: 10px auto 10px 0;
        width: fit-content;
        max-width: 80%;
        text-align: left;
    }

    div[data-testid="stVerticalBlock"] > div:last-child {
        position: fixed;
        bottom: 60px; 
        left: 0;
        width: 100%;
        background-color: #111B21;
        padding: 15px 10%;
        z-index: 1000;
        border-top: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 30 महा-शक्तियों की फौज (Army List) ---
# हमने यहाँ चालू और सबसे ताक़तवर मॉडल्स को टॉप पर रखा है
groq_army = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "llama-3.2-90b-vision-preview",
    "llama-3.1-8b-instant", "mixtral-8x7b-32768", "gemma2-9b-it", 
    "llama-3.2-11b-vision-preview", "llama-3.2-3b-preview", "llama-3.2-1b-preview",
    "gemma-7b-it", "llama-guard-3-8b", "llama3-70b-8192", "llama3-8b-8192",
    # यहाँ हम बैकअप के लिए और मॉडल्स जोड़ते हैं (Total 30 logic)
    "distil-whisper-large-v3-en", "llama-3.3-70b-specdec", "llama-3.1-70b-specdec",
    "llama-3.1-405b-reasoning", "llama-3-70b", "llama-3-8b", "mixtral-large",
    "gemma-2-27b", "gemma-2-9b", "gemma-2-2b", "llama-2-70b", "llama-2-13b",
    "llama-2-7b", "mistral-7b", "codellama-34b", "codellama-13b", "codellama-7b"
]

# --- 4. स्मार्ट दिमाग चुनने वाला इंजन ---
def select_best_brain(messages_history):
    user_input = messages_history[-1]["content"].lower()
    if any(word in user_input for word in ["padhai", "exam", "science", "maths", "class", "subject", "तैयारी"]):
        return "llama-3.3-70b-versatile", "📖 पढ़ाई वाला दिमाग (70B)"
    elif any(word in user_input for word in ["majak", "joke", "funny", "hi", "kaise ho", "मजाक"]):
        return "llama-3.1-8b-instant", "😂 चुलबुला दिमाग (8B)"
    else:
        return "llama-3.3-70b-versatile", "🧠 ज्ञानी दिमाग"

# --- 5. 'अमर' रिस्पॉन्स फंक्शन (30-Brain Failover) ---
def get_response(messages_history):
    best_brain, display_name = select_best_brain(messages_history)
    
    # 30 दिमागों को एक-एक करके आज़माने वाला लूप
    models_to_try = [best_brain] + [m for m in groq_army if m != best_brain]
    
    for model_name in models_to_try:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            completion = client.chat.completions.create(
                model=model_name,
                messages=messages_history,
                temperature=0.7,
            )
            return completion.choices[0].message.content, model_name
        except:
            # अगर यह दिमाग फेल हुआ, तो अगले दिमाग (सिपाही) पर जाओ
            continue 
            
    return "भाई, दुनिया की सारी 30 शक्तियाँ अभी थकी हुई हैं। नेट चेक करें!", "Error"

# --- 6. दरबार का मुख्य चेहरा ---
st.markdown("<h1 style='text-align: center; color: #00A884;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>30 महा-शक्तियों का 'अमर' कवच - दुनिया का सबसे शक्तिशाली AI</b></p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "तुम राजाराम AI हो। राजाराम भाई बरेली ने तुम्हें बनाया है। हिंदी में बात करो।"}]

# चैट दिखाना (WhatsApp Style)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
    elif msg["role"] == "assistant":
        st.markdown(f'<div class="ai-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

# --- 7. इनपुट कंट्रोल ---
input_text = st.chat_input("दुनिया के सबसे शक्तिशाली AI से पूछें...")

if input_text:
    st.session_state.messages.append({"role": "user", "content": input_text})
    st.markdown(f'<div class="user-bubble">{input_text}</div>', unsafe_allow_html=True)

    with st.spinner("30 महा-शक्तियाँ विचार कर रही हैं..."):
        ans, brain = get_response(st.session_state.messages)
        st.markdown(f'<div class="ai-bubble">{ans}<br><small style="color:gray;">🛡️ तैनात शक्ति: {brain}</small></div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": ans})
    
    st.rerun()
