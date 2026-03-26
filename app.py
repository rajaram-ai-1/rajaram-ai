import streamlit as st
import time

# --- पन्ना सेटिंग्स ---
st.set_page_config(page_title="RAJA AI - BAREILLY TO USA", page_icon="👑", layout="wide")

# --- शाही लुक (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00FF9C; }
    .stTextInput>div>div>input { background-color: #111; color: #00FF9C; border: 1px solid #FFD700; }
    .stButton>button { background: linear-gradient(90deg, #8B0000, #FF0000); color: white; border: 2px solid #FFD700; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- ५-लेयर सुरक्षा लॉजिक ---
def check_security(p1, eye, p2, name, finger):
    # यह आपका सीक्रेट लॉजिक है
    if p1 == "raja123" and p2 == "boss" and "rajaram" in name.lower() and finger:
        return True
    return False

# --- सिस्टम की स्थिति ---
if 'locked' not in st.session_state:
    st.session_state.locked = True

# --- १. लॉगिन स्क्रीन (लॉक्ड मोड) ---
if st.session_state.locked:
    st.title("🔱 RAJA AI: 5-LAYER SECURITY 🔱")
    st.write("`[SYSTEM]: Bareilly-05 Grid Active. Identity required.`")
    
    with st.container():
        col1, col2 = st.columns(2)
        p1 = col1.text_input("Layer 1: Password", type="password")
        eye = col1.text_input("Layer 2: Eye Scan ID (Any Code)")
        p2 = col2.text_input("Layer 3: Secret Password", type="password")
        name = col2.text_input("Layer 4: Family Name Logic")
        finger = st.checkbox("Layer 5: Fingerprint Verification")
        
        if st.button("UNLOCK EMPIRE"):
            if check_security(p1, eye, p2, name, finger):
                st.session_state.locked = False
                st.success("स्वागत है सम्राट राजाराम! साम्राज्य खुल रहा है...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("एक्सेस डिनाइड! गलत पहचान।")

# --- २. मेन डैशबोर्ड (अनलॉक्ड मोड) ---
else:
    st.title("👑 RAJA AI - COMMAND CENTER")
    st.write("`[LOG]: Master Rajaram Online.`")
    
    # API KEY चेक (बिना एरर वाला तरीका)
    if "GROQ_API_KEY" not in st.secrets:
        st.warning("⚠️ सम्राट, आपने अभी तक Streamlit Settings में 'GROQ_API_KEY' नहीं डाली है।")
    else:
        st.success("✅ सिस्टम पूरी तरह चार्ज है।")
        # यहाँ आपका असली चैट लॉजिक आएगा
        user_chat = st.chat_input("हुक्म दें मालिक...")
        if user_chat:
            st.write(f"**राजाराम:** {user_chat}")
            st.write(f"**Raja AI:** मालिक, मैं आपके आदेश पर काम करना शुरू कर रहा हूँ।")

    if st.sidebar.button("LOCK SYSTEM"):
        st.session_state.locked = True
        st.rerun()
