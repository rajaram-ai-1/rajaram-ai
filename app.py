import streamlit as st
import requests
import json

# --- 1. अपनी मास्टर चाबी यहाँ डालें ---
OPENROUTER_API_KEY = "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"

# --- 2. दुनिया के सबसे भरोसेमंद 'फ्री' दिमाग ---
# मैंने यहाँ उन मॉडल्स को रखा है जो कभी मना नहीं करते
models_to_try = [
    "meta-llama/llama-3.1-8b-instruct:free",
    "google/gemini-flash-1.5-8b:free",
    "mistralai/mistral-7b-instruct:free",
    "qwen/qwen-2-7b-instruct:free"
]

def get_smart_response(user_input):
    for model in models_to_try:
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json"
                },
                data=json.dumps({
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "You are Rajaram AI. A loyal brother. Motivational and serious about studies."},
                        {"role": "user", "content": user_input}
                    ]
                }),
                timeout=15
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content'], model
            else:
                # यहाँ असली गड़बड़ पकड़ी जाएगी
                error_data = response.json()
                print(f"Model {model} failed: {error_data}")
                continue
        except Exception as e:
            continue
            
    return "भाई, लगता है चाबी में बैलेंस या सेटिंग की दिक्कत है। एक बार OpenRouter पर 'Free Models' चेक करें।", "Error"

# --- 3. आपकी डायरी वाला सुंदर इंटरफ़ेस ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")

st.markdown("""
    <style>
    .stApp { background-color: white; color: black; }
    .chat-user { background-color: #f0f2f6; padding: 15px; border-radius: 20px 20px 0px 20px; text-align: right; color: black; margin-bottom: 10px; border: 1px solid #ddd; }
    .chat-ai { background-color: white; padding: 15px; border-radius: 20px 20px 20px 0px; text-align: left; color: black; margin-bottom: 10px; border: 1px solid #eee; box-shadow: 2px 2px 8px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# हेडर (राजा का मुकुट)
st.markdown("<h1 style='text-align: center;'>👑</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Rajaram AI</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: #555;'>'राजाराम AI आपकी हर प्रकार से मदद करेगी और हमेशा आपके साथ है'</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# चैट दिखाना
for msg in st.session_state.messages:
    style = "chat-user" if msg["role"] == "user" else "chat-ai"
    st.markdown(f"<div class='{style}'>{msg['content']}</div>", unsafe_allow_html=True)

prompt = st.chat_input("भाई से कुछ भी पूछो...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"<div class='chat-user'>{prompt}</div>", unsafe_allow_html=True)

    with st.spinner("राजाराम AI खाली दिमाग ढूंढ रहा है..."):
        answer, used_model = get_smart_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.markdown(f"<div class='chat-ai'>{answer}<br><small style='color:gray;'>दिमाग: {used_model}</small></div>", unsafe_allow_html=True)
