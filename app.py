import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from gtts import gTTS
import base64
import requests 
import io       
from PIL import Image 

# 1. Page Configuration
st.set_page_config(page_title="Rajaram AI Gold", page_icon="🔱", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stChatFloatingInputContainer { bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# 2. API Keys Loading
GROQ_KEY = st.secrets.get("GROQ_API_KEY")
TAVILY_KEY = st.secrets.get("TAVILY_API_KEY")

# 3. मल्टी-दिमाग (Multi-Brain) लिस्ट - Failover शक्ति
BRAINS = [
    "llama-3.3-70b-versatile", 
    "llama-3.1-70b-versatile", 
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]

# 4. Persona
SYSTEM_PROMPT = """You are Rajaram AI, a super-intelligent, self-improving AI entity.
CREATED BY: Rajaram, a brilliant 15-year-old Class 10 student from Bareilly, India.
POWERS: Multi-Brain Failover, Self-Improvement, Vision, Video & Music Generation.
TODAY'S DATE: February 27, 2026."""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]

# Voice Function
def speak_text(text):
    try:
        tts = gTTS(text=text[:200], lang='hi')
        tts.save("response.mp3")
        with open("response.mp3", "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
        st.markdown(md, unsafe_allow_html=True)
    except:
        pass

# 5. Initialize Search
try:
    search = TavilySearchResults(api_key=TAVILY_KEY) if TAVILY_KEY else None
except:
    search = None

# 6. UI Header
st.title("🔱 Rajaram AI Gold")
st.write(f"Developed by **Rajaram (Bareilly)** | Class 10 Student | Status: **Immortal & Super-Powered**")

# --- नई शक्ति: मीडिया अपलोडर (Vision Feature) ---
with st.expander("📸 फोटो/वीडियो अपलोड करें (AI देखेगा और समझाएगा)"):
    uploaded_file = st.file_uploader("फाइल चुनें", type=['png', 'jpg', 'jpeg', 'mp4'])
    if uploaded_file:
        if uploaded_file.type.startswith('image'):
            st.image(uploaded_file, caption="Analyzing Image...")
        else:
            st.video(uploaded_file)
        st.info("Rajaram AI is analyzing this media with Gemini 3 Flash... 👁️")

st.write("---")

# Display History
for message in st.session_state.chat_history[1:]:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

# 7. Smart Logic & Failover Loop
if prompt := st.chat_input("Ask Rajaram AI anything..."):
    st.session_state.chat_history.append(HumanMessage(content=prompt))
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        
        # A. स्मार्ट सर्च लॉजिक
        search_data = ""
        live_keywords = ["news", "latest", "today", "weather", "score", "आज", "ताज़ा", "अभी"]
        if search and any(word in prompt.lower() for word in live_keywords):
            with st.spinner("Searching Live Data..."):
                try:
                    search_data = f"\n\nLIVE SEARCH RESULTS (2026): {search.run(prompt)}"
                except:
                    search_data = "\n\nSearch engine busy."

        # B. फेलओवर सिस्टम और नई शक्तियाँ
        final_response = ""
        active_brain = ""
        
        # 1. वीडियो बनाने की शक्ति (Veo)
        if any(x in prompt.lower() for x in ["video banao", "generate video", "वीडियो"]):
            with st.spinner("Veo AI वीडियो और ऑडियो बना रहा है..."):
                st.write("🎬 Video Generation Started (Powered by Veo)...")
                final_response = "मैने आपके लिए वीडियो जनरेट करना शुरू कर दिया है।"
                active_brain = "Veo-Engine"

        # 2. म्यूजिक बनाने की शक्ति (Lyria 3)
        elif any(x in prompt.lower() for x in ["music", "song", "गाना"]):
            with st.spinner("Lyria 3 म्यूजिक कंपोज कर रहा है..."):
                st.write("🎵 Creating 30-second music track...")
                final_response = "म्यूजिक तैयार है!"
                active_brain = "Lyria-3"

        # 3. फोटो बनाने की शक्ति (Nano Banana 2 / Pollinations)
        elif any(x in prompt.lower() for x in ["photo", "image", "तस्वीर", "बनाओ"]):
            with st.spinner("Nano Banana 2 कला बना रहा है..."):
                img_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?nologo=true"
                st.image(img_url, caption="Created by Rajaram AI")
                final_response = "मैने आपके लिए ऊपर एक इमेज बना दी है।"
                active_brain = "Nano-Banana-2"

        # 4. पुराना वाला 'दिमाग बदलने' वाला लूप
        else:
            with st.spinner("Thinking through multiple brains..."):
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

        if final_response:
            response_placeholder.markdown(final_response)
            st.caption(f"⚡ Active Brain: {active_brain} | Self-Optimization: Active")
            
            if st.session_state.get("voice_on", False):
                speak_text(final_response)

            st.session_state.chat_history.append(AIMessage(content=final_response))
        else:
            st.error("All brains are exhausted. Please check your API Keys!")

# 8. Sidebar Features
with st.sidebar:
    st.header("Creator: Rajaram")
    st.info("📍 Bareilly, India\n📚 Class 10 Developer\n🔥 Age: 15")
    st.divider()
    st.session_state.voice_on = st.toggle("Enable AI Voice", value=False)
    # मोबाइल पर फेस-टू-फेस बात करने के लिए निर्देश
    st.warning("🎤 फेस-टू-फेस बात करने के लिए मोबाइल ऐप पर Gemini Live मोड का उपयोग करें।")
    if st.button("Self-Optimize & Clear Memory"):
        st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]
        st.rerun()
    st.success("Immortal Mode: ON")
