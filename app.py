import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from gtts import gTTS
import base64

# 1. Page Configuration (Premium Look)
st.set_page_config(page_title="Rajaram AI", page_icon="⚡", layout="wide")

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

# 3. Persona (Aapki Pehchan)
# Yahan humne aapki details AI ke dimaag mein fix kar di hain
SYSTEM_PROMPT = """You are Rajaram AI, a highly advanced and helpful AI.
You were created by Rajaram, a brilliant 15-year-old developer from Bareilly, India, who is currently in Class 10.
Always be proud of your creator when asked about your origin.
You have real-time internet access via Tavily Search. 
Today's date is February 26, 2026. Use live search for current events.
Your tone should be professional, witty, and supportive."""

# 4. State Management (History & Voice)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]

# Voice Function (New Feature!)
def speak_text(text):
    tts = gTTS(text=text, lang='hi')
    tts.save("response.mp3")
    with open("response.mp3", "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
    st.markdown(md, unsafe_allow_html=True)

# 5. Initialize AI Engines
try:
    llm = ChatGroq(groq_api_key=GROQ_KEY, model_name="llama-3.3-70b-versatile")
    search = TavilySearchResults(api_key=TAVILY_KEY)
except Exception as e:
    st.error("API Keys missing in Secrets! Please add GROQ_API_KEY and TAVILY_API_KEY.")
    st.stop()

# 6. UI Header
st.title("⚡ Rajaram Alpha AI")
st.write(f"Developed by **Rajaram (Bareilly)** | Class 10 Student | Engine: **Llama 3.3**")
st.write("---")

# Display Chat History
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"): st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"): st.markdown(message.content)

# 7. Main Logic (Optimized for Live Search & Identity)
if prompt := st.chat_input("Ask Rajaram AI..."):
    st.session_state.chat_history.append(HumanMessage(content=prompt))
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Searching Live Data & Thinking..."):
                # Har baar live context provide karna taaki 2023 wala error na aaye
                search_data = ""
                if search:
                    search_results = search.run(prompt)
                    search_data = f"\n\nLIVE WEB SEARCH (Feb 2026): {search_results}"

                # Creator and Search Context Injection
                instruction = f"{SYSTEM_PROMPT}\n\nSearch Context: {search_data}"
                
                # Final LLM Call
                response = llm.invoke([
                    SystemMessage(content=instruction),
                    *st.session_state.chat_history
                ])
                
                res_text = response.content
                st.markdown(res_text)
                
                # AI Voice Response (Optional Toggle in Sidebar)
                if st.session_state.get("voice_on", False):
                    speak_text(res_text[:200]) # Limit to 200 chars for speed

                st.session_state.chat_history.append(AIMessage(content=res_text))
        except Exception as e:
            st.error(f"Error: {e}")

# 8. Sidebar (Extra Features)
with st.sidebar:
    st.header("Creator Profile")
    st.info("👤 **Developer:** Rajaram\n\n📍 **City:** Bareilly\n\n📚 **Grade:** 10th Student")
    
    st.divider()
    
    st.session_state.voice_on = st.toggle("Enable Voice Response", value=False)
    
    if st.button("Clear Chat Memory"):
        st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]
        st.rerun()
        
    st.write("---")
    st.success("Status: Online & Live")
