import streamlit as st
import google.generativeai as genai

# --- 1. आपकी 6 'जादुई' चाबियाँ (Key Rotation) ---
all_keys = ["YOUR_KEY_1", "YOUR_KEY_2", "YOUR_KEY_3", "YOUR_KEY_4", "YOUR_KEY_5", "YOUR_KEY_6"]

# --- 2. सफ़ेद थीम और राजा वाला स्टाइल (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: white; color: black; }
    .chat-bubble-user { background-color: #f0f2f6; padding: 10px; border-radius: 15px; text-align: right; margin-bottom: 10px; }
    .chat-bubble-ai { background-color: #ffffff; border: 1px solid #ddd; padding: 10px; border-radius: 15px; text-align: left; margin-bottom: 10px; }
    .crown-header { text-align: center; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ऊपर का हिस्सा (मुकुट और संदेश) ---
st.markdown("<h1 class='crown-header'>👑</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Rajaram AI</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>'राजाराम AI आपकी हर प्रकार से मदद करेगी और हमेशा आपके साथ है'</p>", unsafe_allow_html=True)

# --- 4. चैट मेमोरी बटन (Sidebar) ---
with st.sidebar:
    st.button("≡ चैट मेमोरी")
    st.write("यहाँ आपकी पुरानी यादें सुरक्षित रहेंगी।")

# --- 5. मुख्य चैट लॉजिक ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# पुराने मैसेज दिखाना
for msg in st.session_state.messages:
    role_class = "chat-bubble-user" if msg["role"] == "user" else "chat-bubble-ai"
    st.markdown(f"<div class='{role_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# इनपुट बॉक्स (चैट बॉक्स)
prompt = st.chat_input("Rajaram AI से पूछें...")

if prompt:
    # यूजर का मैसेज दिखाओ
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"<div class='chat-bubble-user'>{prompt}</div>", unsafe_allow_html=True)

    # AI का जवाब (Key Rotation के साथ)
    response_text = ""
    for key in all_keys:
        try:
            genai.configure(api_key=key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            # आपकी डायरी के हिसाब से 'भावनात्मक और मोटिवेशनल' निर्देश
            res = model.generate_content(f"You are Rajaram AI. Talk like a brother or friend. Be motivational. Be serious about studies. System Instruction: {prompt}")
            response_text = res.text
            break
        except:
            continue
    
    if response_text:
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        st.markdown(f"<div class='chat-bubble-ai'>{response_text}</div>", unsafe_allow_html=True)
