import streamlit as st
import google.generativeai as genai
import time

# 1. मिशन सेटअप
st.set_page_config(page_title="RAJARAM AI: SMART", page_icon="⚔️", layout="wide")

# 2. राजाराम भाई का स्टाइल
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .main-header { color: #ff4b4b; font-size: 40px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. गूगल का सबसे बेस्ट दिमाग खुद ढूँढना (Dynamic Selection ✅)
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    try:
        # गूगल से पूछना कि कौन-कौन से मॉडल उपलब्ध हैं
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # ऑटो-सिलेक्शन लॉजिक
        if 'models/gemini-1.5-flash' in available_models:
            selected_model = 'models/gemini-1.5-flash'
        elif 'models/gemini-1.5-pro' in available_models:
            selected_model = 'models/gemini-1.5-pro'
        elif 'models/gemini-pro' in available_models:
            selected_model = 'models/gemini-pro'
        else:
            # अगर ऊपर वाले नहीं मिले, तो जो भी पहला मॉडल हो उसे उठा लो
            selected_model = available_models[0]
            
        model = genai.GenerativeModel(selected_model)
        st.toast(f"सफलता! {selected_model} एक्टिव है।", icon="✅")
    except Exception as e:
        st.error(f"दिमाग ढूँढने में दिक्कत: {e}")
else:
    st.error("⚠️ मालिक, Secrets में 'GEMINI_API_KEY' डालना न भूलें!")

st.markdown("<div class='main-header'>⚔️ राजाराम AI: हिंदी मोड ⚔️</div>", unsafe_allow_html=True)

# 4. चैट मेमोरी
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 5. बातचीत (शुद्ध हिंदी निर्देश)
if prompt := st.chat_input("हुक्म कीजिये मालिक..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        
        # हिंदी पहचान
        identity = (
            "आपका नाम RAJARAM AI है। आपके मालिक राजाराम (बरेली वाले) हैं। "
            "सिर्फ हिंदी भाषा और देवनागरी लिपि का प्रयोग करें। "
            "मालिक को सम्मान दें।"
        )
        
        try:
            response = model.generate_content(f"{identity}\n\nमालिक: {prompt}")
            reply = response.text
            
            # टाइपिंग इफेक्ट
            for i in range(len(reply)):
                msg_placeholder.markdown(reply[:i+1] + "▌")
                time.sleep(0.005)
            msg_placeholder.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"मालिक, जवाब देने में दिक्कत आई: {e}")
