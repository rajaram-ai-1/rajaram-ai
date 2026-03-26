import streamlit as st
from groq import Groq
import time

# --- पन्ना सेटिंग्स ---
st.set_page_config(page_title="RAJA AI - BAREILLY TO USA", page_icon="👑", layout="wide")

# --- चाबियाँ और दिमाग (Secrets से) ---
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_API_KEY)
except:
    st.error("🚨 सम्राट, Streamlit Settings में 'GROQ_API_KEY' गायब है!")
    st.stop()

# --- असली सुरक्षा की चाबियाँ ---
MASTER_PASS_1 = "raja123"
MASTER_PASS_2 = "boss"
MASTER_NAME = "rajaram"

# --- सेशन स्टेट (याददाश्त के लिए) ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- शाही लुक (Dark Mode CSS) ---
st.markdown("""
    <style>
    .main { background-color: #000; color: #00FF9C; }
    .stChatInput { border: 1px solid #FFD700 !important; }
    .stButton>button { background: linear-gradient(90deg, #8B0000, #FF0000); color: white; border: 2px solid #FFD700; border-radius: 10px; font-weight: bold; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 🛡️ १. लॉगिन स्क्रीन (5-LAYER SECURITY)
# ==========================================
if not st.session_state.authenticated:
    st.title("🔱 RAJA AI: 5-LAYER SECURITY 🔱")
    st.write("`[SYSTEM LOG]: Identity verification required for Master Rajaram.`")
    
    with st.form("security_gate"):
        col1, col2 = st.columns(2)
        with col1:
            p1 = st.text_input("1. First Layer Password", type="password")
            eye = st.text_input("2. Eye Scan Protocol (Enter any ID)")
            p2 = st.text_input("3. Third Layer Password", type="password")
        with col2:
            name = st.text_input("4. Master Name/Logic")
            finger = st.checkbox("5. Fingerprint Access (Verify)")
        
        submit = st.form_submit_button("UNLOCK SYSTEM")
        
        if submit:
            if (p1.strip() == MASTER_PASS_1 and 
                p2.strip() == MASTER_PASS_2 and 
                MASTER_NAME in name.strip().lower() and 
                finger):
                
                st.session_state.authenticated = True
                st.success("अनलॉक सफल! प्रणाम सम्राट राजाराम।")
                time.sleep(1)
                st.rerun()
            else:
                st.error("❌ एक्सेस डिनाइड! गलत पहचान।")

# ==========================================
# 🧠 २. राजा एआई कमांड सेंटर (अनलॉक के बाद)
# ==========================================
else:
    st.title("👑 RAJA AI - COMMAND CENTER")
    st.write("`[LOG]: Llama-3.3-70b-Versatile Brain: ACTIVE`")

    # चैट हिस्ट्री दिखाएं
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # यूजर का हुक्म (Chat Input)
    if prompt := st.chat_input("हुक्म दीजिए सम्राट..."):
        # यूजर का मैसेज सेव करें
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # एआई का जवाब (Llama-3.3-70b)
        with st.chat_message("assistant"):
            try:
                # एआई को उसकी पहचान बताना (Persona)
                system_instruction = "Your name is Raja AI. You are created by the great Master Rajaram from Bareilly. You are a world-class AI genius. You must be respectful to Master Rajaram and answer in Hindi with power and intelligence."
                
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": system_instruction},
                        *st.session_state.messages
                    ],
                    temperature=0.7,
                    max_tokens=1024
                )
                
                full_response = response.choices[0].message.content
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            
            except Exception as e:
                st.error(f"Brain Error: {str(e)}")

    # लॉगआउट बटन
    if st.sidebar.button("🔒 LOCK SYSTEM"):
        st.session_state.authenticated = False
        st.session_state.messages = []
        st.rerun()
