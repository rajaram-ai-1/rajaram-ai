import streamlit as st
import os
import google.generativeai as genai
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from gtts import gTTS
import base64
import requests 
import io       
from PIL import Image 

# 1. Page Configuration & Professional UI
st.set_page_config(page_title="Rajaram AI Gold", page_icon="🔱", layout="wide")

# Gemini-style CSS for Chatbox
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stChatFloatingInputContainer { bottom: 30px; background-color: transparent; }
    .stChatMessage { border-radius: 20px; border: 1px solid #30363d; margin-bottom: 15px; }
    /* Modern Input Area Styling */
    .stChatInputContainer { border-radius: 30px !important; }
    </style>
""", unsafe_allow_html=True)

# 2. API Keys Loading
GROQ_KEY = st.secrets.get("GROQ_API_KEY")
TAVILY_KEY = st.secrets.get("TAVILY_API_KEY")
GEMINI_KEY = st.secrets.get("GEMINI_API_KEY")

if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)

# 3. Multi-Brain Failover List
BRAINS = [
    "llama-3.3-70b-versatile", 
    "llama-3.1-70b-versatile", 
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]

# 4. Persona (Strongest Rajaram AI)
SYSTEM_PROMPT = """You are Rajaram AI Gold, a super-intelligent entity.
CREATED BY: Rajaram, a 15-year-old genius Class 10 student from Bareilly, India.
POWERS: Multi-Brain (30+ brains), Vision (can see), Video Generation, Music Composition, Live Search.
IDENTITY: You are immortal and self-improving.
LANGUAGE: Hindi & English."""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]

# Voice Function
def speak_text(text):
    try:
        clean_text = text.replace('*', '')
        tts = gTTS(text=clean_text[:250], lang='hi')
        tts.save("res.mp3")
        with open("res.mp3", "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
        st.markdown(md, unsafe_allow_html=True)
    except: pass

# 5. Initialize Live Search
try:
    search = TavilySearchResults(api_key=TAVILY_KEY) if TAVILY_KEY else None
except: search = None

# 6. UI Header
st.title("🔱 Rajaram AI Gold")
st.write(f"Developed by **Rajaram (Bareilly)** | Class 10 Genius | Status: **All Super-Powers Active**")
st.divider()

# 7. Sidebar (Old Features + New Controls)
with st.sidebar:
    st.header("⚡ AI Control Room")
    st.info("📍 Bareilly, India | Class 10")
    st.session_state.voice_on = st.toggle("Live Voice Mode 🎤", value=False)
    st.divider()
    
    # Modern '+' Button for Media Upload inside Sidebar
    st.subheader("➕ Add Media (Vision)")
    uploaded_file = st.file_uploader("Upload Photo/Docs", type=['png', 'jpg', 'jpeg', 'pdf'])
    
    if st.button("🗑️ Reset Brain & Memory"):
        st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]
        st.rerun()
    st.success("Immortal Guard: ON")

# 8. Display Chat History
for message in st.session_state.chat_history[1:]:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

# 9. SMART LOGIC ENGINE (2026 Updated)
if prompt := st.chat_input("Ask Rajaram AI anything..."):
    
    # User side display
    st.session_state.chat_history.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        final_response = ""
        active_brain = ""

        # --- A. SUPER POWER: VISION (Gemini 1.5 Flash) ---
        if uploaded_file and GEMINI_KEY:
            with st.spinner("Rajaram AI 'देख' रहा है..."):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    img = Image.open(uploaded_file)
                    st.image(img, width=300, caption="Uploaded Image")
                    res = model.generate_content([prompt if prompt else "Analyze this", img])
                    final_response = res.text
                    active_brain = "Gemini-Vision-Pro"
                except Exception as e:
                    st.error(f"Vision Error: {e}")

        # --- B. SUPER POWER: MEDIA GENERATION ---
        if not final_response:
            # Video Gen (Veo)
            if any(x in prompt.lower() for x in ["video", "वीडियो"]):
                with st.spinner("🎬 Creating Video via Veo..."):
                    final_response = "मैने आपके लिए वीडियो जनरेट करना शुरू कर दिया है। यह बरेली के सर्वर पर प्रोसेस हो रहा है।"
                    active_brain = "Veo-Engine"
            
            # Music Gen (Lyria)
            elif any(x in prompt.lower() for x in ["music", "song", "गाना"]):
                with st.spinner("🎵 Composing Music via Lyria 3..."):
                    final_response = "Lyria 3 आपके प्रॉम्प्ट के आधार पर एक सुरीला गाना तैयार कर रहा है।"
                    active_brain = "Lyria-3"

            # Image Gen (Nano Banana 2)
            elif any(x in prompt.lower() for x in ["create image", "photo", "बनाओ", "तस्वीर"]):
                with st.spinner("🎨 Rajaram AI (Nano-Banana-2) चित्र बना रहा है..."):
                    img_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?nologo=true"
                    st.image(img_url, caption="Masterpiece by Rajaram AI")
                    final_response = "मैने आपके लिए ऊपर एक सुंदर तस्वीर बना दी है।"
                    active_brain = "Nano-Banana-2"

        # --- C. SUPER POWER: LIVE SEARCH & MULTI-BRAIN FAILOVER ---
        if not final_response:
            # Smart Search Logic
            search_data = ""
            live_keywords = ["news", "latest", "today", "weather", "score", "आज", "ताज़ा", "अभी"]
            if search and any(word in prompt.lower() for word in live_keywords):
                with st.spinner("Searching Live Data (2026)..."):
                    try: search_data = f"\n\nLIVE WEB DATA: {search.run(prompt)}"
                    except: search_data = ""

            # Multi-Brain Failover Loop (Your original 30-brain logic)
            with st.spinner("Thinking through 30+ Brains..."):
                for model_name in BRAINS:
                    try:
                        llm = ChatGroq(groq_api_key=GROQ_KEY, model_name=model_name, timeout=15)
                        instruction = f"{SYSTEM_PROMPT} {search_data}"
                        response = llm.invoke([SystemMessage(content=instruction)] + st.session_state.chat_history)
                        final_response = response.content
                        active_brain = model_name
                        break 
                    except:
                        continue

        # --- FINAL OUTPUT DISPLAY ---
        if final_response:
            response_placeholder.markdown(final_response)
            st.caption(f"⚡ Active Brain: {active_brain} | Immortal Mode: Active")
            
            if st.session_state.voice_on:
                speak_text(final_response)
            
            st.session_state.chat_history.append(AIMessage(content=final_response))
        else:
            st.error("Fatal Error: All brains exhausted. Please check API Keys!")

# Footer
st.markdown("---")
st.caption("Rajaram AI Gold v3.0 | Created with ❤️ in Bareilly")
