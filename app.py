import streamlit as st
from groq import Groq

# --- 1. सुरक्षा कवच (Secrets से चाबी उठाना) ---
try:
    # Streamlit की Settings -> Secrets में GROQ_API_KEY = "आपकी_चाबी" होना चाहिए
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    st.error("❌ भाई, तिजोरी (Secrets) में चाबी नहीं मिली! उसे Settings में जाकर भरें।")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

# --- 2. 20+ दिमागों की अमर फौज (Fallback Army) ---
groq_army = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", 
    "llama-3.1-8b-instant", "llama3-70b-8192", 
    "llama3-8b-8192", "mixtral-8x7b-32768", 
    "gemma2-9b-it", "gemma-7b-it"
]

def get_immortal_response(user_input):
    """यह फंक्शन हर दिमाग को तब तक आज़माएगा जब तक जवाब न मिल जाए"""
    for brain in groq_army:
        try:
            completion = client.chat.completions.create(
                model=brain,
                messages=[
                    {"role": "system", "content": "You are Rajaram AI. A loyal brother. Motivational. Focus on studies/jobs. Talk in Hindi-English. Always call user 'Bhai'."},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.6,
                max_tokens=1024,
            )
            return completion.choices[0].message.content, brain
        except Exception:
            # अगर एक दिमाग थका है या एरर है, तो चुपचाप अगले पर बढ़ो
            continue
            
    return "भाई, पूरी फौज अभी विश्राम पर है। 2 मिनट बाद फिर कोशिश करें, मैं यहीं हूँ!", "None"

# --- 3. राजाराम AI इंटरफ़ेस (सफ़ेद डायरी थीम) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: white; color: black; }
    .user-bubble { background-color: #f1f3f4; padding: 15px; border-radius: 20px 20px 0px 20px; color: black; border: 1px solid #ddd; margin-bottom: 10px; width: fit-content; max-width: 80%; margin-left: auto; }
    .ai-bubble { background-color: #ffffff; padding: 15px; border-radius: 20px 20px 20px 0px; color: black; border: 1px solid #eee; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); margin-bottom: 10px; width: fit-content; max-width: 80%; }
    .stChatInput { border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>'20 दिमागों का कवच - अमर और सुरक्षित'</p>", unsafe_allow_html=True)

# याददाश्त (Chat History)
if "messages" not in st.session_state:
    st.session_state.messages = []

# पुरानी चैट दिखाना
for msg in st.session_state.messages:
    style = "user-bubble" if msg["role"] == "user" else "ai-bubble"
    st.markdown(f"<div class='{style}'>{msg['content']}</div>", unsafe_allow_html=True)

# इनपुट बॉक्स
prompt = st.chat_input("हुक्म करें भाई...")

if prompt:
    # यूजर का मैसेज दिखाओ
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"<div class='user-bubble'>{prompt}</div>", unsafe_allow_html=True)

    with st.spinner("राजाराम AI की फौज मोर्चा संभाल रही है..."):
        # अमर रिस्पॉन्स मांगना
        answer, used_id = get_immortal_response(prompt)
        
        # AI का मैसेज दिखाओ
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.markdown(f"<div class='ai-bubble'>{answer}<br><br><small style='color:blue;'>सक्रिय शक्ति: {used_id}</small></div>", unsafe_allow_html=True)
        
        # डायरी के बटन
        st.write("➕ ❤️ 📷 🎥")
