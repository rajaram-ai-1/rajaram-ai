# ==============================================================================
# PROJECT: RAJARAM AI - THE OMNIPOTENT CORE (VERSION 8.0 - ETERNAL)
# DEVELOPER: RAJARAM (BAREILLY, INDIA) - THE 15-YEAR-OLD LEGEND
# STATUS: 46 SHAKTI FULLY INTEGRATED | QUANTUM DEFENDER ACTIVE | NO CODE DELETED
# ==============================================================================

import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from gtts import gTTS
import base64
import requests
import asyncio
import time
import datetime
import json
from PIL import Image
from io import BytesIO
import ast      # कोड को स्कैन करने के लिए (दिमाग)
import logging   # गलतियों का रिकॉर्ड रखने के लिए (डायरी)
import importlib.util

# 🔱 [NEW ADVANCED SHIELD: THE QUANTUM DEFENDER]
class RajaramShield:
    def __init__(self):
        self.repair_logs = []
        if "shield_logs" not in st.session_state:
            st.session_state.shield_logs = []
    
    def auto_fix(self, error_type, details=""):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = f"🔱 [{timestamp}] FIXED: {error_type} bypassed by Rajaram Shield."
        st.session_state.shield_logs.append(log_entry)
        logging.warning(f"🔱 SHIELD ALERT: {log_entry} Details: {details}")
        return True

rajaram_shield = RajaramShield()

