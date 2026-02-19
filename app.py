import streamlit as st
from groq import Groq
import random
import time

# --- 1. पेज कॉन्फ़िगरेशन (शाही लुक) ---
st.set_page_config(page_title="RAJARAM-X: THE MASTER AI", layout="wide")
st.markdown("<style>.stApp { background-color: #000; color: #00FF41; }</style>", unsafe_allow_html=True)

# --- 2. 30 दिमागों का असली स्ट्रक्चर ---
MODELS_ARMY = [
    "llama-3.3-70b-versatile", 
    "llama-3.1-8b-instant", 
    "mixtral-8x7b-32768",
    "gemma2-9b-it"
]

# 30 दिमागों का डेटाबेस (हर बार नया लोड होगा)
if 'brain_cluster' not in st.session_state:
    st.session_state.brain_cluster = {f"Brain-Node-{i}": random.choice(MODELS_ARMY) for i in range(1, 31)}

# --- 3. तिजोरी (Secrets) से दिमाग का कनेक्शन ---
try:
    # यहाँ अब चाबी सीधे कोड में नहीं, बल्कि तिजोरी से आ रही है
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error("❌ तिजोरी (Secrets) में चाबी नहीं मिली! कृपया अपनी सहेलियों से कहें कि 'secrets.toml' चेक करें।")
    st.stop()

# --- 4. मुख्य इंटरफ़ेस ---
st.markdown("<h1 style='text-align: center; color: gold;'>👑 RAJARAM-X: 30 BRAINS CLUSTER</h1>", unsafe_allow_html=True)

# साइडबार में 30 दिमागों का लाइव फीड
with st.sidebar:
    st.header("🌐 30 Active Brains")
    for node, model in st.session_state.brain_cluster.items():
        st.write(f"🟢 {node} ({model})")
    
    st.markdown("---")
    if st.button("सिस्टम रीबूट करें"):
        st.rerun()

# --- 5. असली जवाब देने वाली शक्ति (Chat) ---
st.subheader("💬 राजाराम भाई का दरबार (Live AI)")
user_query = st.chat_input("हुकुम करें राजाराम भाई...")

if user_query:
    # 30 में से एक दिमाग चुनना जो इस सवाल का जवाब देगा
    selected_node = random.choice(list(st.session_state.brain_cluster.keys()))
    selected_model = st.session_state.brain_cluster[selected_node]
    
    with st.chat_message("assistant"):
        st.markdown(f"🧠 **सक्रिय दिमाग:** `{selected_node}`")
        try:
            # असली मॉडल से जवाब मंगवाना
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "तुम राजाराम-X के महा-द्रष्टा AI हो। शुद्ध हिंदी में बहुत ही शक्तिशाली और शाही जवाब दो।"},
                    {"role": "user", "content": user_query}
                ],
                model=selected_model,
            )
            st.success(chat_completion.choices[0].message.content)
            
        except Exception as e:
            st.error(f"क्षमा करें, {selected_node} कनेक्ट नहीं हो पाया।")

# --- 6. फोटो निर्माण की शक्ति ---
st.markdown("---")
st.subheader("🖼️ राजाराम-X विज़न (Photo Power)")
col1, col2 = st.columns([1, 2])
with col1:
    img_prompt = st.text_input("क्या फोटो बनाऊं?")
    p_btn = st.button("फोटो बनाओ")
with col2:
    if p_btn and img_prompt:
        url = f"https://pollinations.ai/p/{img_prompt.replace(' ', '%20')}?width=1024&height=720&model=flux"
        st.image(url, caption="Rajaram-X द्वारा निर्मित दृश्य")

st.markdown("<p style='text-align: center; color: gray;'>Rajaram-X Project 2026 | World's First 30-Brain AI Engine</p>", unsafe_allow_html=True)
