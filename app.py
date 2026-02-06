import streamlit as st
import google.generativeai as genai
import time

# 1. राजाराम भाई का मिशन कंट्रोल
st.set_page_config(page_title="RAJARAM AI", page_icon="⚔️", layout="wide")

# 2. दबंग स्टाइल (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .main-header { color: #ff4b4b; font-size: 42px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. गूगल का दिमाग सेट करना (Fixing the 404 Error ✅)
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # यहाँ बदलाव किया है: 'gemini-pro' इस्तेमाल कर रहे हैं जो हर जगह चलता है
    try:
        model = genai.GenerativeModel('gemini-pro')
    except:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
else:
    st.error("⚠️ Maalik, Secrets mein 'GEMINI_API_KEY' nahi mila!")
    API_KEY = None

st.markdown("<div class='main-header'>⚔️ RAJARAM AI: CORE ACTIVE</div>", unsafe_allow_html=True)

# 4. चैट मेमोरी
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. बातचीत और पहचान
if prompt := st.chat_input("Hukm dijiye, Maalik..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        
        identity = (
            "Tu RAJARAM AI hai. Tera maalik RAJARAM hai (15 saal, Bareilly, Class 10). "
            "Tu hamesha use 'Maalik' kahega aur Hinglish mein jawab dega."
        )
        
        if API_KEY:
            try:
                # नया तरीका जवाब मांगने का
                response = model.generate_content(f"{identity}\n\nUser: {prompt}")
                ai_reply = response.text
            except Exception as e:
                ai_reply = f"Maalik, abhi bhi dikat hai: {str(e)}"
        else:
            ai_reply = "Maalik, Chabi missing hai!"

        # टाइपिंग इफेक्ट
        for i in range(len(ai_reply)):
            msg_placeholder.markdown(ai_reply[:i+1] + "▌")
            time.sleep(0.005)
        msg_placeholder.markdown(ai_reply)
    
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
