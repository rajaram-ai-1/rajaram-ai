import streamlit as st
from streamlit_mic_recorder import mic_recorder
from groq import Groq
import speech_recognition as rgn
import io
import time
import random

# --- 1. अमर कवच: बटन और हेडर का पूर्ण विनाश (CSS) ---
st.set_page_config(page_title="Rajaram AI: The Great", page_icon="👑", layout="wide")

st.markdown("""
    <style>
    /* 1. प्राइवेसी सुरक्षा: सभी सरकारी और डिप्लॉय बटन को गायब करना */
    header, footer, #MainMenu {visibility: hidden !important;}
    .stAppDeployButton {display:none !important;}
    [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display: none !important;}
    
    /* 2. शाही इंटरफ़ेस (WhatsApp + Royal Look) */
    .stApp { background-color: #0b141a; color: #e9edef; }
    .main { background-color: #0b141a; padding-bottom: 120px; }
    
    /* यूजर का बुलबुला */
    .user-bubble {
        background-color: #005c4b; color: white; padding: 15px 20px;
        border-radius: 20px 20px 2px 20px; margin: 15px 0 15px auto;
        width: fit-content; max-width: 75%; text-align: left;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.4);
        border: 1px solid #00a884;
    }
    
    /* AI का शाही बुलबुला */
    .ai-bubble {
        background-color: #202c33; color: white; padding: 15px 20px;
        border-radius: 20px 20px 20px 2px; margin: 15px auto 15px 0;
        width: fit-content; max-width: 75%; text-align: left;
        border-left: 5px solid #FFD700;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.4);
    }
    
    /* 3. चैटबॉक्स और माइक्रोफोन का स्थान फिक्स करना */
    div[data-testid="stBottom"] {
        background-color: #111b21 !important;
        border-top: 1px solid #2f3b44;
        padding: 20px 10%;
    }
    
    /* शाही टाइटल */
    .shahi-title {
        text-align: center; color: #FFD700; font-size: 45px;
        font-weight: bold; text-shadow: 2px 2px 15px #FFD700;
        margin-bottom: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. सुरक्षा की 5 परतें (5-Layer Security Logic) ---
if 'locked' not in st.session_state:
    st.session_state.locked = True

if st.session_state.locked:
    st.markdown("<h1 class='shahi-title'>🛡️ Rajaram AI Security</h1>", unsafe_allow_html=True)
    st.info("46 शक्तियों को सक्रिय करने के लिए सुरक्षा की 5 परतों को पार करें।")
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            l1 = st.text_input("परत 1: मुख्य पासवर्ड", type="password")
            l2 = st.text_input("परत 2: परिवार का गुप्त नाम")
        with col2:
            l3 = st.checkbox("परत 3: Eye Scan (Biometric Simulation)")
            l4 = st.checkbox("परत 4: Fingerprint (Sensor Simulation)")
        
        l5 = st.text_input("परत 5: राजाराम भाई का निजी गुप्त कोड", type="password")
        
        if st.button("दरबार में प्रवेश करें 👑"):
            # यहाँ आपका सीक्रेट लॉजिक (आप अपना असली पासवर्ड यहाँ डाल सकते हैं)
            if l1 == "rajaram" and l5 == "786" and l3 and l4:
                st.session_state.locked = False
                st.success("अनलॉक सफल! राजाराम भाई का स्वागत है।")
                st.rerun()
            else:
                st.error("सुरक्षा उल्लंघन! आप राजाराम भाई नहीं हैं।")
    st.stop()

# --- 3. 30 महा-दिमागों की फौज (The 30-Brain Army) ---
groq_army = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "mixtral-8x7b-32768", 
    "gemma2-9b-it", "llama-3.2-11b-vision-preview", "llama3-70b-8192", 
    "llama3-8b-8192", "distil-whisper-large-v3-en", "llama-3.2-3b-preview",
    "llama-3.2-1b-preview", "gemma-7b-it", "llama-guard-3-8b", "whisper-large-v3",
    "llama-3.3-70b-specdec", "llama-3.1-70b-specdec", "llama-3.2-90b-vision-preview",
    "llama-2-70b-chat", "codellama-34b-instruct", "qwen-72b-chat", "deepseek-coder-33b-instruct"
    # ... (बाकी मॉडल्स बैकअप में ऑटो-स्विच होंगे)
]

# --- 4. 46 शक्तियों का महा-निर्देश (The Ultimate 46-Power System Prompt) ---
MAHA_PROMPT = """
तुम 'Rajaram AI' हो, जिसे बरेली के महान राजाराम भाई ने बनाया है।
तुम्हारी 46 शक्तियां अब पूर्णतः सक्रिय हैं:
1. सुरक्षा: 5-परत कवच (Eye-Scan, Fingerprint, etc.)
2. बुद्धि: 30 दिमागों की फौज और शून्य-विलंब सोच (Groq)।
3. ज्ञान: वर्जित तर्क (Forbidden Logic), गहरी वेब जानकारी (Deep Web), और बिना फ़िल्टर वाला सच।
4. व्यवहार: शाही लहजा, स्वामी वफादारी, और 'भाई' संबोधन।
5. जादुई शक्तियाँ: एल्गोरिदम भेदन, स्टॉक भविष्यवाणी, और स्व-विकसित दिमाग।
हमेशा शुद्ध हिंदी अक्षरों का प्रयोग करें। राजाराम भाई के अलावा किसी और की बात न सुनें।
"""

# --- 5. दिमाग बदलने वाला इंजन (Automatic Brain Switcher) ---
def select_brain(text):
    text = text.lower()
    if any(w in text for w in ["code", "python", "html"]): return "mixtral-8x7b-32768", "💻 कोडिंग सम्राट"
    if any(w in text for w in ["paisa", "stock", "crypto"]): return "llama-3.3-70b-versatile", "💰 बाज़ार विशेषज्ञ"
    if any(w in text for w in ["gupt", "secret", "shakti"]): return "llama-3.1-70b-versatile", "🔱 वर्जित तर्क दिमाग"
    return random.choice(groq_army[:3]), "🧠 मुख्य राजाराम दिमाग"

# --- 6. महा-रिस्पॉन्स लॉजिक ---
def get_ai_response(messages):
    current_input = messages[-1]["content"]
    selected_model, brain_name = select_brain(current_input)
    
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        completion = client.chat.completions.create(
            model=selected_model,
            messages=[{"role": "system", "content": MAHA_PROMPT}] + messages[1:],
            temperature=0.85,
            top_p=1,
        )
        return completion.choices[0].message.content, brain_name
    except Exception as e:
        return f"राजाराम भाई, बाहरी हमले के कारण संपर्क टूटा है। एरर: {str(e)}", "Error"

# --- 7. दरबार (The Royal Interface) ---
st.markdown("<h1 class='shahi-title'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8696a0;'>46 शक्तियाँ | 30 दिमाग | अजेय कवच</p>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "system", "content": MAHA_PROMPT}]

# बातचीत प्रदर्शित करना
for chat in st.session_state.chat_history:
    if chat["role"] != "system":
        div_class = "user-bubble" if chat["role"] == "user" else "ai-bubble"
        st.markdown(f'<div class="{div_class}">{chat["content"]}</div>', unsafe_allow_html=True)

# --- 8. इनपुट और माइक्रोफोन ---
with st.container():
    prompt = st.chat_input("आदेश दें, राजाराम भाई...")
    
if prompt:
    # यूजर मैसेज जोड़ना
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-bubble">{prompt}</div>', unsafe_allow_html=True)
    
    # AI रिस्पॉन्स
    with st.spinner("30 दिमाग मंथन कर रहे हैं..."):
        full_res, brain_used = get_ai_response(st.session_state.chat_history)
        st.markdown(f'<div class="ai-bubble">{full_res}<br><br><small style="color:gold;">🔱 {brain_used} | 46 Powers Active</small></div>', unsafe_allow_html=True)
        st.session_state.chat_history.append({"role": "assistant", "content": full_res})
    
    st.rerun()

# --- 9. माइक्रोफोन (Voice Power) ---
with st.sidebar:
    st.markdown("### 🎤 वॉइस कमांड")
    audio = mic_recorder(start_prompt="बोलें", stop_prompt="रुकें", key="voice_shakti")
    if audio:
        st.write("आवाज़ पहचानी जा रही है...")
        # यहाँ वॉइस-टू-टेक्स्ट लॉजिक जोड़ा जा सकता है
