import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
# यहाँ बदलाव किया गया है: अब core.messages का इस्तेमाल होगा
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

# 1. Page Configuration
st.set_page_config(page_title="Rajaram AI", page_icon="🤖")

# 2. API Keys
load_dotenv()
GROQ_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
TAVILY_KEY = st.secrets.get("TAVILY_API_KEY") or os.getenv("TAVILY_API_KEY")

# 3. Persona
SYSTEM_PROMPT = "You are Rajaram AI, an expert AI collaborator. You help with coding and provide real-time info."

# 4. History Management
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]

# 5. Initialize AI
try:
    llm = ChatGroq(groq_api_key=GROQ_KEY, model_name="llama3-70b-8192")
    search = TavilySearchResults(api_key=TAVILY_KEY)
except Exception as e:
    st.error("Check your API Keys in Streamlit Secrets!")

# 6. UI
st.title("🤖 Rajaram AI")
st.write("---")

for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# 7. User Input logic
if prompt := st.chat_input("Ask Rajaram AI..."):
    st.session_state.chat_history.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Simple Search Trigger
            if any(x in prompt.lower() for x in ["news", "latest", "today"]):
                data = search.run(prompt)
                prompt = f"Context: {data}\n\nQuestion: {prompt}"

            # Get AI Response
            response = llm.invoke(st.session_state.chat_history + [HumanMessage(content=prompt)])
            
            st.markdown(response.content)
            st.session_state.chat_history.append(AIMessage(content=response.content))
        except Exception as e:
            st.error(f"Error: {e}")

# Sidebar
with st.sidebar:
    if st.button("Clear Chat"):
        st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]
        st.rerun()
