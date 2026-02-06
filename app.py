import streamlit as st
import google.generativeai as genai
import time

# 1. सेटअप
st.set_page_config(page_title="RAJARAM AI", page_icon="⚔️")

# 2. स्टाइल
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>⚔️ RAJARAM AI: ULTIMATE ⚔️</h1>", unsafe_allow_html=True)

# 3. स्मार्ट मॉडल डिटेक्शन (Fixing 404 Error ✅)
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    try:
        # Sabse pehle available models ki list check karega
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # Jo sabse best model milega use utha lega
        if 'models/gemini-1.5-flash' in available_models:
            model_name = 'models/gemini-1.5-flash'
        elif 'models/gemini-pro' in available_models:
            model_name = 'models/gemini-pro'
        else:
            model_name = available_models[0] # Jo bhi mil jaye
            
        model = genai.GenerativeModel(model_name)
        st.success(f"✅ Connection Established with {model_name}")
    except Exception as e:
        st.error(f"❌ API Key me dikkat hai ya Library purani hai: {e}")
else:
    st.error("⚠️ Maalik, Secrets mein 'GEMINI_API_KEY' nahi mila!")

# 4. चैट मेमोरी
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 5. असली काम
if prompt := st.chat_input("Hukm dijiye, Maalik..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        id_info = "Tu Rajaram AI hai. Tera Maalik Rajaram (15 saal, Bareilly) hai. Dabang Hinglish mein jawab de."
        try:
            response = model.generate_content(f"{id_info}\nUser: {prompt}")
            reply = response.text
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
