import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import MessagesPlaceholder
from langchain.schema import SystemMessage
from dotenv import load_dotenv

# 1. Page Configuration
st.set_page_config(page_title="Rajaram AI", page_icon="🤖", layout="wide")

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    header {visibility: hidden;}
    .main-title { font-size: 50px; font-weight: bold; color: #00d4ff; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# 2. API Keys Loading
load_dotenv()
GROQ_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
TAVILY_KEY = st.secrets.get("TAVILY_API_KEY") or os.getenv("TAVILY_API_KEY")

# 3. Rajaram AI Personality (System Prompt)
# Yahi wo part hai jo ise meri tarah banata hai
rajaram_persona = SystemMessage(content="""
You are Rajaram AI, a highly advanced and helpful AI assistant. 
Your goal is to help users with coding, web development, and solving complex problems.
You are professional, polite, and can write expert-level Python code. 
You have access to the internet to provide real-time information.
Always respond in a way that is easy to understand, just like a human expert.
""")

# 4. Initialize Session State (Memory)
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferWindowMemory(
        memory_key="chat_history", k=10, return_messages=True
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. AI Setup
search_tool = TavilySearchResults(api_key=TAVILY_KEY)
llm = ChatGroq(
    groq_api_key=GROQ_KEY,
    model_name="llama3-70b-8192", # Sabse powerful model
    temperature=0.5
)

# Agent setup with Memory and Persona
agent_kwargs = {
    "extra_prompt_messages": [MessagesPlaceholder(variable_name="chat_history")],
    "system_message": rajaram_persona,
}

agent_executor = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=st.session_state.memory,
    agent_kwargs=agent_kwargs,
    verbose=True,
    handle_parsing_errors=True
)

# 6. UI Layout
st.markdown("<h1 class='main-title'>Rajaram AI Engine</h1>", unsafe_allow_html=True)
st.write("---")

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("How can Rajaram AI help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Processing with Rajaram Intelligence..."):
            try:
                # Running the Agent
                response = agent_executor.run(input=prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error: {str(e)}")

# 7. Sidebar with Advanced Features
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100)
    st.title("Rajaram AI Settings")
    st.success("Mode: God Mode Activated")
    st.info("Uses Llama-3-70B & Real-time Web Search")
    
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.session_state.memory.clear()
        st.rerun()
