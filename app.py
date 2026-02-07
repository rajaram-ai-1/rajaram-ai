import streamlit as st
import requests
import json

# --- 1. अपनी मास्टर चाबी यहाँ डालें ---
GOOGLE_API_KEY = "AIzaSyAe6Y5uWuWCXkT1OlAZpy47Y2ytmgxo0Vg"

# --- 2. अमर सेना (20+ दिमागों की लिस्ट) ---
brain_army = [
    "gemini-1.5-flash", "gemini-1.5-pro", "gemini-1.5-flash-8b", 
    "gemini-1.0-pro", "gemini-pro", "gemini-1.5-flash-latest",
    "gemini-1.5-pro-latest", "gemini-1.0-pro-latest",
    "gemini-2.0-flash-exp", # भविष्य का दिमाग
]

def get_immortal_response(user_input):
    """यह फंक्शन कभी हार नहीं मानता"""
    for brain_id in brain_army:
        for ver in ["v1beta", "v1"]:
            try:
                url = f"https://generativelanguage.googleapis.com/{ver}/models/{brain_id}:generateContent?key={GOOGLE_API_KEY}"
                headers = {'Content-Type': 'application/json'}
                payload = {
                    "contents": [{"parts": [{"text": f"You are Rajaram AI. A loyal brother. Answer simply in Hindi. User: {user_input}"}]}],
                    "safetySettings": [{"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"}]
                }
                
                # सिर्फ 5 सेकंड का इंतज़ार, वरना अगले दिमाग पर कूदो
                response = requests.post(url, json=payload, headers=headers, timeout=5)
                
                if response.status_code == 200:
                    result = response.json()
                    if 'candidates' in result:
                        return result['candidates'][0]['content']['parts'][0]['text'], f"{brain_id} ({ver})"
            except:
                continue # चुपचाप अगले दिमाग पर चले जाओ, यूजर को पता भी नहीं चलेगा
                
    return "भाई, अभी सारे दिमाग ध्यान (Meditation) में हैं। एक बार फिर कोशिश करो, मैं यहीं हूँ।", "None"

# --- 3. इंटरफ़ेस (सफ़ेद थीम और अमर लुक) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")

# CSS: इसे और भी क्लीन बनाने के लिए
st.markdown("""
    <style>
    .stApp { background-color: white; color: black; }
    .chat-bubble { padding: 15px; border-radius: 15px; margin-bottom: 10px; border: 1px solid #eee; }
    .user { background-color: #f1f3f4; text-align: right; }
    .ai { background-color: #ffffff; box-shadow: 0px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# पुरानी चैट दिखाओ
for chat in st.session_state.chat_history:
    role_class = "user" if chat["role"] == "user" else "ai"
    st.markdown(f"<div class='chat-bubble {role_class}'>{chat['content']}</div>", unsafe_allow_html=True)

# इनपुट बॉक्स
user_query = st.chat_input("मुझसे बात करो भाई...")

if user_query:
    st.session_state.chat_history.append({"role": "user", "content": user_query})
    st.markdown(f<div class='chat-bubble user'>{user_query}</div>", unsafe_allow_html=True)
    
    with st.spinner("राजाराम AI आपकी सेवा में..."):
        # यहाँ 'अमर' फंक्शन कॉल हो रहा है
        reply, working_id = get_immortal_response(user_query)
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.markdown(f"<div class='chat-bubble ai'>{reply}<br><small style='color:gray;'>शक्ति: {working_id}</small></div>", unsafe_allow_html=True)
        st.write("➕ ❤️ 📷 🎥")
