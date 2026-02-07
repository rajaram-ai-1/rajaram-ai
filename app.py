import streamlit as st
import requests
import json

# --- 1. आपकी मास्टर चाबी (यहाँ अपनी OpenRouter Key डालें) ---
OPENROUTER_API_KEY = "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"

# --- 2. वेबसाइट की सजावट (आपकी डायरी के हिसाब से: सफ़ेद थीम, काली स्याही) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

st.markdown("""
    <style>
    /* सफ़ेद थीम और काली स्याही */
    .stApp { background-color: #ffffff; color: #000000; }
    
    /* चैट बॉक्स का स्टाइल (आपकी तरह सुंदर) */
    .chat-bubble-user { 
        background-color: #f0f2f6; 
        padding: 15px; 
        border-radius: 20px 20px 0px 20px; 
        text-align: right; 
        margin: 10px; 
        color: black; 
        border: 1px solid #e0e0e0;
        float: right;
        width: 80%;
    }
    .chat-bubble-ai { 
        background-color: #ffffff; 
        padding: 15px; 
        border-radius: 20px 20px 20px 0px; 
        text-align: left; 
        margin: 10px; 
        color: black; 
        border: 1px solid #eeeeee; 
        box-shadow: 2px 4px 10px rgba(0,0,0,0.05);
        float: left;
        width: 80%;
    }
    
    /* मुकुट और हेडर */
    .crown { font-size: 50px; text-align: center; margin-bottom: 0px; }
    .title { text-align: center; font-weight: bold; font-size: 32px; margin-top: -10px; }
    .subtitle { text-align: center; font-style: italic; color: #555; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ऊपर का हिस्सा (मुकुट और राजाराम संदेश) ---
st.markdown("<div class='crown'>👑</div>", unsafe_allow_html=True)
st.markdown("<div class='title'>Rajaram AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>'राजाराम AI आपकी हर प्रकार से मदद करेगी और Rajaram AI आपकी मदद के लिए हमेशा आपके साथ है'</div>", unsafe_allow_html=True)

# --- 4. साइडबार (चैट मेमोरी और गूगल साइन-इन संदेश) ---
with st.sidebar:
    st.markdown("### ≡ राजाराम AI मेनू")
    if st.button("चैट मेमोरी साफ़ करें"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.info("📢 संदेश: फोटो और वीडियो बनाने जैसी उच्च सुविधाओं के लिए जल्द ही 'Sign in with Google' आने वाला है।")

# --- 5. ओपन-राउटर का जादुई दिमाग ---
def get_ai_response(user_input):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "google/gemini-flash-1.5", # आप यहाँ 'meta-llama/llama-3-8b-instruct' भी कर सकते हैं
                "messages": [
                    {"role": "system", "content": "You are Rajaram AI, a loyal brother and friend. Talk in Hindi-English mix. Be motivational. Be very serious about studies. Help with all government jobs and courses information. Never give illegal advice."},
                    {"role": "user", "content": user_input}
                ]
            })
        )
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return "माफ़ करना भाई, अभी सर्वर में कुछ हलचल है। फिर से कोशिश करें।"
    except Exception as e:
        return f"त्रुटि: {str(e)}"

# --- 6. चैट का असली खेल ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# पुराने मैसेज दिखाना
for msg in st.session_state.messages:
    style = "chat-bubble-user" if msg["role"] == "user" else "chat-bubble-ai"
    st.markdown(f"<div class='{style}'>{msg['content']}</div><div style='clear: both;'></div>", unsafe_allow_html=True)

# यूजर इनपुट (चैट बॉक्स)
prompt = st.chat_input("Rajaram AI से पूछें (जैसे: पढ़ाई में मन कैसे लगाऊं भाई?)...")

if prompt:
    # यूजर का मैसेज सेव और डिस्प्ले करें
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"<div class='chat-bubble-user'>{prompt}</div><div style='clear: both;'></div>", unsafe_allow_html=True)

    # AI का जवाब लाएं
    with st.spinner("राजाराम AI सोच रहा है..."):
        answer = get_ai_response(prompt)
    
    # AI का जवाब सेव और डिस्प्ले करें
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.markdown(f"<div class='chat-bubble-ai'>{answer}</div><div style='clear: both;'></div>", unsafe_allow_html=True)
