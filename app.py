import streamlit as st
import requests
import json

# --- 1. अपनी गूगल मास्टर चाबी यहाँ डालें ---
GOOGLE_API_KEY = "AIzaSyAfs96f1KQq7Hnq9_k-EPh70SU8b70Tt0E"

# --- 2. दिमागों की फौज (Direct API Endpoints) ---
brain_army = [
    "gemini-1.5-flash",
    "gemini-1.5-pro",
    "gemini-1.0-pro"
]

def get_super_response(user_input):
    for brain_id in brain_army:
        try:
            # सीधा गूगल के सर्वर का पता
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{brain_id}:generateContent?key={GOOGLE_API_KEY}"
            
            headers = {'Content-Type': 'application/json'}
            
            # आपकी डायरी के निर्देश (System Instruction)
            data = {
                "contents": [{
                    "parts": [{
                        "text": f"You are Rajaram AI. A loyal brother. Talk in Hindi-English. Be motivational. Help with studies. User says: {user_input}"
                    }]
                }]
            }
            
            response = requests.post(url, headers=headers, data=json.dumps(data))
            result = response.json()
            
            # जवाब बाहर निकालना
            if 'candidates' in result:
                return result['candidates'][0]['content']['parts'][0]['text'], brain_id
            else:
                st.warning(f"ID {brain_id} ने मना किया: {result.get('error', {}).get('message', 'Unknown Error')}")
                continue
        except Exception as e:
            st.error(f"ID {brain_id} में दिक्कत: {str(e)}")
            continue
            
    return "भाई, लगता है चाबी या इंटरनेट में कोई बड़ी गड़बड़ है।", "None"

# --- 3. आपका सुन्दर इंटरफ़ेस (सफ़ेद थीम) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")

st.markdown("""
    <style>
    .stApp { background-color: white; color: black; }
    .user-box { background-color: #f1f3f4; padding: 15px; border-radius: 15px; margin-bottom: 10px; color: black; border: 1px solid #ddd; }
    .ai-box { background-color: #ffffff; padding: 15px; border-radius: 15px; margin-bottom: 10px; color: black; border: 1px solid #eee; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-style: italic;'>'राजाराम AI आपकी मदद के लिए हमेशा आपके साथ है'</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    style = "user-box" if msg["role"] == "user" else "ai-box"
    st.markdown(f"<div class='{style}'>{msg['content']}</div>", unsafe_allow_html=True)

prompt = st.chat_input("अब तो बात करो भाई से...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"<div class='user-box'>{prompt}</div>", unsafe_allow_html=True)

    with st.spinner("राजाराम AI सीधा गूगल से बात कर रहा है..."):
        answer, used_id = get_super_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.markdown(f"<div class='ai-box'>{answer}<br><small style='color:gray;'>कामयाब ID: {used_id}</small></div>", unsafe_allow_html=True)
        st.write("➕ ❤️ 📷 🎥")
