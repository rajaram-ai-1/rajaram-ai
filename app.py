import streamlit as st
import requests
import json

# --- 1. अपनी मास्टर चाबी यहाँ डालें ---
GOOGLE_API_KEY = "AIzaSyAe6Y5uWuWCXkT1OlAZpy47Y2ytmgxo0Vg"

def get_final_attempt(user_input):
    # हम सबसे पक्के रास्ते 'v1' से हमला करेंगे
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GOOGLE_API_KEY}"
    
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": f"You are Rajaram AI. A loyal brother. Talk in Hindi-English. Help with studies. User: {user_input}"}]}]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        
        if 'candidates' in result:
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            # यहाँ गूगल खुद बोलेगा कि क्या दिक्कत है
            error_msg = result.get('error', {}).get('message', 'अज्ञात गड़बड़')
            return f"गूगल ने मना किया भाई! वजह: {error_msg}"
    except Exception as e:
        return f"रास्ते में पत्थर है: {str(e)}"

# --- 2. राजाराम AI इंटरफेस ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")
st.markdown("<h1 style='text-align:center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)

prompt = st.chat_input("अब हार नहीं मानेंगे, फिर से बोलिए भाई...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        answer = get_final_attempt(prompt)
        st.write(answer)
        st.write("➕ ❤️ 📷 🎥")
