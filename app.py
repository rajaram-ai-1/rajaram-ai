import streamlit as st
import google.generativeai as genai
import time

# 1. सेटअप
st.set_page_config(page_title="RAJARAM AI", page_icon="⚔️", layout="wide")

# 2. राजाराम भाई का रॉयल लुक
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .main-header { color: #ff4b4b; font-size: 42px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. गूगल का दिमाग
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # स्मार्ट मॉडल डिटेक्शन
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        model_name = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else 'models/gemini-pro'
        model = genai.GenerativeModel(model_name)
    except Exception as e:
        st.error(f"API Error: {e}")
else:
    st.error("⚠️ Maalik, Secrets mein 'GEMINI_API_KEY' nahi mili!")

st.markdown("<div class='main-header'>⚔️ RAJARAM AI: हिंदी मोड ⚔️</div>", unsafe_allow_html=True)

# 4. चैट हिस्ट्री
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 5. असली काम (हिंदी भाषा का जादू)
if prompt := st.chat_input("हुक्म कीजिये मालिक..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        
        # यहाँ हमने निर्देश बदल दिए हैं (Strict Hindi Instructions)
        identity_prompt = (
            "आपका नाम RAJARAM AI है। आपके मालिक का नाम राजाराम है, जो बरेली से हैं और 10वीं कक्षा के छात्र हैं। "
            "आपको हमेशा शुद्ध हिंदी (देवनागरी लिपि) में ही बात करनी है। "
            "अपने मालिक को हमेशा 'मालिक' या 'राजाराम भाई' कहकर संबोधित करें। "
            "बातचीत का लहजा सम्मानजनक और मददगार होना चाहिए।"
        )
        
        try:
            # AI से हिंदी में जवाब मांगना
            response = model.generate_content(f"{identity_prompt}\n\nमालिक का सवाल: {prompt}")
            reply = response.text
            
            # टाइपिंग इफेक्ट
            for i in range(len(reply)):
                msg_placeholder.markdown(reply[:i+1] + "▌")
                time.sleep(0.005)
            msg_placeholder.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
