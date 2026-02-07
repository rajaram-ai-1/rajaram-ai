import streamlit as st
import google.generativeai as genai

# --- 1. अपनी गूगल मास्टर चाबी यहाँ डालें ---
GOOGLE_API_KEY = "AIzaSyCEaasqfKx3uMBIReMj4FuQyk-OWxpW99Y"
genai.configure(api_key=GOOGLE_API_KEY)

# --- 2. दिमागों की लिस्ट ---
brain_army = [
    'gemini-1.5-flash', 
    'gemini-1.5-pro',
    'gemini-1.0-pro'
]

def get_empty_brain_response(user_input):
    for brain_id in brain_army:
        try:
            # सुरक्षा के साथ मॉडल लोड करना
            model = genai.GenerativeModel(model_name=brain_id)
            
            # आपकी डायरी के निर्देश
            context = "You are Rajaram AI. A loyal brother. Talk in Hindi. Be motivational."
            
            # यहाँ हम safety_settings को भी कंट्रोल कर रहे हैं ताकि कोई रुकावट न आए
            response = model.generate_content(
                f"{context} \n User: {user_input}",
                safety_settings=[
                    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                ]
            )
            
            if response.text:
                return response.text, brain_id
                
        except Exception as e:
            # राजाराम भाई, इस एरर को ध्यान से पढ़ना कि क्या लिखा आ रहा है!
            st.error(f"ID {brain_id} ने कहा: {str(e)}")
            continue
            
    return "भाई, गूगल के सर्वर में आपकी चाबी का रास्ता ब्लॉक है।", "None"

# --- 3. इंटरफ़ेस ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")
st.markdown("<h1 style='text-align:center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("यहाँ लिखें...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("राजाराम AI कोशिश कर रहा है..."):
            answer, used_id = get_empty_brain_response(prompt)
            st.write(answer)
            st.caption(f"ID: {used_id}")
            st.session_state.messages.append({"role": "assistant", "content": answer})
