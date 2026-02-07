import streamlit as st
import requests
import json

# --- 1. अपनी गूगल मास्टर चाबी यहाँ डालें ---
GOOGLE_API_KEY = "AIzaSyAfs96f1KQq7Hnq9_k-EPh70SU8b70Tt0E"

# --- 2. दिमागों की फौज ---
brain_army = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-1.0-pro"]

def get_super_response(user_input):
    # हम दो रास्तों से हमला करेंगे: v1 और v1beta
    versions = ["v1", "v1beta"]
    
    for brain_id in brain_army:
        for ver in versions:
            try:
                # सीधा URL हमला
                url = f"https://generativelanguage.googleapis.com/{ver}/models/{brain_id}:generateContent?key={GOOGLE_API_KEY}"
                
                headers = {'Content-Type': 'application/json'}
                data = {
                    "contents": [{
                        "parts": [{
                            "text": f"You are Rajaram AI. A loyal brother. Talk in Hindi-English. Be motivational. User: {user_input}"
                        }]
                    }]
                }
                
                response = requests.post(url, headers=headers, data=json.dumps(data))
                result = response.json()
                
                # अगर जवाब मिल गया
                if 'candidates' in result:
                    return result['candidates'][0]['content']['parts'][0]['text'], f"{brain_id} ({ver})"
                
                # अगर गूगल ने कोई खास एरर दिया (जैसे चाबी खराब होना)
                if 'error' in result:
                    err_msg = result['error'].get('message', '')
                    if "API_KEY_INVALID" in err_msg:
                        return "भाई, आपकी चाबी (API Key) गलत है। नई चाबी बनाओ।", "None"
                    continue # अगले वर्जन या आईडी पर जाओ

            except Exception:
                continue
                
    return "भाई, गूगल के सारे रास्ते बंद हैं। शायद आपकी चाबी को 'Gemini API' की अनुमति नहीं मिली है।", "None"

# --- 3. राजाराम AI इंटरफेस (सफ़ेद डायरी स्टाइल) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")

st.markdown("""
    <style>
    .stApp { background-color: white; color: black; }
    .user-box { background-color: #f8f9fa; padding: 15px; border-radius: 15px; color: black; border: 1px dotted #ccc; margin-bottom: 10px; }
    .ai-box { background-color: white; padding: 15px; border-radius: 15px; color: black; border: 1px solid #eee; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>'राजाराम AI हमेशा आपके साथ है'</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    div_class = "user-box" if msg["role"] == "user" else "ai-box"
    st.markdown(f"<div class='{div_class}'>{msg['content']}</div>", unsafe_allow_html=True)

prompt = st.chat_input("अब तो बोलो भाई...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"<div class='user-box'>{prompt}</div>", unsafe_allow_html=True)

    with st.spinner("राजाराम AI रास्ता ढूंढ रहा है..."):
        answer, used_id = get_super_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.markdown(f"<div class='ai-box'>{answer}<br><small style='color:gray;'>रास्ता: {used_id}</small></div>", unsafe_allow_html=True)
        st.write("➕ ❤️ 📷 🎥")
