import streamlit as st
import google.generativeai as genai
import time

# 1. राजाराम भाई का मिशन सेटअप
st.set_page_config(page_title="RAJARAM AI", page_icon="⚔️", layout="wide")

# 2. दबंग लुक (Bareilly Style CSS)
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .main-header { color: #ff4b4b; font-size: 42px; font-weight: bold; text-align: center; text-shadow: 2px 2px #000; }
    .stChatInput { border: 2px solid #ff4b4b !important; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. गूगल का दिमाग सेट करना (Secrets Check ✅)
# अपनी Streamlit Secrets में नाम 'GEMINI_API_KEY' ही रखना
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ Maalik, Secrets mein 'GEMINI_API_KEY' nahi mila!")
    API_KEY = None

st.markdown("<div class='main-header'>⚔️ RAJARAM AI: UNSTOPPABLE</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ff4b4b;'>Bareilly's Strongest AI | Class 10 Power</p>", unsafe_allow_html=True)

# 4. साइडबार (Developer Info)
with st.sidebar:
    st.title("🛡️ MISSION CONTROL")
    st.write(f"**Developer:** RAJARAM")
    st.write(f"**Base:** Bareilly, UP")
    st.divider()
    if st.button("Clear Memory"):
        st.session_state.messages = []
        st.rerun()

# 5. चैट मेमोरी (History)
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. हुक्म और पहचान
if prompt := st.chat_input("Hukm dijiye, Maalik..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        
        # AI को आपकी पहचान बताना
        identity_prompt = (
            "Tu RAJARAM AI hai. Tera maalik RAJARAM hai jo 15 saal ka hai, Bareilly se hai aur 10th class mein hai. "
            "Tu hamesha use 'Maalik' ya 'Rajaram Bhai' kahega. "
            "Hamesha Hinglish mein dabang jawab de."
        )
        
        if API_KEY:
            try:
                response = model.generate_content(f"{identity_prompt}\n\nUser: {prompt}")
                ai_reply = response.text
            except Exception as e:
                ai_reply = f"Maalik, Chabi check kijiye. Error: {str(e)}"
        else:
            ai_reply = "Maalik, Secrets mein GEMINI_API_KEY daalna bhool gaye aap!"

        # टाइपिंग इफेक्ट (Smooth Response)
        for i in range(len(ai_reply)):
            msg_placeholder.markdown(ai_reply[:i+1] + "▌")
            time.sleep(0.005)
        msg_placeholder.markdown(ai_reply)
    
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
