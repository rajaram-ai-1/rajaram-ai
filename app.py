import streamlit as st
from groq import Groq

# --- 1. सुरक्षा कवच (Secrets) ---
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    st.error("❌ भाई, तिजोरी (Secrets) में चाबी नहीं मिली!")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

# --- 2. 20-25 दिमागों की महा-फौज (Full Army List) ---
# हमने Groq के सभी मुख्य और बैकअप मॉडल्स जोड़ दिए हैं
groq_army = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", 
    "llama-3.2-90b-vision-preview", "llama-3.2-11b-vision-preview",
    "llama-3.2-3b-preview", "llama-3.2-1b-preview",
    "llama-3.1-8b-instant", "llama3-70b-8192", 
    "llama3-8b-8192", "mixtral-8x7b-32768", 
    "gemma2-9b-it", "gemma-7b-it",
    "llama-guard-3-8b", "distil-whisper-large-v3-en"
    # नोट: Groq पर उपलब्ध मॉडल्स समय-समय पर अपडेट होते रहते हैं, 
    # यह लिस्ट उन सभी को कवर करने की कोशिश करती है।
]

def get_immortal_response(messages_history):
    """पूरी फौज में से किसी एक से जवाब लाने की कोशिश"""
    for brain in groq_army:
        try:
            completion = client.chat.completions.create(
                model=brain,
                messages=messages_history,
                temperature=0.8,
                max_tokens=2048,
            )
            return completion.choices[0].message.content, brain
        except Exception:
            # अगर ये दिमाग काम नहीं कर रहा, तो चुपचाप अगले पर जाओ
            continue
            
    return "भाई, पूरी की पूरी 25 दिमागों की फौज अभी विश्राम पर है। 2 मिनट बाद फिर हुक्म करें!", "None"

# --- 3. इंटरफ़ेस सेटअप ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: white; color: black; }
    .user-bubble { background-color: #f1f3f4; padding: 15px; border-radius: 20px 20px 0px 20px; color: black; border: 1px solid #ddd; margin-bottom: 10px; width: fit-content; max-width: 80%; margin-left: auto; }
    .ai-bubble { background-color: #ffffff; padding: 15px; border-radius: 20px 20px 20px 0px; color: black; border: 1px solid #eee; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); margin-bottom: 10px; width: fit-content; max-width: 80%; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>25 दिमागों का कवच - अमर और सुरक्षित</b></p>", unsafe_allow_html=True)

# --- 4. याददाश्त और पहचान ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", 
            "content": "तुम 'राजाराम AI' हो, जिसे बरेली के मास्टर राजाराम ने बनाया है। हमेशा सिर्फ और सिर्फ हिंदी में बात करो। 'भाई' शब्द को हमेशा सही तरीके से लिखो। जवाब न बहुत लंबे हों और न बहुत छोटे, बिल्कुल संतुलित होने चाहिए। हर सवाल का सीधा और दोस्ताना जवाब दो। कभी भी 'बेटा' शब्द का इस्तेमाल मत करना और हमेशा सम्मान के साथ 'भाई' कहना।"
            
        }
    ]

# पुरानी चैट दिखाना
for msg in st.session_state.messages:
    if msg["role"] != "system":
        style = "user-bubble" if msg["role"] == "user" else "ai-bubble"
        st.markdown(f"<div class='{style}'>{msg['content']}</div>", unsafe_allow_html=True)

# --- 5. इनपुट और महा-रिस्पॉन्स ---
prompt = st.chat_input("हुक्म करें राजाराम भाई...")

if prompt:
    # यूजर का मैसेज याददाश्त में जोड़ो
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"<div class='user-bubble'>{prompt}</div>", unsafe_allow_html=True)

    with st.spinner("25 दिमागों की फौज मोर्चा संभाल रही है..."):
        # पूरी हिस्ट्री के साथ जवाब लाओ
        answer, used_id = get_immortal_response(st.session_state.messages)
        
        # AI का मैसेज याददाश्त में जोड़ो
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.markdown(f"<div class='ai-bubble'>{answer}<br><br><small style='color:blue;'>सक्रिय शक्ति: {used_id}</small></div>", unsafe_allow_html=True)
        
        st.write("➕ ❤️ 📷 🎥")
        # पेज रिफ्रेश ताकि मेमोरी सेट रहे
        st.rerun()
