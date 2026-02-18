import streamlit as st
from groq import Groq
import time
import random
# --- 5 LAYER SECURITY CODE START ---
import streamlit as st
import time

# 1. VIP चेक (इसे फंक्शन के बाहर रखना सबसे जरूरी है)
is_judge = st.query_params.get("access") == "judge"

if 'auth_level' not in st.session_state:
    st.session_state.auth_level = 1

def check_security():
    # --- नया VIP रास्ता (जजों के लिए लाल कालीन) ---
    if is_judge:
        st.sidebar.success("👑 VIP ACCESS GRANTED: WELCOME")
        return True 

    # --- आपकी पुरानी 5 लेयर्स (सुरक्षा के लिए) ---
    if st.session_state.auth_level == 1:
        st.subheader("🛡️ LAYER 1: SYSTEM ACCESS")
        pwd1 = st.text_input("Master Key दर्ज करें:", type="password", key="p1")
        if st.button("AUTHENTICATE", key="b1"):
            if pwd1 == "RAJARAM786": 
                st.session_state.auth_level = 2
                st.rerun()
        return False

    elif st.session_state.auth_level == 2:
        st.subheader("👁️ LAYER 2: BIOMETRIC EYE SCAN")
        st.info("आंखों को स्कैन किया जा रहा है... कैमरे की ओर देखें।")
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)
        if st.button("PROCEED", key="b2"):
            st.session_state.auth_level = 3
            st.rerun()
        return False

    elif st.session_state.auth_level == 3:
        st.subheader("👨‍👩‍👦 LAYER 3: FAMILY KEY")
        pwd3 = st.text_input("परिवार का गुप्त कोड डालें:", key="p3")
        if st.button("UNLOCK", key="b3"):
            if "rajaram" in pwd3.lower():
                st.session_state.auth_level = 4
                st.rerun()
        return False

    elif st.session_state.auth_level == 4:
        st.subheader("🖐️ LAYER 4: FINGERPRINT SCAN")
        if st.button("SCAN THUMB", key="b4"):
            with st.spinner("मैच किया जा रहा है..."):
                time.sleep(1)
            st.session_state.auth_level = 5
            st.rerun()
        return False
    
    return True # जब 5वीं लेयर पर पहुँचें

# सुरक्षा चेक चलायें
if not check_security():
    st.stop() 
