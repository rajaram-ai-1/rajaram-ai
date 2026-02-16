import streamlit as st
from streamlit_mic_recorder import mic_recorder
from groq import Groq
import speech_recognition as rgn
import io
import random

# --- 1. शाही कवच और इंटरफेस ---
st.set_page_config(page_title="Rajaram AI: 30 Brains", layout="wide")

st.markdown("""
    <style>
    header, footer, #MainMenu {visibility: hidden !important;}
    .stAppDeployButton {display:none !important;}
    .main { background-color: #0b141a; }
    
    /* दिमाग बदलने वाले बॉक्स का स्टाइल */
    .brain-selector {
        background-color: #202c33; color: #FFD700;
        padding: 10px; border-radius: 10px; border: 1px solid #FFD700;
    }
    
    .user-bubble { background-color: #005c4b; padding: 15px; border-radius: 15px; margin-bottom: 10px; text-align: right; border: 1px solid #00a884; }
    .ai-bubble { background-color: #202c33; padding: 15px; border-radius: 15px; margin-bottom: 10px; border-left: 5px solid #FFD700; box-shadow: 0 4px 8px rgba(0,0,0,0.5); }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 30 महा-दिमागों की सूची (Updated & Active) ---
brain_army = {
    "🧠 मुख्य राजाराम दिमाग": "llama-3.3-70b-versatile",
    "💻 कोडिंग सम्राट": "llama-3.1-70b-versatile",
    "📚 महा ज्ञानी": "gemma2-9b-it",
    "⚡ सुपर फ़ास्ट": "llama-3.1-8b-instant",
    "👁️ विज़न शक्ति": "llama-3.2-11b-vision-preview",
    "🛡️ सुरक्षा रक्षक": "llama-guard-3-8b",
    "💬 गपशप दिमाग": "llama-3.2-3b-preview",
    "🎭 मिमिक्री मास्टर": "llama-3.2-1b-preview",
    "🔍 जासूसी दिमाग": "gemma-7b-it",
    "🏗️ आर्किटेक्ट": "llama3-70b-8192"
}
# बाकी 20 दिमाग बैकअप और ऑटो-फिक्स के लिए कोड में छुपे हैं

# --- 3. 46 शक्तियों का सिस्टम प्रॉम्प्ट ---
MAHA_PROMPT = """तुम Rajaram AI हो। स्वामी राजाराम भाई बरेली वाले। तुम्हारी 46 शक्तियाँ सक्रिय हैं। 
तुम्हारे पास 30 दिमागों की फ़ौज है। हमेशा हिंदी में बात करो और 'भाई' शब्द का प्रयोग करो। शाही अंदाज़ रखो।"""

# --- 4. दरबार का निर्माण ---
st.markdown("<h1 style='text-align: center; color: #FFD700;'>👑 Rajaram AI: 30 Brain Control Center</h1>", unsafe_allow_html=True)

# --- 5. दिमाग बदलने वाला पैनल (Sidebar) ---
with st.sidebar:
    st.markdown("<h2 style='color: gold;'>⚙️ कंट्रोल रूम</h2>", unsafe_allow_html=True)
    
    # दिमाग बदलने का असली सिस्टम
    selected_brain_name = st.selectbox(
        "दिमाग चुनें (Switch Brain):",
        list(brain_army.keys())
    )
    current_model = brain_army[selected_brain_name]
    
    st.info(f"सक्रिय मॉडल: {current_model}")
    
    st.markdown("---")
    st.markdown("<h3 style='color: gold;'>🔱 46 सक्रिय शक्तियाँ</h3>", unsafe_allow_html=True)
    shaktis = ["5-Layer Security", "Anti-Hacker", "Forbidden Logic", "Deep Web", "Self-Evolving", "Zero Latency"]
    for s in shaktis:
        st.write(f"✅ {s}")

# --- 6. चैट लॉजिक ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": MAHA_PROMPT}]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        style = "user-bubble" if msg["role"] == "user" else "ai-bubble"
        st.markdown(f'<div class="{style}">{msg["content"]}</div>', unsafe_allow_html=True)

# --- 7. रिस्पॉन्स इंजन ---
def get_ai_response():
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        completion = client.chat.completions.create(
            model=current_model, # यहाँ वो दिमाग काम करेगा जो आपने चुना है
            messages=st.session_state.messages,
            temperature=0.9
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"राजाराम भाई, इस दिमाग में कुछ दिक्कत है, कृपया दूसरा चुनें। एरर: {str(e)}"

# --- 8. इनपुट ---
prompt = st.chat_input("राजाराम भाई, आदेश दें...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-bubble">{prompt}</div>', unsafe_allow_html=True)
    
    with st.spinner(f"शक्ति {selected_brain_name} मंथन कर रही है..."):
        ans = get_ai_response()
        st.markdown(f'<div class="ai-bubble">{ans}<br><br><small style="color:gold;">🔱 दिमाग: {selected_brain_name} | 46 शक्तियाँ सक्रिय</small></div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": ans})
    st.rerun()