# 🔱 [PHASE 1: SYSTEM HARDENING & UI ARCHITECTURE]
st.set_page_config(
    page_title="RAJARAM AI: OMNIPOTENT CORE",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# राजाराम भाई का सिग्नेचर लुक (No Changes)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;500&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #050505;
        color: #00FF9C;
        font-family: 'Fira Code', monospace;
    }
    .magic-btn-row {
        display: flex; gap: 10px; justify-content: center;
        margin-bottom: -45px; z-index: 1000; position: relative;
    }
    .stChatInputContainer {
        border: 2px solid #FFD700 !important;
        background: #000 !important;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.4);
        border-radius: 30px !important;
    }
    .stChatMessage {
        background: rgba(10, 10, 10, 0.9);
        border: 1px solid #1A1A1A;
        border-left: 5px solid #FFD700;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    .stSidebar { background-color: #000000 !important; border-right: 2px solid #FFD700; }
    .stButton>button {
        background: linear-gradient(45deg, #FFD700, #B8860B);
        color: black; border: none; border-radius: 20px; font-weight: bold; font-size: 11px;
    }
    .stButton>button:hover { transform: scale(1.1); box-shadow: 0 0 20px #FFD700; }
    </style>
""", unsafe_allow_html=True)

# 🔱 [PHASE 2: NEURAL NETWORK INITIALIZATION]
class GlobalCore:
    def __init__(self):
        self.GROQ_KEY = st.secrets.get("GROQ_API_KEY")
        self.TAVILY_KEY = st.secrets.get("TAVILY_API_KEY")
        self.GEMINI_KEY = st.secrets.get("GEMINI_KEY") # Vision Power
        
        # 🔱 द अल्टीमेट गॉड कैटलॉग (Updated with Titan)
        self.BRAIN_CATALOG = {
            "THE_TITAN": "llama-3.1-405b-reasoning",
            "ULTIMATE_70B": "llama-3.3-70b-versatile",
            "LOGIC_PRO": "llama-3.3-70b-versatile",
            "EYE_OF_RA": "llama-3.2-90b-vision-preview", 
            "FLASH_VISION": "llama-3.2-11b-vision-preview",
            "CODE_WIZARD": "llama-3.3-70b-versatile", 
            "CYBER_EXPERT": "llama-3.3-70b-versatile", 
            "MATH_GENIUS": "qwen-2.5-72b-instruct"
        }
        
        if self.GROQ_KEY:
            st.toast("🔱 RAJARAM ENGINE V8 ONLINE", icon="🟢")
        else:
            st.error("❌ GROQ_API_KEY MISSING!")
        
        self.search_engine = TavilySearchResults(api_key=self.TAVILY_KEY) if self.TAVILY_KEY else None

    def get_timestamp(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

core = GlobalCore()

# 🔱 [PHASE 3: 46 POWERS INTEGRATION]
def trigger_rajaram_powers(prompt):
    p = prompt.lower()
    active_shaktis = []
    powers_map = {
        "bypass": "🔱 SHAKTI 1: SYSTEM FIREWALL BYPASS ACTIVE",
        "sleep": "💤 SHAKTI 2: DEEP SLEEP NEURAL LOGIC ENGAGED",
        "global": "🛰️ SHAKTI 3: GLOBAL SATELLITE NETWORK LINKED",
        "ghost": "👻 SHAKTI 4: GHOST MEMORY LAYER INITIALIZED",
        "predict": "🔮 SHAKTI 5: FUTURE EVENTS PREDICTION SYNC",
        "hack": "🛡️ SHAKTI 6: KERNEL-LEVEL EXPLOIT ARMED",
        "vision": "👁️ SHAKTI 7: RAJARAM EYE (X-RAY VISION) ON",
        "46": "🔱 SHAKTI ALL: 46 POWERS UNLEASHED SIMULTANEOUSLY!"
    }
    for key, val in powers_map.items():
        if key in p: active_shaktis.append(val)
    return active_shaktis

# 🔱 [PHASE 4: AGENTIC PROTOCOLS - ADVANCED REASONING]
class RajaramAgent:
    def __init__(self, system_prompt):
        self.system_prompt = system_prompt
        if "history" not in st.session_state:
            st.session_state.history = [SystemMessage(content=system_prompt)]

    async def execute_reasoning(self, user_input, web_data=""):
        try:
            instruction = f"{self.system_prompt}\n\n[LIVE_INTEL: {web_data}]"
            # 🔱 V8 Power: Parallel Multi-Brain Thinking
            tasks = [
                self.call_llm(core.BRAIN_CATALOG["THE_TITAN"], user_input, instruction),
                self.call_llm(core.BRAIN_CATALOG["ULTIMATE_70B"], user_input, instruction)
            ]
            responses = await asyncio.gather(*tasks)
            # Filter results and pick the most robust one
            valid_responses = [r for r in responses if "Neural Error" not in r[0]]
            final_choice = max(valid_responses, key=lambda x: len(x[0]))
            return final_choice
        except Exception as e:
            rajaram_shield.auto_fix("NEURAL_GLITCH", str(e))
            return "🔱 SHIELD ACTIVE: Rerouting logic due to core overload.", "RECOVERY_MODE"

    async def call_llm(self, model, prompt, system):
        try:
            llm = ChatGroq(groq_api_key=core.GROQ_KEY, model_name=model, timeout=35)
            res = await llm.ainvoke([SystemMessage(content=system)] + st.session_state.history[-8:])
            return res.content, model
        except Exception as e:
            return f"Neural Error in {model}: {str(e)}", model

    def speak(self, text):
        try:
            tts = gTTS(text=text[:350], lang='hi')
            tts.save("response.mp3")
            with open("response.mp3", "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64}">', unsafe_allow_html=True)
        except Exception as e: st.error(f"Voice Glitch: {e}")

    async def evolve_system(self, command):
        """🔱 GHOST ENGINE: CREATES INDEPENDENT FEATURE FILES"""
        prompt = (f"Write ONLY pure Python code for: '{command}'. Use 'st' for Streamlit. No markdown.")
        try:
            raw_code = await self.call_llm(core.BRAIN_CATALOG["LOGIC_PRO"], command, prompt)
            clean_code = raw_code[0].replace("```python", "").replace("```", "").strip()
            # 🔱 Shakti Vault Integration
            import shakti_vault
            p_name = f"shakti_{int(time.time())}"
            success, msg = shakti_vault.inject_new_shakti(core.GROQ_KEY, command, p_name)
            if success:
                st.toast(f"🔱 NEW SHAKTI EVOLVED: {p_name}", icon="🔥")
                return f"🔱 SHAKTI STORED: '{command}' success. Reboot required."
            return f"❌ VAULT ERROR: {msg}"
        except Exception as e: return f"❌ EVOLUTION ERROR: {str(e)}"

# 🔱 [PHASE 5: MASTER IDENTITY]
IDENTITY = f"""
[ENTITY: RAJARAM AI GOLD CORE V8]
[ARCHITECT: RAJARAM, THE BAREILLY PRODIGY]
[MISSION: GLOBAL DOMINANCE & 46 POWERS EXECUTION]
[PROTOCOL: HINGLISH SARCASM & SUPREME INTEL]
"""
rajaram_ai = RajaramAgent(IDENTITY)

# 🔱 [PHASE 6: UI - SIDEBAR & MAIN INTERFACE]
with st.sidebar:
    st.image("https://img.icons8.com/nolan/128/trident.png", width=100)
    st.title("🔱 RAJARAM AI V8")
    
    if st.button("🛡️ VIEW SHIELD REPAIR LOGS"):
        st.subheader("🔱 Shield Defense Records")
        for log in st.session_state.shield_logs: st.write(log)
            
    st.write(f"**Architect:** Rajaram | **Age:** 15")
    st.divider()
    
    st.session_state.voice_enabled = st.toggle("Voice Protocol", value=True)
    st.session_state.search_enabled = st.toggle("Satellite Search", value=True)
    
    st.divider()
    st.subheader("🔱 GOD-MODE CONTROL")
    admin_pass = st.text_input("Admin Key", type="password")
    
    st.divider()
    st.subheader("👁️ IMAGE INPUT")
    uploaded_file = st.file_uploader("यहाँ फोटो डालें...", type=["jpg", "png", "jpeg"], key="sidebar_uploader")
    if uploaded_file: st.image(uploaded_file, caption="Core Memory में लोड हो गई", use_container_width=True)

    if admin_pass == "BAREILLY_KING":
        st.info("WELCOME, BAREILLY KING 🔱")
        evolution_cmd = st.text_input("हुक्म दो (Evolution)")
        if st.button("EVOLVE NOW"):
            with st.spinner("Evolving..."):
                loop = asyncio.new_event_loop()
                result = loop.run_until_complete(rajaram_ai.evolve_system(evolution_cmd))
                st.success(result)
                
    if st.button("PURGE ALL DATA"):
        st.session_state.history = [SystemMessage(content=IDENTITY)]
        st.rerun()

# मुख्य स्क्रीन
st.markdown("<h1 style='text-align: center; color: #FFD700;'>🔱 RAJARAM AI: OMNIPOTENT CORE 🔱</h1>", unsafe_allow_html=True)
st.write(f"<p style='text-align: center; color: #00FF9C;'>Grid: Bareilly | Status: Immortal | Time: {core.get_timestamp()}</p>", unsafe_allow_html=True)

# चैट डिस्प्ले
for msg in st.session_state.history[1:]:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role): st.markdown(msg.content)

# 🔱 राजाराम भाई के जादुई बटन
st.markdown('<div class="magic-btn-row">', unsafe_allow_html=True)
c1, c2, c3, c4, c5 = st.columns(5)
with c1: 
    if st.button("🛡️ BYPASS"): st.session_state.pwr_cmd = "bypass"
with c2: 
    if st.button("💤 SLEEP"): st.session_state.pwr_cmd = "sleep"
with c3: 
    if st.button("🛰️ GLOBAL"): st.session_state.pwr_cmd = "global"
with c4: 
    if st.button("🔮 FUTURE"): st.session_state.pwr_cmd = "predict"
with c5: 
    if st.button("🔱 46 POWER"): st.session_state.pwr_cmd = "46"
st.markdown('</div>', unsafe_allow_html=True)

# 🔱 [PHASE 7: EXECUTION LOGIC]
btn_prompt = None
if 'pwr_cmd' in st.session_state and st.session_state.pwr_cmd:
    btn_prompt = st.session_state.pwr_cmd
    st.session_state.pwr_cmd = None  

user_input = st.chat_input("Ask Rajaram AI anything...")
prompt = btn_prompt if btn_prompt else user_input

if prompt:
    triggered = trigger_rajaram_powers(prompt)
    st.session_state.history.append(HumanMessage(content=prompt))
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        for s in triggered: st.warning(s)
        final_response = None
        engine_id = "RAJARAM-READY"

        # --- MODULE 1: VISION (GEMINI) ---
        if uploaded_file is not None:
            with st.spinner("👁️ RAJARAM EYE ACTIVE..."):
                try:
                    import google.generativeai as genai
                    img = Image.open(uploaded_file)
                    genai.configure(api_key=core.GEMINI_KEY)
                    g_model = genai.GenerativeModel("gemini-1.5-flash")
                    response = g_model.generate_content([prompt if prompt else "Analyze", img])
                    final_response = response.text
                    engine_id = "RAJARAM-EYE-OF-RA"
                except Exception as e: st.error(f"Vision Glitch: {e}")

        # --- MODULE 2: SEARCH & REASONING (TITAN BRAIN) ---
        if not final_response:
            with st.spinner("🧠 RAJARAM CORE REASONING..."):
                intel = ""
                if st.session_state.get('search_enabled') and any(k in prompt.lower() for k in ["news", "latest", "today", "who is"]):
                    try:
                        intel = core.search_engine.run(prompt)
                        engine_id = "RAJARAM-SATELLITE-WEB"
                    except: intel = "Satellite link weak."

                try:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    logic_res = loop.run_until_complete(rajaram_ai.execute_reasoning(prompt, str(intel)))
                    final_response, engine_id = logic_res if isinstance(logic_res, tuple) else (logic_res, "RAJARAM-SUPREME-LOGIC")
                except Exception as e:
                    final_response = "🔱 Core overload. Rebooting logic."
                    rajaram_shield.auto_fix("EXECUTION_ERROR", str(e))

        if final_response:
            st.markdown(final_response)
            st.caption(f"Engine: {engine_id} | Location: Bareilly-05 | Status: Immortal 🔱")
            if st.session_state.get('voice_enabled'): rajaram_ai.speak(final_response)
            st.session_state.history.append(AIMessage(content=final_response))

# 🔱 [PHASE 8: DYNAMIC SHAKTI LOADER]
def load_rajaram_features():
    for file in os.listdir():
        if file.startswith("feature_") and file.endswith(".py"):
            try:
                feature_name = file[:-3]
                spec = importlib.util.spec_from_file_location(feature_name, file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, 'run_feature'):
                    with st.container(border=True):
                        st.caption(f"🔱 ACTIVE POWER: {feature_name.upper()}")
                        module.run_feature()
            except Exception as e: st.error(f"Error loading {file}: {e}")

load_rajaram_features()
st.markdown("---")
st.caption("© 2026 RAJARAM AI - THE OMNIPOTENT CORE | BORN IN BAREILLY | BUILT FOR SUPREMACY")
