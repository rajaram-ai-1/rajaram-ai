import streamlit as st
import requests

# --- Page Configuration (Ultra-Premium Theme) ---
st.set_page_config(page_title="Raja AI - Single Core", page_icon="🔱", layout="centered")

# Custom CSS for that 'Photo-like' feel
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #d4af37; }
    .stTextInput>div>div>input { background-color: #111; color: gold; border: 1px solid #d4af37; }
    .stButton>button { 
        background: linear-gradient(45deg, #8a6d3b, #d4af37); 
        color: black; 
        font-weight: bold; 
        width: 100%;
        border-radius: 5px;
        border: none;
    }
    .security-banner { 
        border: 2px solid #d4af37; 
        padding: 15px; 
        text-align: center; 
        border-radius: 10px;
        background: rgba(212, 175, 55, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- Raja AI Header ---
st.markdown('<div class="security-banner"><h1>🔱 RAJA AI: MASTER CORE</h1><p>DHMSR Protocol: STANDBY | Security: 5-LAYER ACTIVE</p></div>', unsafe_allow_html=True)

# --- Sidebar: Master Access ---
st.sidebar.title("🔐 Access Control")
key = st.sidebar.text_input("Master Password:", type="password")

if key == "Rajaram_King":
    st.sidebar.success("Welcome, Rajaram. Core Online.")
    
    # User Command Input
    user_input = st.text_input("आपका हुक्म क्या है, राजा?", placeholder="यहाँ अपना सवाल लिखें...")

    if st.button("EXECUTE COMMAND"):
        if user_input:
            try:
                # Taking API Key from Streamlit Secrets
                api_key = st.secrets["GROQ_API_KEY"]
                
                # Using Meta Llama 3 70B - The most powerful single core
                with st.spinner("Processing with 0-Delay Logic..."):
                    response = requests.post(
                        "https://api.groq.com/openai/v1/chat/completions",
                        headers={"Authorization": f"Bearer {api_key}"},
                        json={
                            "model": "llama3-70b-8192", # Meta's Strongest Model
                            "messages": [{"role": "user", "content": user_input}],
                            "temperature": 0.6
                        },
                        timeout=10
                    )
                    
                    if response.status_code == 200:
                        ans = response.json()['choices'][0]['message']['content']
                        st.markdown("### 🛡️ Core Response:")
                        st.write(ans)
                    else:
                        st.error("🚨 Core Error: API Connection Failed. Check Secrets.")
            except Exception as e:
                st.error(f"🚨 Critical Failure: {str(e)}")
        else:
            st.warning("कमांड खाली नहीं हो सकता।")

else:
    st.warning("⚠️ सिस्टम लॉक है। केवल राजा के पास ही इसकी चाबी है।")

# --- Footer ---
st.markdown("---")
st.caption("Developed by RAJARAM | Powered by Meta Llama 3 & Streamlit | 2026")
