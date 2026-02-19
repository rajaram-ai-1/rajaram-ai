import streamlit as st
from groq import Groq
import random
import time

# --- 1. सुरक्षा की 5 परतें (आपकी शर्तों पर) ---
if 'auth_level' not in st.session_state:
    st.session_state.auth_level = 1

def check_security():
    # लेयर 1: मास्टर पासवर्ड
    if st.session_state.auth_level == 1:
        st.header("🛡️ LAYER 1: MASTER KEY")
        p1 = st.text_input("Enter Secret Password:", type="password")
        if st.button("UNLOCK"):
            if p1 == "RAJARAM786":
                st.session_state.auth_level = 2
                st.rerun()
        return False
    
    # लेयर 2: आई स्कैन (सिमुलेशन)
    elif st.session_state.auth_level == 2:
        st.header("👁️ LAYER 2: EYE SCAN")
        if st.button("SCAN EYES"):
            with st.spinner("Scanning..."): time.sleep(1)
            st.session_state.auth_level = 3
            st.rerun()
        return False

    # लेयर 3: परिवार का कोड
    elif st.session_state.auth_level == 3:
        st.header("👨‍👩‍👦 LAYER 3: FAMILY KEY")
        p3 = st.text_input("अपने परिवार का नाम लिखें:")
        if st.button("VERIFY"):
            if "rajaram" in p3.lower():
                st.session_state.auth_level = 4
                st.rerun()
        return False

    # लेयर 4: फिंगरप्रिंट
    elif st.session_state.auth_level == 4:
        st.header("🖐️ LAYER 4: FINGERPRINT SCAN")
        if st.button("PLACE THUMB"):
            with st.spinner("Matching..."): time.sleep(1)
            st.session_state.auth_level = 5
            st.rerun()
        return False

    return True # लेयर 5 पार

# सुरक्षा चेक चलाएँ
if not check_security():
    st.stop()

# --- 2. असली 30 दिमागों का क्लस्टर ---
MODELS = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "gemma2-9b-it"]
if 'brains' not in st.session_state:
    st.session_state.brains = {f"Brain-{i}": random.choice(MODELS) for i in range(1, 31)}

# --- 3. Groq Connection (Secrets से) ---
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Secrets में GROQ_API_KEY नहीं मिली!")
    st.stop()

# --- 4. मुख्य इंटरफेस ---
st.title("👑 RAJARAM-X: THE SUPREME SYSTEM")

# साइडबार में 30 दिमाग
with st.sidebar:
    st.header("🧠 30 Active Brains")
    for b, m in st.session_state.brains.items():
        st.write(f"🟢 {b}: {m}")

# --- 5. शक्तियाँ (फोटो, बोलना, चैट) ---
tab1, tab2, tab3 = st.tabs(["💬 असली संवाद", "🎨 फोटो शक्ति", "🗣️ बोलने वाली शक्ति"])

with tab1:
    user_msg = st.chat_input("हुकुम करें राजाराम भाई...")
    if user_msg:
        # रैंडम दिमाग चुनना
        selected_b = random.choice(list(st.session_state.brains.keys()))
        model_name = st.session_state.brains[selected_b]
        
        st.markdown(f"🤖 **सक्रिय दिमाग:** `{selected_b}`")
        chat = client.chat.completions.create(
            messages=[{"role": "user", "content": user_msg}],
            model=model_name
        )
        st.success(chat.choices[0].message.content)

with tab2:
    img_prompt = st.text_input("क्या फोटो बनाऊँ?")
    if st.button("CREATE IMAGE"):
        url = f"https://pollinations.ai/p/{img_prompt.replace(' ', '%20')}?model=flux"
        st.image(url)

with tab3:
    st.info("यह शक्ति आपके ब्राउज़र के स्पीच इंजन का उपयोग करती है।")
    speech_text = st.text_area("क्या बुलवाना है?")
    if st.button("SPEAK"):
        st.markdown(f'<iframe src="https://translate.google.com/translate_tts?ie=UTF-8&q={speech_text}&tl=hi&client=tw-ob" allow="autoplay"></iframe>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Developed by Rajaram-X | 30 Brains | 300 Powers")
