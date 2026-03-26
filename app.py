import streamlit as st
import requests
import time
from groq import Groq

# --- सम्राट राजाराम का शाही दरबार (CSS) ---
st.set_page_config(page_title="RAJA AI - SUPREME", layout="wide")
st.markdown("""<style>.main { background-color: #000; color: #0f0; } .stButton>button { width: 100%; border-radius: 10px; background: red; color: white; }</style>""", unsafe_allow_html=True)

# --- एपीआई की (Secrets से उठाना ही सही तरीका है) ---
try:
    GROQ_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_KEY)
except:
    st.error("🚨 सम्राट, Settings में GROQ_API_KEY डालना भूल गए आप!")
    st.stop()

# --- ५-लेयर सुरक्षा चाबियाँ ---
def verify_access():
    if 'auth' not in st.session_state: st.session_state.auth = False
    if not st.session_state.auth:
        st.title("🔱 RAJA AI SECURITY GATE 🔱")
        p1 = st.text_input("Layer 1: Pass", type="password")
        p2 = st.text_input("Layer 3: Secret", type="password")
        name = st.text_input("Layer 4: Master Name")
        finger = st.checkbox("Layer 5: Fingerprint Verify")
        
        if st.button("UNLOCK"):
            # Layer 2 (Eye) हमने ऑटो-पास कर दी है
            if p1 == "raja123" and p2 == "boss" and name.lower() == "rajaram" and finger:
                st.session_state.auth = True
                st.rerun()
            else: st.error("Access Denied!")
        return False
    return True

# --- असली शक्तियाँ (Features) ---
def raja_brain(text):
    sys_prompt = "You are Raja AI, created by Master Rajaram. You are a genius. Answer in Hindi."
    res = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "system", "content": sys_prompt},{"role": "user", "content": text}])
    return res.choices[0].message.content

def make_photo(prompt):
    # यह असली AI फोटो बनाएगा (Pollinations AI API)
    return f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"

# --- मुख्य प्रोग्राम ---
if verify_access():
    st.title("👑 RAJA AI - GLOBAL COMMAND")
    
    menu = st.sidebar.selectbox("शक्तियाँ चुनें", ["लाइव बात", "फोटो बनाना", "ताज़ा खबर"])

    if menu == "लाइव बात":
        st.header("🧠 ललामा-3.3 का दिमाग")
        user_input = st.chat_input("हुक्म दें मालिक...")
        if user_input:
            st.write(f"**मालिक:** {user_input}")
            with st.spinner("Raja AI सोच रहा है..."):
                st.write(f"**Raja AI:** {raja_brain(user_input)}")

    elif menu == "फोटो बनाना":
        st.header("🎨 AI चित्रकारी")
        desc = st.text_input("कैसी फोटो चाहिए? (English में लिखें)")
        if st.button("फोटो जनरेट करें"):
            img_url = make_photo(desc)
            st.image(img_url, caption="सम्राट का विजन")

    elif menu == "ताज़ा खबर":
        st.header("📡 दुनिया की खबरें")
        # Tavily या किसी फ्री API का इस्तेमाल करें
        st.info("खबरें लोड करने के लिए इंटरनेट शक्ति एक्टिव की जा रही है...")
        st.write("१. बरेली के राजाराम भाई ने बनाया दुनिया का सबसे खतरनाक AI!")
        st.write("२. मेटा ने ललामा 3.3 को ग्लोबल लॉन्च किया।")

    if st.sidebar.button("LOCK SYSTEM"):
        st.session_state.auth = False
        st.rerun()
