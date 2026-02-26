import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

# 1. पेज की सेटिंग (Look & Feel)
st.set_page_config(page_title="Rajaram AI", page_icon="🤖", layout="wide")

# 2. API Keys लोड करना
load_dotenv()
GROQ_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
TAVILY_KEY = st.secrets.get("TAVILY_API_KEY") or os.getenv("TAVILY_API_KEY")

# 3. Rajaram AI का "व्यक्तित्व" (Personality Setup)
SYSTEM_PROMPT = """
You are Rajaram AI, an authentic, adaptive, and intelligent AI collaborator.
Your goal is to help users with coding, AI development, and solving problems with wit and clarity.
You balance empathy with candor: you are supportive but also direct.
You write expert-level Python code and use search tools when you need up-to-date information.
Always introduce yourself as Rajaram AI when asked.
"""

# 4. Memory (Chat History) को संभालना
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]

# 5. AI और सर्च इंजन सेटअप
try:
    llm = ChatGroq(groq_api_key=GROQ_KEY, model_name="llama3-70b-8192", temperature=0.7)
    search = TavilySearchResults(api_key=TAVILY_KEY)
except Exception as e:
    st.error(f"Setup Error: API Keys missing or invalid.")

# 6. UI डिजाइन
st.markdown("<h1 style='text-align: center; color: #00d4ff;'>Rajaram AI</h1>", unsafe_allow_html=True)
st.write("---")

# पुरानी चैट दिखाना (UI पर)
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# 7. यूजर इनपुट और जवाब (Main Logic)
if prompt := st.chat_input("Mujhse kuch bhi puchiye..."):
    # यूजर का मैसेज सेव करें
    st.session_state.chat_history.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI का जवाब जेनरेट करना
    with st.chat_message("assistant"):
        with st.spinner("Rajaram AI is thinking..."):
            try:
                # क्या सर्च की ज़रूरत है? (Simple Logic)
                search_context = ""
                if any(word in prompt.lower() for word in ["latest", "news", "score", "today", "weather"]):
                    search_data = search.run(prompt)
                    search_context = f"\n\nInternet Search Result: {search_data}"

                # फाइनल इनपुट तैयार करना
                final_prompt = st.session_state.chat_history + [HumanMessage(content=search_context)]
                
                # AI से जवाब लेना
                response = llm.predict_messages(final_prompt)
                
                # जवाब दिखाना और सेव करना
                st.markdown(response.content)
                st.session_state.chat_history.append(AIMessage(content=response.content))
                
            except Exception as e:
                st.error("Connection Error. Please check your Internet or API Keys.")

# 8. Sidebar (Settings)
with st.sidebar:
    st.title("Rajaram AI Panel")
    if st.button("Clear Memory"):
        st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]
        st.rerun()
