import streamlit as st
from groq import Groq

# 1. पेज सेटिंग (सबसे ऊपर)
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

# --- राजाराम भाई का 'दिमाग' चुनने वाला इंजन (नया जोड़ा गया) ---
def select_best_brain(messages_history):
    user_input = messages_history[-1]["content"].lower()
    if any(word in user_input for word in ["padhai", "maths", "science", "exam", "book", "class", "study"]):
        return "llama-3.3-70b-versatile", "📖 पढ़ाई वाला दिमाग (Llama 70B)"
    elif any(word in user_input for word in ["majak", "joke", "funny", "hi", "hello", "kaise ho"]):
        return "llama-3.1-8b-instant", "😂 चुलबुला दिमाग (Llama 8B)"
    else:
        return "llama-3.1-70b-versatile", "🧠 ज्ञानी दिमाग (Mixtral)"

# 2. सुरक्षा कवच (स्टाइलिंग)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display:none !important;}
    div[data-testid="stStatusWidget"] {display:none !important;}
    button[title="Manage app"] {display: none !important;}
    .viewerBadge_container__1QS13 {display: none !important;}
    </style>
    """, unsafe_allow_html=True)

# 3. तिजोरी से चाबी निकालना
try:
    if "GROQ_API_KEY" in st.secrets:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    else:
        st.error("❌ भाई, Secrets में 'GROQ_API_KEY' नहीं मिली!")
        st.stop()
except Exception as e:
    st.error(f"❌ कनेक्शन एरर: {e}")
    st.stop()

# 4. 25+ शक्तिशाली दिमागों की महा-फौज (आपकी लिस्ट सुरक्षित है)
groq_army = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", 
    "llama-3.2-90b-vision-preview", "llama-3.2-11b-vision-preview",
    "llama-3.2-3b-preview", "llama-3.2-1b-preview",
    "llama-3.1-8b-instant", "llama3-70b-8192", 
    "llama3-8b-8192", "mixtral-8x7b-32768", 
    "gemma2-9b-it", "gemma-7b-it",
    "llama-guard-3-8b", "distil-whisper-large-v3-en"
]

# 5. रिस्पॉन्स फंक्शन (इसे मैंने आपके पुराने कोड में फिट कर दिया है)
def get_response(messages_history):
    # स्मार्ट तरीके से दिमाग चुनना
    best_brain, brain_display_name = select_best_brain(messages_history)
    
    try:
        completion = client.chat.completions.create(
            model=best_brain,
            messages=messages_history,
            temperature=0.7,
            max_tokens=2048,
        )
        return completion.choices[0].message.content, brain_display_name
    except Exception as e:
        return f"माफ़ करना भाई, गड़बड़ हो गई: {e}", "Error"

# 6. दरबार की सजावट
st.markdown("<h1 style='text-align: center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>25+ महा-शक्तियों का कवच - सुरक्षित और तेज़</b></p>", unsafe_allow_html=True)

# 7. याददाश्त
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "तुम 'राजाराम AI' हो। और यह आपके लिए बरेली के राजाराम भाई ने बनाया है जो 15 साल के क्लास 10 के स्टूडेंट हैं, वे बहुत इंटेलिजेंट हैं। हमेशा हिंदी में बात करो और 'भाई' कहकर सम्मान दो।"}
    ]

# पुरानी चैट दिखाना
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# 8. हुक्म और जवाब
prompt = st.chat_input("हुक्म करें राजाराम भाई...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.spinner("फौज मोर्चा संभाल रही है..."):
        # यहाँ आपका 'answer' और 'used_id' सही से सेट हो गया है
        answer, used_id = get_response(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)
            st.caption(f"सक्रिय शक्ति: {used_id}")
        
        st.rerun()
