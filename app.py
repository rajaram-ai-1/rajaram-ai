import streamlit as st
from streamlit_mic_recorder import mic_recorder
import time

# --- 1. Page Configuration (The 'God-Mode' Look) ---
st.set_page_config(
    page_title="RAJARAM AI V7",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Custom CSS (As per your Screenshot) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #000000; border-right: 2px solid #d4af37; }
    .main-title { color: #ffd700; text-align: center; font-size: 45px; font-weight: bold; text-shadow: 2px 2px #555; }
    .status-bar { color: #00ff00; text-align: center; font-family: monospace; font-size: 18px; }
    .stButton>button { background: #d4af37; color: black; border-radius: 20px; border: none; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: white; border: 1px solid #333; }
    .shield-btn { background: #8a6d3b !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Sidebar (The Architect's Control) ---
with st.sidebar:
    st.markdown("## 🔱 RAJARAM AI V7")
    st.button("🛡️ VIEW SHIELD REPAIR LOGS", key="shield_btn")
    st.write("---")
    st.markdown("**Architect:** Rajaram | **Age:** 15")
    st.write("---")
    
    voice_protocol = st.toggle("Voice Protocol", value=True)
    satellite_search = st.toggle("Satellite Search")
    
    st.write("---")
    st.markdown("### 🔱 GOD-MODE CONTROL")
    admin_key = st.text_input("Admin Key", type="password", placeholder="Enter Secret...")

# --- 4. Main Dashboard UI ---
if admin_key == "Rajaram_King": # अपना असली पासवर्ड यहाँ सेट करें
    
    # Header Section
    st.markdown('<h1 class="main-title">🔱 RAJARAM AI: OMNIPOTENT CORE 🔱</h1>', unsafe_allow_html=True)
    st.markdown('<p class="status-bar">Grid: Bareilly | Status: Immortal | Time: ' + time.strftime("%H:%M:%S") + '</p>', unsafe_allow_html=True)

    # Feature Buttons (As seen in your UI)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.button("🛡️ BYPASS")
    with col2: st.button("💤 SLEEP")
    with col3: st.button("📡 GLOBAL")
    with col4: st.button("🔮 FUTURE")
    with col5: st.button("⚡ 46 POWER")

    st.write("---")

    # --- 5. Fixing the Voice Error (The Mic Logic) ---
    if voice_protocol:
        st.write("### 🎙️ Voice Input System")
        # Corrected: Using the library properly to avoid 'attribute' error
        audio = mic_recorder(
            start_prompt="Start Recording",
            stop_prompt="Stop",
            key='rajaram_mic_unique',
            use_container_width=True
        )
        
        if audio:
            st.success("आदेश रिकॉर्ड हो गया है, राजा!")
            st.audio(audio['bytes'])

    # --- 6. The Omnipotent Chat Input ---
    query = st.chat_input("Ask Rajaram AI anything.")
    
    if query:
        with st.chat_message("user"):
            st.write(query)
        
        with st.spinner("Processing through 30-Brain Cluster..."):
            # यहाँ आपका Meta Llama 3 API लॉजिक जुड़ सकता है
            time.sleep(1)
            st.chat_message("assistant").write(f"राजाराम, आपका 'Omnipotent Core' आदेश पर काम कर रहा है। '{query}' का विश्लेषण पूरा हुआ।")

else:
    st.warning("⚠️ Access Denied. केवल राजा ही इस 'God-Mode' को जगा सकता है।")
    st.image("https://img.icons8.com/clouds/200/000000/lock-landscape.png")

st.markdown("---")
st.caption("Developed by RAJARAM | 2026 Bareilly Grid Control")
