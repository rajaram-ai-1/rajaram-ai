import streamlit as st
import google.generativeai as genai

# --- 1. अपनी गूगल मास्टर चाबी यहाँ डालें ---
GOOGLE_API_KEY = "AIzaSyCEaasqfKx3uMBIReMj4FuQyk-OWxpW99Y"
genai.configure(api_key=GOOGLE_API_KEY)

# --- 2. दिमागों की महा-सूची (सही नामों के साथ) ---
# हमने यहाँ 'models/' हटा दिया है क्योंकि लाइब्रेरी इसे खुद जोड़ लेती है
brain_army = [
    'gemini-1.5-flash', 
    'gemini-1.5-pro',
    'gemini-1.0-pro'
]

def get_super_response(user_input):
    for brain_id in brain_army:
        try:
            # यहाँ हमने GenerativeModel के अंदर सीधा नाम भेजा है
            model = genai.GenerativeModel(brain_id)
            
            # आपकी डायरी के निर्देश
            context = "You are Rajaram AI. A loyal brother. Talk in Hindi. Be motivational. Help with studies."
            
            # जवाब मांगने का तरीका बदला गया है
            response = model.generate_content(f"{context} \n User: {user_input}")
            
            if response and response.text:
                return response.text, brain_id
                
        except Exception as e:
            # अगर एरर आए तो उसे यहाँ दिखाओ
            st.warning(f"ID {brain_id} में दिक्कत: {str(e)}")
            continue
            
    return "भाई, लगता है चाबी को एक बार फिर से जनरेट करना पड़ेगा।", "None"

# --- 3. आपका सुन्दर इंटरफ़ेस ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")
st.markdown("<h1 style='text-align:center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)

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
        with st.spinner("राजाराम AI का दिमाग चल रहा है..."):
            answer, used_id = get_super_response(prompt)
            st.write(answer)
            st.caption(f"कामयाब ID: {used_id}")
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.write("➕ ❤️ 📷 🎥")
