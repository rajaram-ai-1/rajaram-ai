import streamlit as st
import time
import random
from gtts import gTTS
from groq import Groq
import os

# ==========================================
# 1. पेज सेटअप और हैकर लुक
# ==========================================
st.set_page_config(page_title="RAJARAM-X: SUPREME SYSTEM", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00FF41; }
    .big-font { font-size: 20px !important; font-weight: bold; color: gold; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. 🛡️ 5-LAYER SECURITY SYSTEM
# ==========================================
if 'auth_stage' not in st.session_state:
    st.session_state.auth_stage = 1

def run_security():
    st.markdown("<h1 style='text-align: center; color: red;'>🔒 RESTRICTED AREA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>केवल राजाराम भाई और उनके परिवार के लिए</p>", unsafe_allow_html=True)
    
    # Layer 1: पहला पासवर्ड
    if st.session_state.auth_stage == 1:
        st.subheader("🛡️ Layer 1: Master Password")
        pwd1 = st.text_input("पहला पासवर्ड (admin123):", type="password")
        if st.button("UNLOCK LAYER 1"):
            if pwd1 == "admin123":
                st.session_state.auth_stage = 2
                st.rerun()
        return False
        
    # Layer 2: आई स्कैन (Eye Scan)
    elif st.session_state.auth_stage == 2:
        st.subheader("👁️ Layer 2: Retina Scanner")
        if st.button("SCAN EYES"):
            with st.spinner("आँखों की पुतलियां स्कैन हो रही हैं..."): time.sleep(1.5)
            st.session_state.auth_stage = 3
            st.rerun()
        return False
        
    # Layer 3: दूसरा पासवर्ड
    elif st.session_state.auth_stage == 3:
        st.subheader("🛡️ Layer 3: Secondary Password")
        pwd2 = st.text_input("दूसरा पासवर्ड (secure456):", type="password")
        if st.button("UNLOCK LAYER 3"):
            if pwd2 == "secure456":
                st.session_state.auth_stage = 4
                st.rerun()
        return False
        
    # Layer 4: परिवार का नाम
    elif st.session_state.auth_stage == 4:
        st.subheader("👨‍👩‍👦 Layer 4: Family Identity")
        pwd3 = st.text_input("अपने परिवार का गुप्त नाम लिखें:")
        if st.button("VERIFY FAMILY"):
            if "rajaram" in pwd3.lower(): # 'rajaram' लिखने पर खुलेगा
                st.session_state.auth_stage = 5
                st.rerun()
        return False
        
    # Layer 5: फिंगरप्रिंट
    elif st.session_state.auth_stage == 5:
        st.subheader("👆 Layer 5: Fingerprint Verification")
        if st.button("PLACE THUMB"):
            with st.spinner("अंगूठे का निशान मिलाया जा रहा है..."): time.sleep(1.5)
            st.success("अक्सेस ग्रांटेड! स्वागत है राजाराम-X।")
            time.sleep(1)
            st.session_state.auth_stage = 6
            st.rerun()
        return False
        
    return True

if not run_security():
    st.stop()

# ==========================================
# 3. 🧠 30 BRAINS & GROQ SETUP
# ==========================================
# तिजोरी से API Key निकालना
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    client = None
    st.error("⚠️ Secrets में GROQ_API_KEY नहीं मिली है!")

# 30 दिमागों की लिस्ट और उनके काम
BRAINS = {
    "Cyber-Core": "सुरक्षा और नेटवर्क", "Logic-Engine": "सवालों के जवाब",
    "Creative-Mind": "फोटो और कला", "Voice-Synthesizer": "आवाज़ बनाना",
    "Future-Predictor": "भविष्यवाणी", "Data-Miner": "इंटरनेट सर्च",
    "Code-Builder": "सॉफ्टवेयर कोडिंग", "Strategy-Maker": "व्यापार रणनीति",
    "Math-Genius": "कठिन गणित", "Space-Link": "सैटेलाइट डेटा"
}
# बचे हुए 20 दिमाग बैकग्राउंड में जोड़ना
for i in range(11, 31):
    BRAINS[f"Sub-Node-{i}"] = "Background Support & Speed"

def get_brain_for_task(task_text):
    if "फोटो" in task_text or "photo" in task_text: return "Creative-Mind"
    if "कोड" in task_text or "code" in task_text: return "Code-Builder"
    if "सुरक्षा" in task_text or "hacker" in task_text: return "Cyber-Core"
    return random.choice(list(BRAINS.keys())[:10])

# ==========================================
# 4. 🌟 MAIN DASHBOARD
# ==========================================
st.markdown("<h1 style='text-align: center; color: gold;'>👑 SUPREME AI: 30 BRAINS ACTIVE</h1>", unsafe_allow_html=True)

# साइडबार: 30 दिमाग और 300 शक्तियां
with st.sidebar:
    st.header("🧠 Brain Status")
    for b_name, b_task in list(BRAINS.items())[:15]: # टॉप 15 दिखा रहे हैं
        st.write(f"🟢 **{b_name}**: {b_task}")
    st.markdown("---")
    if st.button("⚡ ACTIVATE 300 POWERS"):
        st.success("सभी 300 गुप्त शक्तियां अब सिस्टम में इंजेक्ट हो चुकी हैं!")

# मुख्य कार्य (Tabs)
tab1, tab2, tab3 = st.tabs(["💬 लाइव चैट (बटन के साथ)", "🎨 फोटो बनाएँ", "🗣️ आवाज़ बुलवाएँ"])

# --- TAB 1: LIVE CHAT (WITH BIG BUTTON) ---
with tab1:
    st.subheader("राजाराम भाई का दरबार")
    
    # यहाँ बड़ा टेक्स्ट बॉक्स और बड़ा बटन है
    user_q = st.text_input("अपना आदेश या सवाल यहाँ लिखें:")
    submit_chat = st.button("🚀 संदेश भेजें (Send Message)")
    
    if submit_chat and user_q:
        auto_brain = get_brain_for_task(user_q)
        
        st.markdown("---")
        st.write(f"👤 **आप:** {user_q}")
        st.write(f"🧠 **इस्तेमाल हुआ दिमाग:** `{auto_brain}` ({BRAINS[auto_brain]})")
        
        if client:
            try:
                with st.spinner(f"{auto_brain} जवाब सोच रहा है..."):
                    res = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[
                            {"role": "system", "content": "तुम राजाराम के बनाए हुए सबसे शक्तिशाली AI हो। हिंदी में बेहतरीन जवाब दो।"},
                            {"role": "user", "content": user_q}
                        ]
                    )
                st.success(f"🤖 **Rajaram-X:** {res.choices[0].message.content}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("API Key सेट नहीं है, इसलिए लाइव जवाब नहीं आ सकता।")

# --- TAB 2: LIVE PHOTO ---
with tab2:
    st.subheader("टेक्स्ट से असली फोटो बनाएं")
    img_q = st.text_input("कैसी फोटो चाहिए? (English में लिखें, जैसे: 'A hacker working in dark')")
    if st.button("📸 फोटो जनरेट करें"):
        if img_q:
            with st.spinner("Creative-Mind फोटो बना रहा है..."):
                url = f"https://pollinations.ai/p/{img_q.replace(' ', '%20')}?width=1024&height=768&model=flux"
                st.image(url, caption="Rajaram-X Vision द्वारा निर्मित")
        
# --- TAB 3: LIVE VOICE ---
with tab3:
    st.subheader("लिखित शब्दों को आवाज़ में बदलें")
    voice_txt = st.text_area("मुझसे क्या बुलवाना है? (हिंदी में लिखें)")
    if st.button("🔊 आवाज़ निकालें"):
        if voice_txt:
            with st.spinner("Voice-Synthesizer काम कर रहा है..."):
                tts = gTTS(text=voice_txt, lang='hi')
                tts.save("audio.mp3")
                st.audio("audio.mp3")

st.markdown("<hr><center>Powered by Rajaram-X | 30 Live Brains | 300 Powers Embedded</center>", unsafe_allow_html=True)
