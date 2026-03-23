import streamlit as st
import os, base64, asyncio, time
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from gtts import gTTS
from PIL import Image
import google.generativeai as genai

# 🔱 [PHASE 1: ROYAL UI SETUP]
st.set_page_config(page_title="RAJA AI 👑", page_icon="👑", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #050505 !important; color: #FFD700 !important;
    }
    
    /* Header Style */
    .raja-header {
        font-family: 'Cinzel', serif; font-size: 50px; text-align: center;
        color: #FFD700; text-shadow: 0 0 15px #FFD700; padding: 20px;
    }

    /* Gemini Style Chat Bubbles */
    .stChatMessage { border-radius: 20px; border: 1px solid #333; margin-bottom: 10px; }
    
    /* Global Map Styling */
    .map-container {
        border: 2px solid #FFD700; border-radius: 15px; overflow: hidden;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.2);
    }
    </style>
    <div class="raja-header">👑 RAJA AI 👑</div>
""", unsafe_allow_html=True)

# 🔱 [PHASE 2: THE BRAIN & SENSES]
class RajaCore:
    def __init__(self):
        self.K = {
            "G": st.secrets.get("GROQ_API_KEY"),
            "GM": st.secrets.get("GEMINI_KEY")
        }
        if self.K["GM"]: genai.configure(api_key=self.K["GM"])
        
    def speak(self, text):
        tts = gTTS(text=text[:300], lang='hi')
        tts.save("v.mp3")
        with open("v.mp3", "rb") as f:
            data = base64.b64encode(f.read()).decode()
        st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{data}">', unsafe_allow_html=True)

raja = RajaCore()

# 🔱 [PHASE 3: GLOBAL INTELLIGENCE DISPLAY]
st.markdown("<div class='map-container'>", unsafe_allow_html=True)
# यहाँ एक एनिमेटेड ग्लोबल मैप का विजुअल (iframe या image)
st.image("https://www.nasa.gov/sites/default/files/styles/full_width/public/thumbnails/image/earth_night.jpg", caption="GLOBAL INTELLIGENCE GRID : LIVE")
st.markdown("</div>", unsafe_allow_html=True)

# 🔱 [PHASE 4: CHAT HISTORY (GEMINI STYLE)]
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 🔱 [PHASE 5: INPUT SYSTEM (PHOTO + VIDEO + TEXT)]
# Gemini की तरह नीचे + बटन और इनपुट
col1, col2 = st.columns([1, 10])

with col1:
    uploaded_file = st.file_uploader(" ", type=['jpg', 'png', 'jpeg', 'mp4'], label_visibility="collapsed")
    st.markdown("### ➕") # यह विजुअल प्लस का निशान

query = st.chat_input("RAJA AI से कुछ भी पूछें...")

if query:
    # यूजर का मैसेज दिखाओ
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        final_response = ""
        
        # 1. Vision Logic (अगर फोटो है)
        if uploaded_file and uploaded_file.type.startswith('image'):
            img = Image.open(uploaded_file)
            st.image(img, width=300)
            model = genai.GenerativeModel("gemini-1.5-flash-latest")
            res = model.generate_content([query if query else "इस फोटो को देखें", img])
            final_response = res.text
            
        # 2. Video Logic (अगर वीडियो है)
        elif uploaded_file and uploaded_file.type.startswith('video'):
            st.video(uploaded_file)
            final_response = "🔱 राजाराम भाई, मैंने आपका वीडियो लोड कर लिया है। यह बहुत शानदार है!"

        # 3. Photo/Video Generation (अगर यूजर बनाने को कहे)
        elif any(word in query.lower() for word in ["बनाओ", "create", "generate"]):
            clean_q = query.replace(" ", "%20")
            img_url = f"https://image.pollinations.ai/prompt/{clean_q}?model=flux&nologo=true"
            st.image(img_url)
            final_response = "🔱 आपके हुक्म पर यह दृश्य तैयार किया गया है, मेरे राजा!"

        # 4. Supreme Reasoning (Llama 405B)
        else:
            llm = ChatGroq(groq_api_key=raja.K["G"], model_name="llama-3.1-405b-reasoning")
            res = llm.invoke([SystemMessage(content="You are RAJA AI, created by Rajaram. Speak like a Royal High-Tech King.")] + 
                             [HumanMessage(content=query)])
            final_response = res.content

        st.markdown(final_response)
        st.session_state.messages.append({"role": "assistant", "content": final_response})
        
        # फेस टू फेस लाइव बात (आवाज़)
        raja.speak(final_response)

# 🔱 [PHASE 6: FACE-TO-FACE (LIVE CAMERA)]
if st.checkbox("🎥 START FACE-TO-FACE SESSION"):
    st.camera_input("RAJA AI IS WATCHING YOU...")
    st.write("Master Rajaram, I am looking at you. System operational.")
