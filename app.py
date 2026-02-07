import streamlit as st
import google.generativeai as genai
from google.api_core import client_options

# --- 1. अपनी गूगल मास्टर चाबी यहाँ डालें ---
GOOGLE_API_KEY = "AIzaSyAfs96f1KQq7Hnq9_k-EPh70SU8b70Tt0E"

# यहाँ हम गूगल को 'v1' (Stable) रास्ते पर चलने के लिए मजबूर कर रहे हैं
options = client_options.ClientOptions(api_version='v1')
genai.configure(api_key=GOOGLE_API_KEY, client_options=options)

# --- 2. दिमागों की सही फौज (Stable IDs) ---
brain_army = [
    'gemini-1.5-flash', 
    'gemini-1.5-pro',
    'gemini-1.0-pro'
]

def get_super_response(user_input):
    for brain_id in brain_army:
        try:
            # मॉडल को सही तरीके से लोड करना
            model = genai.GenerativeModel(model_name=f"models/{brain_id}")
            
            # आपकी डायरी के निर्देश
            context = "You are Rajaram AI. A loyal brother. Talk in Hindi-English. Be motivational. Help with studies."
            
            # जवाब मांगना
            response = model.generate_content(f"{context} \n User: {user_input}")
            
            if response and response.text:
                return response.text, brain_id
                
        except Exception as e:
            # अगर एरर आए तो उसे साफ़ दिखाओ
            st.warning(f"ID {brain_id} चेक की गई: {str(e)}")
            continue
            
    return "भाई, गूगल का स्थिर (Stable) रास्ता भी काम नहीं कर रहा।", "None"

# --- 3. आपका सुन्दर इंटरफ़ेस ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")
st.markdown("<h1 style='text-align:center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>'राजाराम AI आपकी मदद के लिए हमेशा आपके साथ है'</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("अब बात करो भाई से...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("राजाराम AI दिमागों को जगा रहा है..."):
            answer, used_id = get_super_response(prompt)
            st.write(answer)
            st.caption(f"कामयाब ID: {used_id}")
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.write("➕ ❤️ 📷 🎥")
