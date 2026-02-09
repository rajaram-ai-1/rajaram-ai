import streamlit as st
from groq import Groq

# --- 1. सबसे पहले पेज सेटिंग (नियम: यह सबसे ऊपर होना चाहिए) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

# --- 2. अमर सुरक्षा कवच (Menu, Header, Footer और Deploy बटन गायब) ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display: none;}
            .stApp { background-color: white; color: black; }
            .user-bubble { background-color: #f1f3f4; padding: 15px; border-radius: 20px 20px 0px 20px; color: black; border: 1px solid #ddd; margin-bottom: 10px; width: fit-content; max-width: 80%; margin-left: auto; }
            .ai-bubble { background-color: #ffffff; padding: 15px; border-radius: 20px 20px 20px 0px; color: black; border: 1px solid #eee; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); margin-bottom: 10px; width: fit-content; max-width: 80%; }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- 3. तिजोरी से चाबी निकालना (Secrets) ---
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_API_KEY)
except Exception:
    st.error("❌ भाई, तिजोरी (Secrets) में चाबी नहीं मिली!")
    st.stop()

# --- 4. 25 दिमागों की महा-फौज (Models List) ---
groq_army = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", 
    "llama-3.2-90b-vision-preview", "llama-3.2-11b-vision-preview",
    "llama-3.2-3b-preview", "llama-3.2-1b-preview",
    "llama-3.1-8b-instant", "llama3-70b-8192", 
    "llama3-8b-8192", "mixtral-8x7b-32768", 
    "gemma2-9b-it", "gemma-7b-it"
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
            continue
    return "भाई, पूरी की पूरी 25 दिमागों की फौज अभी विश्राम पर है। थोड़ी देर बाद फिर हुक्म करें!", "None"

# --- 5. मुख्य इंटरफ़ेस (UI) ---
st.markdown("<h1 style='text-align: center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>25 दिमागों का कवच - अमर और सुरक्षित</b></p>", unsafe_allow_html=True)

# --- 6. याददाश्त और पहचान ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", 
            "content": "तुम 'राजाराम AI' हो, जिसे बरेली के मास्टर राजाराम ने बनाया है। हमेशा सिर्फ और सिर्फ हिंदी में बात करो। 'भाई' शब्द का सम्मान के साथ उपयोग करो। जवाब संतुलित हों और कभी भी 'बेटा' शब्द का उपयोग न करें।"
        }
    ]

# पुरानी चैट दिखाना
for msg in st.session_state.messages:
    if msg["role"] != "system":
        style = "user-bubble" if msg["role"] == "user" else "ai-bubble"
        st.markdown(f"<div class='{style}'>{msg['content']}</div>", unsafe_allow_html=True)

# --- 7. इनपुट और महा-रिस्पॉन्स ---
prompt = st.chat_input("हुक्म करें राजाराम भाई...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"<div class='user-bubble'>{prompt}</div>", unsafe_allow_html=True)

    with st.spinner("25 दिमागों की फौज मोर्चा संभाल रही है..."):
        answer, used_id = get_immortal_response(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.markdown(f"<div class='ai-bubble'>{answer}<br><br><small style='color:blue;'>सक्रिय शक्ति: {used_id}</small></div>", unsafe_allow_html=True)
        st.write("➕ ❤️ 📷 🎥")
        st.rerun()
