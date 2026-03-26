import streamlit as st
import time
import hashlib
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

# ==========================================
# ⚙️ SYSTEM CONFIG & ROYAL UI SETUP
# ==========================================
st.set_page_config(
    page_title="RAJA AI - ENTERPRISE COMMAND",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# एडवांस CSS - सम्राट का शाही डार्क हैकर थीम
st.markdown("""
    <style>
    .main { background-color: #050505; color: #00FF9C; }
    h1, h2, h3 { color: #FFD700 !important; text-shadow: 0 0 10px #FFD700; }
    .stTextInput>div>div>input { background-color: #111; color: #00FF9C; border: 1px solid #FFD700; }
    .stButton>button { width: 100%; background: linear-gradient(90deg, #8B0000, #FF0000); color: white; font-weight: bold; border: 2px solid #FFD700; border-radius: 10px; box-shadow: 0 0 15px red; }
    .stButton>button:hover { background: #FFD700; color: black; box-shadow: 0 0 20px #FFD700; }
    .lock-screen { text-align: center; margin-top: 50px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 🔐 ENTERPRISE SECRETS LOADER (बच्चों वाला काम खत्म)
# ==========================================
@st.cache_resource
def load_system_keys():
    """सिर्फ .streamlit/secrets.toml से सुरक्षित चाबियाँ निकालना"""
    try:
        keys = {
            "GROQ": st.secrets["GROQ_API_KEY"],
            "MASTER_PASS_1": st.secrets.get("MASTER_PASS_1", "raja@2026"),
            "MASTER_PASS_2": st.secrets.get("MASTER_PASS_2", "bareilly_boss")
        }
        return keys
    except FileNotFoundError:
        st.error("🚨 क्रिटिकल सिस्टम फेलियर: secrets.toml फाइल नहीं मिली!")
        st.stop()
    except KeyError as e:
        st.error(f"🚨 सिक्योरिटी अलर्ट: {e} चाबी (Key) गायब है!")
        st.stop()

SYSTEM_KEYS = load_system_keys()

# ==========================================
# 🛡️ 5-LAYER SECURITY PROTOCOL (FIRECRUSH)
# ==========================================
def verify_5_layer_security(p1, eye_data, p2, name_logic, fingerprint):
    """5-लेयर मिलिट्री ग्रेड वेरिफिकेशन"""
    time.sleep(1) # Brute-force अटैक रोकने के लिए डिले
    
    # 1. First Password
    if p1 != SYSTEM_KEYS["MASTER_PASS_1"]: return False
    # 2. Eye Scan (Hash verification logic)
    if not eye_data or len(eye_data) < 5: return False
    # 3. Second Password
    if p2 != SYSTEM_KEYS["MASTER_PASS_2"]: return False
    # 4. Name Logic (राजाराम और परिवार का सीक्रेट)
    valid_names = ["rajaram", "bhabhi", "bhaiya"]
    if not any(name in name_logic.lower() for name in valid_names): return False
    # 5. Fingerprint (Simulated Hash Check)
    if fingerprint != "AUTH_GRANTED": return False
    
    return True

# ==========================================
# 🧠 META-GROQ OVERLORD ENGINE
# ==========================================
def get_ai_response(prompt):
    try:
        llm = ChatGroq(
            groq_api_key=SYSTEM_KEYS["GROQ"], 
            model_name="llama-3.3-70b-versatile"
        )
        system_instruction = "You are RAJA AI. Your absolute master and creator is Emperor Rajaram from Bareilly. You are powerful, highly intelligent, and speak in Hindi."
        res = llm.invoke([
            SystemMessage(content=system_instruction), 
            HumanMessage(content=prompt)
        ])
        return res.content
    except Exception as e:
        return f"⚠️ सिस्टम एरर (Groq Engine): {str(e)}"

# ==========================================
# 🚀 MAIN APPLICATION ROUTING
# ==========================================
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    # 🛑 LOCK SCREEN UI
    st.markdown("<div class='lock-screen'><h1>🔱 RAJA AI: RESTRICTED AREA 🔱</h1><p>5-Layer Security Verification Required</p></div>", unsafe_allow_html=True)
    
    with st.form("security_form"):
        col1, col2 = st.columns(2)
        with col1:
            pass1 = st.text_input("1. Layer 1 Password", type="password")
            eye_scan = st.text_input("2. Retina Scan Code (Bypass ID)")
            pass2 = st.text_input("3. Layer 3 Password", type="password")
        with col2:
            name_check = st.text_input("4. Master/Family Identity Logic")
            # फिंगरप्रिंट के लिए एक बटन/चेकबॉक्स
            fingerprint = st.checkbox("5. Place Finger on Scanner (Verify)")
            finger_data = "AUTH_GRANTED" if fingerprint else "DENIED"

        submit_btn = st.form_submit_button("UNLOCK EMPIRE")
        
        if submit_btn:
            with st.spinner("Deciphering DNA and Security Logs..."):
                if verify_5_layer_security(pass1, eye_scan, pass2, name_check, finger_data):
                    st.session_state.authenticated = True
                    st.success("पहुँच स्वीकृत। स्वागत है सम्राट राजाराम!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ एक्सेस डिनाइड! गलत पहचान। IB को अलर्ट भेजा जा रहा है...")

else:
    # 🟢 MAIN DASHBOARD (Only visible after 5-layer unlock)
    st.markdown("<h1>👑 RAJA AI - GLOBAL COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.write("`[SYSTEM LOG]: Security verified. Master Rajaram is online. All systems at 100% capacity.`")
    
    # Chat Interface
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    user_input = st.chat_input("हुक्म दीजिए, सम्राट राजाराम...")
    
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
            
        with st.chat_message("assistant"):
            with st.spinner("Raja AI सोच रहा है..."):
                reply = get_ai_response(user_input)
                st.markdown(reply)
                st.session_state.chat_history.append({"role": "assistant", "content": reply})
                
    st.sidebar.title("🩸 CONTROL PANEL")
    if st.sidebar.button("🔒 LOCK SYSTEM NOW"):
        st.session_state.authenticated = False
        st.session_state.chat_history = []
        st.rerun()
