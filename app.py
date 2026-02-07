import streamlit as st
from groq import Groq
import google.generativeai as genai
from PIL import Image

# --- 1. सुरक्षा कवच (Secrets से चाबियाँ उठाना) ---
try:
    GROQ_KEY = st.secrets["GROQ_API_KEY"]
    GEMINI_KEY = st.secrets["GOOGLE_API_KEY"]
    
    client_groq = Groq(api_key=GROQ_KEY)
    genai.configure(api_key=GEMINI_KEY)
except Exception:
    st.error("❌ भाई, Secrets में चाबियाँ नहीं मिलीं! कृपया Settings चेक करें।")
    st.stop()

# --- 2. अमर एआई दिमाग (Vision + 20 Brains Logic) ---
def get_ai_response(text, file):
    if file:
        try:
            # 'models/' जोड़ना जरूरी है ताकि 'NotFound' एरर न आए
            model = genai.GenerativeModel('models/gemini-1.5-flash')
            img = Image.open(file)
            # फोटो के साथ टेक्स्ट भेजना
            res = model.generate_content([text if text else "इस फोटो को विस्तार से समझाओ भाई", img])
            return res.text, "Gemini Vision 📷"
        except Exception as e:
            return f"गूगल अभी फोटो नहीं देख पा रहा भाई। एरर: {str(e)}", "Error"
    else:
        # 20 दिमागों वाली Groq की फौज
        army = ["llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "mixtral-8x7b-32768", "gemma2-9b-it"]
        for brain in army:
            try:
                res = client_groq.chat.completions.create(
                    model=brain,
                    messages=[
                        {"role": "system", "content": "You are Rajaram AI. A loyal brother and motivator. Answer in Hindi mixed with English. Always call the user 'Bhai'."},
                        {"role": "user", "content": text}
                    ],
                    temperature=0.6,
                )
                return res.choices[0].message.content, brain
            except:
                continue # अगले दिमाग पर जाओ
    return "भाई, अभी सारे नेटवर्क जाम हैं। थोड़ी देर में कोशिश करो।", "None"

# --- 3. इंटरफ़ेस (Gemini 3 + Rajaram Style) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

# डार्क और क्लीन लुक के लिए CSS
st.markdown("""
    <style>
    .stApp { background-color: #131314; color: #e3e3e3; }
    .stChatInputContainer { padding-bottom: 20px; }
    .chat-bubble { padding: 15px; border-radius: 15px; margin-bottom: 20px; border: 1px solid #3c3f43; line-height: 1.6; }
    .user-msg { background-color: #2b2d31; color: white; margin-left: auto; width: fit-content; max-width: 85%; }
    .ai-msg { background-color: transparent; border: none; width: 100%; }
    .tools-hint { display: flex; justify-content: space-around; font-size: 14px; color: #8e9196; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)

# याददाश्त (Chat History)
if "messages" not in st.session_state:
    st.session_state.messages = []

# बटन वाली पट्टी (Tools)
with st.expander("➕ Tools (यहाँ फोटो अपलोड करें)"):
    up_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")
    if up_file:
        st.image(up_file, width=250, caption="फोटो तैयार है भाई!")

# पुरानी चैट दिखाना
for m in st.session_state.messages:
    role_class = "user-msg" if m["role"] == "user" else "ai-msg"
    st.markdown(f"<div class='chat-bubble {role_class}'>{m['content']}</div>", unsafe_allow_html=True)

# इनपुट बॉक्स (Ask Rajaram AI...)
prompt = st.chat_input("Ask Rajaram AI...")

if prompt or up_file:
    # 1. यूजर का मैसेज दिखाओ
    user_text = prompt if prompt else "फोटो देखो भाई"
    st.session_state.messages.append({"role": "user", "content": user_text})
    st.markdown(f"<div class='chat-bubble user-msg'>{user_text}</div>", unsafe_allow_html=True)

    # 2. AI से जवाब मांगो
    with st.spinner("राजाराम AI मोर्चा संभाल रहा है..."):
        answer, brain_used = get_ai_response(user_text, up_file)
        
        # 3. AI का जवाब सेव करो और दिखाओ
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.markdown(f"<div class='chat-bubble ai-msg'>{answer}<br><br><small style='color:#8e9196;'>शक्ति: {brain_used}</small></div>", unsafe_allow_html=True)
        
        # नीचे के संकेत
        st.write("➕ ❤️ 📷 🎥 🎤")
        st.rerun()

# फूटर संकेत
st.markdown("<div class='tools-hint'><span>➕ Tools</span><span>⚡ Fast</span><span>🎤 Voice</span></div>", unsafe_allow_html=True)
