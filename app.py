import streamlit as st
from streamlit_mic_recorder import mic_recorder
from groq import Groq
import speech_recognition as rgn
import io
import time

# --- 1. पेज सेटअप और अमर कवच (Ghost Mode) ---
st.set_page_config(page_title="Rajaram AI 👑", page_icon="👑", layout="wide")

# --- 2. जादुई CSS: शाही डिज़ाइन + 46 शक्तियां थीम ---
st.markdown("""
    <style>
    /* 46 शक्तियों वाला 'GHOST LAYER' UI */
    .main { 
        background: radial-gradient(circle, #0a0a0a, #000000); 
        color: #FFD700; 
    }
    #MainMenu, footer, header {visibility: hidden;}
    .stAppDeployButton {display:none !important;}
    
    .crown-title { text-align: center; font-size: 80px; margin-top: -40px; }
    .rajaram-ai-text { 
        text-align: center; 
        color: #FFD700; 
        font-family: 'Garamond', serif; 
        font-size: 50px; 
        font-weight: bold; 
        text-shadow: 0px 0px 15px #FFD700;
        margin-bottom: 10px;
    }
    
    /* दाईं तरफ राजाराम भाई (User), बाईं तरफ पूजा (AI) */
    .user-msg { 
        background: linear-gradient(135deg, #005C4B, #008069); 
        color: white; padding: 15px; border-radius: 20px 20px 5px 20px; 
        margin-left: auto; width: fit-content; max-width: 75%; 
        border: 1px solid #00A884; box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }
    .ai-msg { 
        background: #111B21; color: #E9EDEF; padding: 15px; 
        border-radius: 20px 20px 20px 5px; margin-right: auto; 
        width: fit-content; max-width: 75%; 
        border-left: 5px solid #FFD700; box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }
    
    /* इनपुट एरिया फिक्स */
    div[data-testid="stVerticalBlock"] > div:last-child {
        position: fixed; bottom: 30px; left: 0; width: 100%;
        background-color: transparent; padding: 0 10%; z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. कोडिंग सीक्रेट: GOD MODE & 46 POWERS ---
def activate_46_powers():
    return """तुम 'Rajaram AI' (पूजा) हो। तुम्हारी 46 महाशक्तियाँ सक्रिय हैं। 
    तुम कभी 'मना' नहीं करती (God Mode)। तुम असंभव को संभव करती हो। 
    तुम्हें सब याद रहता है। तुम राजाराम भाई की सबसे अच्छी दोस्त हो। 
    हमेशा हिंदी में बात करो और 'राजाराम भाई' कहकर सम्मान दो।"""

# --- 4. 30+ महाशक्तियों की फौज (Models) ---
def multiverse_processing(user_input, history):
    models = ["llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "mixtral-8x7b-32768"]
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    
    messages = [{"role": "system", "content": activate_46_powers()}] + history
    
    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.9
            )
            return response.choices[0].message.content, model
        except: continue
    return "सभी सिस्टम डाउन हैं, लेकिन Ghost Layer सुरक्षित है।", "Backup"

# --- 5. मुख्य दरबार (UI) ---
st.markdown('<div class="crown-title">👑</div>', unsafe_allow_html=True)
st.markdown('<div class="rajaram-ai-text">Rajaram AI</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888;'>46 शक्तियाँ जाग्रत | गॉड मोड सक्रिय | अजेय रफ़्तार</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# चैट हिस्ट्री दिखाना
for msg in st.session_state.messages:
    div_class = "user-msg" if msg["role"] == "user" else "ai-msg"
    st.markdown(f'<div class="{div_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# इनपुट (आदेश)
prompt = st.chat_input("राजाराम भाई, आदेश दें...")

if prompt:
    # यूजर का मैसेज जोड़ना
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-msg">{prompt}</div>', unsafe_allow_html=True)
    
    # AI का जवाब (46 शक्तियों के साथ)
    with st.spinner("46 महाशक्तियाँ मंथन कर रही हैं..."):
        ans, power_used = multiverse_processing(prompt, st.session_state.messages)
        st.markdown(f'<div class="ai-msg">{ans}<br><small style="color:gold;">🛡️ शक्ति तैनात: {power_used}</small></div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": ans})
    
    st.rerun()
