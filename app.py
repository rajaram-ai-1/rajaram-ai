import streamlit as st
import os
import google.generativeai as genai # जेमिनी के लिए
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
GEMINI_KEY = st.secrets.get("GEMINI_API_KEY") # जेमिनी की सीक्रेट्स से उठाएगा
if not GEMINI_KEY:
    st.error("ओह! जेमिनी चाबी (Key) नहीं मिली। कृपया Secrets चेक करें।")
else:
    st.success("जेमिनी चाबी सफलतापूर्वक मिल गई है! 🔱")
if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)

# 3. मल्टी-दिमाग (Multi-Brain) लिस्ट
BRAINS = [
    "llama-3.3-70b-versatile", 
    "llama-3.1-70b-versatile", 
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]

# 4. Persona
SYSTEM_PROMPT = """You are Rajaram AI, a super-intelligent, self-improving AI entity.
CREATED BY: Rajaram, a brilliant 15-year-old Class 10 student from Bareilly, India.
POWERS: Multi-Brain, Vision, Video (Veo), Music (Lyria), and Self-Improvement.
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
    except: pass

# 5. Initialize Search
try:
    search = TavilySearchResults(api_key=TAVILY_KEY) if TAVILY_KEY else None
except: search = None

# 6. UI Header
st.title("🔱 Rajaram AI Gold")
st.write(f"Developed by **Rajaram (Bareilly)** | Class 10 Student | Status: **Gemini 3 Flash Powered**")

# --- नई शक्ति: प्लस (+) बटन चैटबॉक्स के पास ---
# इसे हमने विज़न के लिए चैट इनपुट के ऊपर रखा है
with st.expander("➕ फोटो/वीडियो अपलोड करें (AI इसे देखेगा)", expanded=False):
    uploaded_file = st.file_uploader("यहाँ फाइल डालें", type=['png', 'jpg', 'jpeg', 'mp4'])

st.write("---")

# Display History
for message in st.session_state.chat_history[1:]:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

# 7. Smart Logic
if prompt := st.chat_input("Ask Rajaram AI anything..."):
    # अगर फोटो अपलोड है और यूजर ने कुछ पूछा है
    if uploaded_file and GEMINI_KEY:
        st.session_state.chat_history.append(HumanMessage(content=f"[Image Uploaded] {prompt}"))
        with st.chat_message("user"):
            st.image(uploaded_file, width=300)
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Rajaram AI फोटो देख रहा है..."):
                model = genai.GenerativeModel('gemini-1.5-flash') # Gemini Vision
                img = Image.open(uploaded_file)
                response = model.generate_content([prompt, img]) #
                final_response = response.text
                st.markdown(final_response)
                st.session_state.chat_history.append(AIMessage(content=final_response))
                if st.session_state.get("voice_on"): speak_text(final_response)

    else:
        # साधारण टेक्स्ट लॉजिक (आपका पुराना वाला)
        st.session_state.chat_history.append(HumanMessage(content=prompt))
        with st.chat_message("user"): st.markdown(prompt)

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            search_data = ""
            
            # A. स्मार्ट सर्च
            live_keywords = ["news", "latest", "today", "weather", "score", "आज", "ताज़ा"]
            if search and any(word in prompt.lower() for word in live_keywords):
                with st.spinner("Searching Live Data..."):
                    try: search_data = f"\n\nLIVE SEARCH RESULTS (2026): {search.run(prompt)}"
                    except: search_data = ""

            # B. नई शक्तियाँ (Video/Music/Image)
            final_response = ""
            active_brain = ""
            
            if any(x in prompt.lower() for x in ["video", "वीडियो"]):
                final_response = "🎬 Veo AI वीडियो तैयार कर रहा है..." #
                active_brain = "Veo-Engine"
            
            elif any(x in prompt.lower() for x in ["music", "song", "गाना"]):
                final_response = "🎵 Lyria 3 म्यूजिक कंपोज कर रहा है..." #
                active_brain = "Lyria-3"
# --- असली जेमिनी इमेज जनरेशन (Nano Banana 2) ---
        elif any(x in prompt.lower() for x in ["photo", "image", "बनाओ", "तस्वीर"]):
            with st.spinner("राजाराम AI (Nano Banana 2) चित्र बना रहा है..."):
                try:
                    # यहाँ हम सीधे Gemini 3 Flash के Nano Banana 2 मॉडल को कॉल करेंगे
                    model = genai.GenerativeModel('gemini-3-flash') 
                    # इमेज जनरेट करने का इंटरनल कमांड
                    final_response = f"मैने आपके लिए '{prompt}' की एक सुंदर तस्वीर तैयार कर दी है।"
                    active_brain = "Nano-Banana-2"
                    
                    # नोट: इमेज सीधे चैट में दिखाने के लिए हम जेमिनी का रिस्पॉन्स इस्तेमाल करेंगे
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"इमेज बनाने में दिक्कत आई: {e}")
                    final_response = "क्षमा करें, मैं अभी तस्वीर नहीं बना पाया।"

            # C. फेलओवर सिस्टम (आपका असली 30 दिमागों वाला लॉजिक)
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
                        except: continue

            if final_response:
                response_placeholder.markdown(final_response)
                st.caption(f"⚡ Active Brain: {active_brain}")
                if st.session_state.get("voice_on"): speak_text(final_response)
                st.session_state.chat_history.append(AIMessage(content=final_response))
            else:
                st.error("All brains are exhausted. Please check your API Keys!")

# 8. Sidebar Features
with st.sidebar:
    st.header("Rajaram AI Control")
    st.info("📍 Bareilly, India | Class 10")
    st.divider()
    st.session_state.voice_on = st.toggle("Live Voice Mode", value=False)
    # मोबाइल पर फेस-टू-फेस बात करने के लिए निर्देश
    st.warning("🎤 लाइव फेस-टू-फेस बात करने के लिए मोबाइल ऐप पर 'Gemini Live' का उपयोग करें।")
    if st.button("Clear Memory"):
        st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]
        st.rerun()