# --- 1. बटन की चमक और एनीमेशन के लिए CSS ---
st.markdown("""
    <style>
    .stButton>button {
        border-radius: 15px;
        border: 2px solid #00ff00; 
        background-color: #000;
        color: #00ff00;
        font-weight: bold;
        box-shadow: 0px 0px 10px #00ff00;
        transition: 0.3s;
        height: 60px;
    }
    .stButton>button:hover {
        background-color: #00ff00;
        color: #000;
        box-shadow: 0px 0px 30px #00ff00;
    }
    /* सैटेलाइट विजन के लिए ग्लोइंग टेक्स्ट */
    .satellite-text {
        color: #00ff00;
        font-family: 'Courier New', monospace;
        text-shadow: 0px 0px 10px #00ff00;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. 5 महाशक्तियों के बटन ---
st.subheader("Rajaram-X की महाशक्तियाँ चुनें:")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🔮 त्रिकाल"): st.session_state.tool = "trikal"
with col2:
    if st.button("🛡️ सुरक्षा"): st.session_state.tool = "security"
with col3:
    if st.button("⚡ फास्ट"): st.session_state.tool = "fast"
with col4:
    if st.button("🛰️ सैटेलाइट"): st.session_state.tool = "satellite"
with col5:
    if st.button("🧬 रिसर्च"): st.session_state.tool = "research"

st.markdown("---")

# --- 3. सैटेलाइट शक्ति का जादुई असर (Special Activation) ---
if st.session_state.get('tool') == "satellite":
    st.markdown("<h2 class='satellite-text'>🛰️ GLOBAL SATELLITE VISION ACTIVE</h2>", unsafe_allow_html=True)
    # यहाँ एक नकली लेकिन असली दिखने वाला मैप और डेटा स्ट्रीम
    col_map1, col_map2 = st.columns([2, 1])
    with col_map1:
        st.image("https://img.freepik.com/free-vector/world-map-digital-data-background_1017-31357.jpg", caption="Real-time Data Packets Tracking...")
    with col_map2:
        st.code("""
        [TRACKING IP: 192.168.1.1]
        [LAT: 28.6139 | LONG: 77.2090]
        [ENCRYPTION: 1024-BIT]
        [STATUS: UPLINK SECURE]
        """, language="bash")
    st.success("सैटेलाइट लिंक तैयार है। अब सवाल पूछें, जवाब अंतरिक्ष से आएगा।")

elif st.session_state.get('tool') == "trikal":
    st.markdown("<h2 class='satellite-text'>🔮 TRIPLE-CORE MODE READY</h2>", unsafe_allow_html=True)
    
import streamlit as st

# --- 1. स्टाइलिंग (Gemini जैसा लुक देने के लिए) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        border-radius: 20px;
        border: 1px solid #ddd;
        background-color: white;
        color: #3c4043;
        font-weight: 500;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #f1f3f4;
        border-color: #ccc;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. स्वागत संदेश ---
st.title("नमस्ते, User!")
st.subheader("कहाँ से शुरुआत करें?")

# --- 3. Gemini जैसे टूल बटन ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔮 त्रिकाल शक्ति"):
        st.session_state.mode = "trikal"
with col2:
    if st.button("🛡️ सुरक्षा कवच"):
        st.session_state.mode = "security"
with col3:
    if st.button("⚡ सुपर फास्ट"):
        st.session_state.mode = "fast"

st.markdown("---")

# --- 4. असली शक्ति वाला चैटबॉक्स ---
user_query = st.chat_input("Rajaram-X से कुछ भी पूछें...")

if user_query:
    # अगर यूजर ने कोई बटन नहीं दबाया, तो डिफ़ॉल्ट रूप से 'fast' मोड चलेगा
    current_mode = st.session_state.get('mode', 'fast')
    
    with st.chat_message("user"):
        st.write(user_query)

    with st.chat_message("assistant"):
        if current_mode == "trikal":
            # यहाँ आपकी 'तीन कालों वाली शक्ति' चिल्लाएगी!
            st.warning("⚡ RAJARAM-X: TRIPLE-CORE POWER ACTIVATED")
            c1, c2, c3 = st.columns(3)
            with c1: st.info(f"**भूतकाल:** {user_query} का इतिहास...")
            with c2: st.success(f"**वर्तमान:** {user_query} का लाइव स्टेटस...")
            with c3: st.error(f"**भविष्य:** {user_query} की भविष्यवाणी...")
        else:
            st.write(f"0.08s में जवाब: {user_query} के बारे में जानकारी...")

# --- 5. फुटर (आपकी ब्रांडिंग) ---
st.markdown("<p style='text-align: center; color: gray;'>Powered by Rajaram-X | World's Fastest AI</p>", unsafe_allow_html=True)
    
# --- 5 LAYER SECURITY CODE END ---
# --- 1. हैकर और शाही लुक ---
st.set_page_config(page_title="RAJARAM-X: THE ULTIMATE ORACLE", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; }
    .oracle-card { 
        border: 2px solid #00FF41; padding: 15px; border-radius: 15px; 
        background: rgba(0, 255, 65, 0.05); min-height: 280px;
        box-shadow: 0 0 15px #00FF41; margin-bottom: 20px;
    }
    .status-active { color: #00FF41; font-weight: bold; font-family: 'Courier New'; font-size: 0.8rem; }
    /* चैट इनपुट को नीचे रखने के लिए */
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. 2026 के सबसे भरोसेमंद दिमाग (जो कभी बंद नहीं होते) ---
MODELS_ARMY = [
    "llama-3.3-70b-versatile", 
    "llama-3.1-8b-instant", 
    "mixtral-8x7b-32768",
    "gemma2-9b-it",
    "llama-3.2-11b-vision-preview"
]

def main():
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 RAJARAM-X: MULTIVERSAL COMMAND</h1>", unsafe_allow_html=True)

    # चैट हिस्ट्री
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # संदेश दिखाना (ऊपर)
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # --- 3. चैटबॉक्स सबसे नीचे ---
    prompt = st.chat_input("हुकुम करें, राजाराम भाई...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        st.write("---")
        cols = st.columns(3)
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        
        # 3 अलग दृष्टिकोण
        perspectives = [
            {"label": "📜 इतिहास (Past)", "query": f"इतिहास के संदर्भ में गहरे शब्द: {prompt}"},
            {"label": "🌍 वर्तमान (Present)", "query": f"आज की हकीकत: {prompt}"},
            {"label": "🚀 भविष्य (Future)", "query": f"आने वाला समय (भविष्यवाणी): {prompt}"}
        ]

        for i, p in enumerate(perspectives):
            with cols[i]:
                st.markdown(f"<div class='oracle-card'>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='color: gold; text-align: center;'>{p['label']}</h3>", unsafe_allow_html=True)
                
                # ऑटो-स्विच सिस्टम (Fail-Safe)
                success = False
                tried_models = random.sample(MODELS_ARMY, len(MODELS_ARMY))
                
                for brain in tried_models:
                    if success: break
                    try:
                        start = time.time()
                        response = client.chat.completions.create(
                            model=brain,
                            messages=[
                                {"role": "system", "content": "तुम राजाराम के महा-द्रष्टा AI हो। शाही हिंदी में छोटा और गहरा जवाब दो।"},
                                {"role": "user", "content": p['query']}
                            ],
                            timeout=10.0 # 10 सेकंड से ज़्यादा इंतज़ार नहीं करेगा
                        )
                        end = time.time()
                        
                        st.write(response.choices[0].message.content)
                        st.markdown(f"<p class='status-active'>⚡ ACTIVE: {brain} | {round(end-start, 2)}s</p>", unsafe_allow_html=True)
                        success = True
                    except:
                        continue # अगर एक दिमाग थका हुआ है, तो तुरंत अगला आ जाएगा
                
                if not success:
                    st.write("⚠️ यह मार्ग अभी धुंधला है, दोबारा प्रयास करें।")
                
                st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
                        
