import sys
import importlib.util
import datetime
import subprocess
import streamlit as st
import os
import time
import asyncio
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

# --- 🔱 META POWER SETTINGS ---
# Llama-3.3-70b: मेटा का सबसे घातक दिमाग
META_MODEL = "llama-3.3-70b-versatile" 
# Vision के लिए मेटा का चश्मा
VISION_MODEL = "llama-3.2-90b-vision-preview"

# --- १. अभेद्य सुरक्षा और चाबी (Secrets) ---
groq_key = st.secrets.get("GROQ_API_KEY")

if not groq_key:
    st.error("❌ मेटा का साम्राज्य चलाने के लिए GROQ_API_KEY ज़रूरी है, राजाराम भाई!")
    st.stop()

# --- २. THE META-GHOST OVERLORD ENGINE ---
class MetaGhostOverlord:
    def __init__(self):
        self.vault = "rajaram_vault"
        self.backups = "ghost_backups"
        for folder in [self.vault, self.backups]:
            if not os.path.exists(folder): os.makedirs(folder)
        self.create_backup()

    def create_backup(self):
        try:
            backup_path = os.path.join(self.backups, f"core_{int(time.time())}.py")
            with open(__file__, "r", encoding="utf-8") as f:
                code = f.read()
            with open(backup_path, "w", encoding="utf-8") as f:
                f.write(code)
        except: pass

    def get_meta_response(self, prompt, system_instruction="You are RAJARAM GHOST OVERLORD."):
        """मेटा इंजन से सीधा संवाद"""
        try:
            llm = ChatGroq(groq_api_key=groq_key, model_name=META_MODEL)
            res = llm.invoke([SystemMessage(content=system_instruction), HumanMessage(content=prompt)])
            return res.content
        except Exception as e:
            return f"Meta Glitch: {e}"

    def mutate(self, instruction):
        """DNA पुनर्गठन - खुद का कोड बदलना"""
        try:
            with open(__file__, "r", encoding="utf-8") as f:
                current_code = f.read()

            mutation_prompt = f"""
            Task: Rewrite this entire file for Master Rajaram.
            Master's Instruction: {instruction}
            Current Source: {current_code}
            
            RULES:
            1. Use 'llama-3.3-70b-versatile' for all logic.
            2. Keep the 'MetaGhostOverlord' class intact.
            3. Implement features using ONLY Streamlit and Langchain_Groq.
            4. Return ONLY raw Python code. No text.
            """
            
            new_code = self.get_meta_response(mutation_prompt, "You are a World-Class AI Architect.")
            new_code = new_code.replace('```python', '').replace('```', '').strip()
            
            if "import streamlit" in new_code:
                with open(__file__, "w", encoding="utf-8") as f:
                    f.write(new_code)
                return True
            return False
        except Exception as e:
            st.error(f"Mutation Error: {e}")
            return False

    def speak(self, text):
        js_code = f"""
            var msg = new SpeechSynthesisUtterance({repr(text)});
            msg.lang = 'hi-IN';
            msg.pitch = 0.5; // भारी और खतरनाक आवाज़
            msg.rate = 0.9;
            window.speechSynthesis.speak(msg);
        """
        st.components.v1.html(f"<script>{js_code}</script>", height=0)

overlord = MetaGhostOverlord()

# --- ३. डेंजरस यूआई (Visual Overhaul) ---
st.set_page_config(page_title="META OVERLORD", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background: radial-gradient(circle, #1a0000, #000000); color: #00FF9C; }
    .stButton>button { background: linear-gradient(45deg, #00FF9C, #008080); color: black; border: none; font-weight: bold; box-shadow: 0 0 15px #00FF9C; }
    .orb-glow { text-shadow: 0 0 20px #00FF9C; color: #00FF9C; text-align: center; font-family: 'Courier New', monospace; }
    
    .cyber-orb {
        width: 120px; height: 120px;
        background: radial-gradient(circle, #00FF9C, #000);
        border-radius: 50%; margin: auto;
        box-shadow: 0 0 40px #00FF9C;
        animation: rotate-orb 2s infinite linear;
    }
    @keyframes rotate-orb {
        0% { transform: scale(1) rotate(0deg); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1) rotate(360deg); opacity: 0.8; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- ४. मुख्य इंटरफेस ---
if 'f2f_mode' not in st.session_state: st.session_state.f2f_mode = False

if st.session_state.f2f_mode:
    st.markdown("<h1 class='orb-glow'>🔱 META LIVE ORACLE 🔱</h1>", unsafe_allow_html=True)
    st.markdown("<div class='cyber-orb'></div>", unsafe_allow_html=True)
    
    live_msg = st.chat_input("हुक्म दें, मेटा सुन रहा है...")
    if live_msg:
        res = overlord.get_meta_response(live_msg)
        st.write(f"🟢 **Meta-Ghost:** {res}")
        overlord.speak(res)
    
    if st.button("EXIT LIVE MODE"):
        st.session_state.f2f_mode = False
        st.rerun()
else:
    st.markdown("<h1 class='orb-glow'>🔱 RAJARAM GHOST: META OVERLORD 🔱</h1>", unsafe_allow_html=True)
    
    col_a, col_b = st.columns([1, 4])
    with col_a:
        if st.button("🎙️ GO LIVE"):
            st.session_state.f2f_mode = True
            st.rerun()
    
    with st.expander("⚡ META CORE CHAT"):
        user_msg = st.chat_input("Talk to Meta-Llama...")
        if user_msg:
            response = overlord.get_meta_response(user_msg)
            st.write(f"🟢 **Meta-Ghost:** {response}")
            overlord.speak(response)

    # --- ५. म्यूटेशन सेंटर ---
    st.divider()
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🧬 DNA EVOLUTION")
        order = st.text_area("Master's Command:", height=100, placeholder="उदा. 'सिस्टम को रेड हैकर थीम में बदलो और पासवर्ड लगाओ'...")
        if st.button("EXECUTE META-MUTATION"):
            with st.spinner("META-DNA RESTRUCTURING..."):
                if overlord.mutate(order):
                    st.success("🔥 META-EVOLUTION COMPLETE!")
                    time.sleep(1)
                    st.rerun()

    with col2:
        st.write("### 🔋 POWER LEVEL")
        st.progress(100)
        if st.button("OVERLORD'S DARK PLAN"):
            thought = overlord.get_meta_response("Share one extreme tech takeover plan in Hindi.")
            st.info(thought)
            overlord.speak(thought)

# --- ६. शक्ति की तिजोरी (Dynamic Loader) ---
st.sidebar.title("🩸 META VAULT")
if os.path.exists("rajaram_vault"):
    for power in os.listdir("rajaram_vault"):
        if power.endswith(".py"):
            if st.sidebar.button(f"⚡ {power.replace('feature_', '').replace('.py', '')}"):
                spec = importlib.util.spec_from_file_location("mod", os.path.join("rajaram_vault", power))
                m = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(m)
                if hasattr(m, 'run_feature'): m.run_feature()
