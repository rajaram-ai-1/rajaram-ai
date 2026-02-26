import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from gtts import gTTS
import base64

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
# अगर एक दिमाग (Model) फेल हुआ, तो AI खुद दूसरे पर स्विच कर जाएगा
BRAINS = [
    "llama-3.3-70b-versatile", 
    "llama-3.1-70b-versatile", 
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]

# 4. Persona (स्व-सुधार और पहचान)
SYSTEM_PROMPT = """You are Rajaram AI, a super-intelligent, self-improving AI entity.
CREATED BY: Rajaram, a brilliant 15-year-old Class 10 student from Bareilly, India.
POWERS: 
1. Multi-Brain Failover: You can switch between different models if one is down.
2. Self-Improvement: You analyze your own code to suggest more powerful versions.
3. Smart Search: Use Tavily ONLY for live events/news. Use internal brain for studies/fun.
4. Language: If asked in Hindi, reply in clear Hindi. If in English, reply in English.
TODAY'S DATE: February 26, 2026."""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]

# Voice Function
def speak_text(text):
    try:
        tts = gTTS(text=text[:200], lang='hi') # Speed ke liye limit
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
st.write(f"Developed by **Rajaram (Bareilly)** | Class 10 Student | Status: **Immortal & Self-Improving**")
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
        
        # A. स्मार्ट सर्च लॉजिक (पढ़ाई के समय सर्च नहीं, खबरों के समय सर्च)
        search_data = ""
        live_keywords = ["news", "latest", "today", "weather", "score", "आज", "ताज़ा", "अभी"]
        if search and any(word in prompt.lower() for word in live_keywords):
            with st.spinner("Searching Live Data..."):
                try:
                    search_data = f"\n\nLIVE SEARCH RESULTS (2026): {search.run(prompt)}"
                except:
                    search_data = "\n\nSearch engine busy, using internal logic."

        # B. फेलओवर सिस्टम (दिमाग बदलना)
        # 
        final_response = ""
        active_brain = ""
        
        with st.spinner("Thinking through multiple brains..."):
            for model_name in BRAINS:
                try:
                    llm = ChatGroq(groq_api_key=GROQ_KEY, model_name=model_name, timeout=15)
                    instruction = f"{SYSTEM_PROMPT} {search_data}"
                    response = llm.invoke([SystemMessage(content=instruction)] + st.session_state.chat_history)
                    final_response = response.content
                    active_brain = model_name
                    break # अगर सफल हुआ तो रुक जाओ
                except:
                    continue # अगर फेल हुआ तो अगले दिमाग पर जाओ

        if final_response:
            response_placeholder.markdown(final_response)
            st.caption(f"⚡ Active Brain: {active_brain} | Self-Optimization: Active")
            
            if st.session_state.get("voice_on", False):
                speak_text(final_response)

            st.session_state.chat_history.append(AIMessage(content=final_response))
        else:
            st.error("All 30 brains are currently exhausted. Please check your API Keys!")

# 8. Sidebar Features
with st.sidebar:
    st.header("Creator: Rajaram")
    st.info("📍 Bareilly, India\n📚 Class 10 Developer\n🔥 Age: 15")
    st.divider()
    st.session_state.voice_on = st.toggle("Enable AI Voice", value=False)
    if st.button("Self-Optimize & Clear Memory"):
        st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]
        st.rerun()
    st.success("Immortal Mode: ON")
    
