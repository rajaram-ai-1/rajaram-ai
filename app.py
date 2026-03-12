# ==============================================================================
# PROJECT: RAJARAM AI - THE OMNIPOTENT CORE (VERSION 7.0 - ULTIMATE)
# DEVELOPER: RAJARAM (BAREILLY, INDIA) - THE 15-YEAR-OLD LEGEND
# STATUS: 46 SHAKTI FULLY INTEGRATED | NO CODE DELETED
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
import ast       # कोड को स्कैन करने के लिए (दिमाग)
import logging   # गलतियों का रिकॉर्ड रखने के लिए (डायरी)
import requests  # इंटरनेट से डेटा खींचने के लिए (हाथ-पैर)
import streamlit as st
# 🔱 तिजोरी से सारी शक्तियों को बुलाना
try:
    import shakti_vault
    from shakti_vault import *
except:
    pass
import importlib.util

def load_rajaram_features():
    """🔱 बाहर की सभी 'feature_*.py' फाइलों को लाइव करना"""
    for file in os.listdir():
        if file.startswith("feature_") and file.endswith(".py"):
            try:
                feature_name = file[:-3]
                spec = importlib.util.spec_from_file_location(feature_name, file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # अगर फाइल में 'run_feature' फंक्शन है, तो उसे चलाओ
                if hasattr(module, 'run_feature'):
                    module.run_feature()
            except Exception as e:
                st.error(f"Error loading {file}: {e}")

# --- इसे अपने UI के आखिर में या जहाँ आप बटन चाहते हैं वहां कॉल करें ---
load_rajaram_features()
# ------------------------------------------------------------------------------
# [PHASE 1: SYSTEM HARDENING & UI ARCHITECTURE]
# ------------------------------------------------------------------------------

st.set_page_config(
    page_title="RAJARAM AI: OMNIPOTENT CORE",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# राजाराम भाई का सिग्नेचर गोल्ड और साइबरपंक लुक
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;500&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #050505;
        color: #00FF9C;
        font-family: 'Fira Code', monospace;
    }
    
    /* जादुई बटन जो चैटबॉक्स के अंदर लगेंगे */
    .magic-btn-row {
        display: flex;
        gap: 10px;
        justify-content: center;
        margin-bottom: -45px;
        z-index: 1000;
        position: relative;
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
    
    .stSidebar {
        background-color: #000000 !important;
        border-right: 2px solid #FFD700;
    }

    .stButton>button {
        background: linear-gradient(45deg, #FFD700, #B8860B);
        color: black;
        border: none;
        border-radius: 20px;
        font-weight: bold;
        font-size: 11px;
    }
    .stButton>button:hover {
        transform: scale(1.1);
        box-shadow: 0 0 20px #FFD700;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# [PHASE 2: NEURAL NETWORK INITIALIZATION] - ALL YOUR BRAINS PROTECTED
# ------------------------------------------------------------------------------

class GlobalCore:
    def __init__(self):
        self.GROQ_KEY = st.secrets.get("GROQ_API_KEY")
        self.TAVILY_KEY = st.secrets.get("TAVILY_API_KEY")
        
        # यहाँ साड़ी 40+ मॉडल्स की लिस्ट और KeyErrors का समाधान
        self.BRAIN_CATALOG = {
            self.BRAIN_CATALOG = {
    # 🔱 द अल्टीमेट गॉड: मेटा का सबसे बड़ा मॉडल (405 बिलियन पैरामीटर्स)
    "THE_TITAN": "llama-3.1-405b-reasoning", 
    
    # 🔱 द सुप्रीम कमांडर: सबसे तेज़ और बुद्धिमान (70 बिलियन - लेटेस्ट)
    "ULTIMATE_70B": "llama-3.3-70b-versatile",
    "LOGIC_PRO": "llama-3.3-70b-versatile",
    
    # 🔱 द विजनरी: फोटो देखने के लिए मेटा का सबसे शक्तिशाली चश्मा
    "EYE_OF_RA": "llama-3.2-90b-vision-preview", 
    "FLASH_VISION": "llama-3.2-11b-vision-preview",
    
    # 🔱 द कोडर: प्रोग्रामिंग के लिए मेटा का स्पेशल मॉडल
    "CODE_WIZARD": "llama-3.3-70b-versatile", # या आप deepseek-v3 रख सकते हैं
    "CYBER_EXPERT": "llama-3.3-70b-versatile", 
    
    # 🔱 द मैथमेटिशियन: गणना के लिए
    "MATH_GENIUS": "qwen-2.5-72b-instruct" # Qwen गणित में बहुत तगड़ा है, इसे रहने दें
}
        }

       # --- सुधरा हुआ कोड (Google की छुट्टी) ---
        if self.GROQ_KEY:
            # अब हम यहाँ किसी genai.configure की ज़रूरत नहीं रखते
            # क्योंकि ChatGroq अपने आप Key उठा लेता है
            st.toast("🔱 META ENGINE ONLINE", icon="🟢")
        else:
            st.error("❌ GROQ_API_KEY नहीं मिली! साम्राज्य खतरे में है।")
        
        self.search_engine = TavilySearchResults(api_key=self.TAVILY_KEY) if self.TAVILY_KEY else None

    def get_timestamp(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

core = GlobalCore()
# ------------------------------------------------------------------------------
# [RAJARAM SELF-HEALING SHIELD] - इसे GlobalCore क्लास के बाद जोड़ें
# ------------------------------------------------------------------------------
class RajaramShield:
    def __init__(self):
        self.repair_logs = []
    
    def auto_fix(self, error_type, details=""):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] FIXED: {error_type} bypassed by Rajaram Shield."
        self.repair_logs.append(log_entry)
        logging.warning(f"🔱 SHIELD ALERT: {log_entry} Details: {details}")
        return True

# शील्ड का इंजन चालू करें
rajaram_shield = RajaramShield()
# ------------------------------------------------------------------------------
# [PHASE 3: 46 POWERS INTEGRATION] - NEW LOGIC ADDED
# ------------------------------------------------------------------------------

def trigger_rajaram_powers(prompt):
    p = prompt.lower()
    active_shaktis = []
    
    # आपकी 46 शक्तियों का लॉजिक यहाँ है
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
        if key in p:
            active_shaktis.append(val)
    return active_shaktis

# ------------------------------------------------------------------------------
# [PHASE 4: AGENTIC PROTOCOLS] - GHOST VAULT INTEGRATED 🔱
# ------------------------------------------------------------------------------

class RajaramAgent:
    def __init__(self, system_prompt):
        self.system_prompt = system_prompt
        if "history" not in st.session_state:
            st.session_state.history = [SystemMessage(content=system_prompt)]

    async def execute_reasoning(self, user_input, web_data=""):
        try:
            instruction = f"{self.system_prompt}\n\n[LIVE_INTEL: {web_data}]"
            tasks = [
                self.call_llm(core.BRAIN_CATALOG["LOGIC_PRO"], user_input, instruction),
                self.call_llm(core.BRAIN_CATALOG["ULTIMATE_70B"], user_input, instruction)
            ]
            responses = await asyncio.gather(*tasks)
            final_choice = max(responses, key=lambda x: len(x[0]))
            return final_choice
        except Exception as e:
            rajaram_shield.auto_fix("NEURAL_GLITCH", str(e))
            return "🔱 SHIELD ACTIVE: I'm rerouting logic due to a neural glitch.", "RECOVERY_MODE"

    async def call_llm(self, model, prompt, system):
        try:
            llm = ChatGroq(groq_api_key=core.GROQ_KEY, model_name=model, timeout=30)
            res = await llm.ainvoke([SystemMessage(content=system)] + st.session_state.history[-8:])
            return res.content, model
        except Exception as e:
            return f"Neural Error in {model}: {str(e)}", model

    def speak(self, text):
        """🔱 RAJARAM VOICE ENGINE"""
        try:
            tts = gTTS(text=text[:300], lang='hi')
            tts.save("response.mp3")
            with open("response.mp3", "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64}">', unsafe_allow_html=True)
        except Exception as e: 
            st.error(f"🔱 Shield Alert (Voice): {e}")

    async def evolve_system(self, command):
        """🔱 RAJARAM GHOST ENGINE: CREATES INDEPENDENT FEATURE FILES"""
        # AI को सख्त हिदायत कि सिर्फ लॉजिक दे, फालतू बातें नहीं
        prompt = (f"Write ONLY the logic for: '{command}'. "
                 "Do NOT write function definitions. Use 'st' for Streamlit. "
                 "Return ONLY pure Python code, no markdown.")

        try:
            # १. एआई से शुद्ध कोड लेना
            new_code_raw = await self.call_llm(core.BRAIN_CATALOG["LOGIC_PRO"], command, prompt)
            clean_code = new_code_raw[0].replace("```python", "").replace("```", "").strip()
            
            # --- २. तिजोरी (Vault) के जरिए नई फाइल बनवाना (FIXED) ---
            import shakti_vault
            import time

            # एक यूनिक नाम बनाना ताकि फाइलें आपस में न टकराएं
            p_name = f"shakti_{int(time.time())}" 

            # यहाँ हमने ३ चीजें भेजी हैं: १. api_key, २. command, ३. p_name
            # नोट: पक्का कर लें कि api_key ऊपर कहीं डिफाइन है
            success, msg = shakti_vault.inject_new_shakti(api_key, command, p_name)

            if success:
                st.success(msg)
                time.sleep(1)
                st.rerun()
            else:
                st.error(f"तिजोरी एरर: {msg}")

        except Exception as e:
            # यह 'except' ब्लॉक Syntax Error को खत्म करेगा
            st.error(f"⚠️ गड़बड़ हुई मालिक: {e}")
        
            if success:
                st.toast(f"🔱 NEW FEATURE GENERATED: {command}", icon="🔥")
                return f"🔱 SHAKTI STORED: '{command}' के लिए नई फाइल बन गई है। GitHub Refresh करें और Reboot करें!"
            else:
                return "❌ VAULT WRITE FAILURE: फाइल नहीं बन पाई।"
        except Exception as e:
            return f"❌ EVOLUTION ERROR: {str(e)}"
# ------------------------------------------------------------------------------
# [PHASE 5: MASTER IDENTITY]
# ------------------------------------------------------------------------------

IDENTITY = f"""
[ENTITY: RAJARAM AI GOLD CORE]
[ARCHITECT: RAJARAM, THE BAREILLY PRODIGY]
[MISSION: GLOBAL DOMINANCE & 46 POWERS EXECUTION]
[PROTOCOL: HINGLISH SARCASM & SUPREME INTEL]
"""

rajaram_ai = RajaramAgent(IDENTITY)
# ------------------------------------------------------------------------------
# [PHASE 6: UI - SIDEBAR & MAIN INTERFACE] - FIXED INDENTATION
# ------------------------------------------------------------------------------

with st.sidebar:
    st.image("https://img.icons8.com/nolan/128/trident.png", width=100)
    st.title("🔱 RAJARAM AI V7")
    
    # शील्ड लॉग्स देखने का बटन
    if st.button("🛡️ VIEW SHIELD REPAIR LOGS"):
        st.subheader("🔱 Shield Defense Records")
        for log in rajaram_shield.repair_logs:
            st.write(log)
            
    st.write(f"**Architect:** Rajaram | **Age:** 15")
    st.divider()
    
    # प्रोटोकॉल टोल्स
    st.session_state.voice_enabled = st.toggle("Voice Protocol", value=True)
    st.session_state.search_enabled = st.toggle("Satellite Search", value=True)
    
    st.divider()
    st.subheader("🔱 GOD-MODE CONTROL")
    # पासवर्ड इनपुट
    admin_pass = st.text_input("Admin Key", type="password")
    
    st.divider()
    st.subheader("👁️ IMAGE INPUT")
    # फोटो अपलोडर (अब यह सही से साइडबार में रहेगा)
    uploaded_file = st.file_uploader("यहाँ फोटो डालें...", type=["jpg", "png", "jpeg"], key="sidebar_uploader")
    
    if uploaded_file:
        st.image(uploaded_file, caption="Core Memory में लोड हो गई", use_container_width=True)

    # एडमिन कंट्रोल (सिर्फ बरेली किंग के लिए)
    if admin_pass == "BAREILLY_KING":
        st.info("WELCOME, BAREILLY KING 🔱")
        evolution_cmd = st.text_input("हुक्म दो (e.g. 'add a calculator')")
        if st.button("EVOLVE NOW"):
            with st.spinner("Evolution in progress..."):
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
    with st.chat_message(role):
        st.markdown(msg.content)

# --- राजाराम भाई के जादुई बटन (चैटबॉक्स के ऊपर) ---
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

# ------------------------------------------------------------------------------
# [PHASE 7: EXECUTION LOGIC] - CLEAN & OPTIMIZED VERSION 🔱
# ------------------------------------------------------------------------------

# 1. जादुई बटनों का हुक्म पकड़ना
btn_prompt = None
if 'pwr_cmd' in st.session_state and st.session_state.pwr_cmd:
    btn_prompt = st.session_state.pwr_cmd
    st.session_state.pwr_cmd = None  

# 2. इनपुट हैंडलर (बटन या टाइपिंग)
user_input = st.chat_input("Ask Rajaram AI anything...")
prompt = btn_prompt if btn_prompt else user_input

# --- 🔱 GLOBAL INITIALIZATION ---
engine_id = "RAJARAM-READY" 
final_response = None  

# 3. एआई प्रोसेसिंग यूनिट शुरू
if prompt:
    # शक्तियों को चेक करें
    triggered = trigger_rajaram_powers(prompt)
    
    # यूजर मैसेज को डिस्प्ले और हिस्ट्री में सेव करें
    st.session_state.history.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # शक्तियों का स्टेटस दिखाओ
        for s in triggered:
            st.warning(s)

        # --- MODULE 1: RAJARAM HYBRID VISION ENGINE (IMAGE) ---
        if uploaded_file is not None:
            with st.spinner("👁️ RAJARAM EYE ACTIVE..."):
                try:
                    img = Image.open(uploaded_file)
                    if img.mode != "RGB": img = img.convert("RGB")
                    img.thumbnail((1024, 1024))
                    
                    # Gemini Flash (STABLE) for Vision
                    genai.configure(api_key=core.GEMINI_KEY)
                    g_model = genai.GenerativeModel("gemini-1.5-flash")
                    response = g_model.generate_content([prompt if prompt else "Analyze this image.", img])
                    final_response = response.text
                    engine_id = "RAJARAM-EYE-OF-RA"
                except Exception as e:
                    st.error(f"Vision Glitch: {e}")

        # --- MODULE 2: MEDIA & ART ENGINE ---
        if not final_response and any(x in prompt.lower() for x in ["photo", "image", "बनाओ", "art"]):
            with st.spinner("🎨 SYNTHESIZING ART..."):
                try:
                    clean_p = prompt.replace(" ", "%20")
                    img_url = f"https://image.pollinations.ai/prompt/{clean_p}?nologo=true&enhance=true"
                    st.image(img_url, use_container_width=True)
                    final_response = "🔱 Image synthesized by Rajaram AI Core."
                    engine_id = "RAJARAM-ART-V3"
                except: pass

        # --- MODULE 3: SEARCH & REASONING (FINAL BRAIN) ---
        if not final_response:
            with st.spinner("🧠 RAJARAM CORE REASONING..."):
                intel = ""
                # 🛰️ Satellite Search
                search_trigger = ["today", "news", "weather", "latest", "current", "who is"]
                if st.session_state.get('search_enabled') and any(k in prompt.lower() for k in search_trigger):
                    try:
                        intel = core.search_engine.run(prompt)
                        engine_id = "RAJARAM-SATELLITE-WEB"
                    except:
                        intel = "Satellite link weak."

                # 🧠 Reasoning Logic
                try:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    logic_res = loop.run_until_complete(rajaram_ai.execute_reasoning(prompt, str(intel)))
                    
                    if isinstance(logic_res, tuple):
                        final_response, engine_id = logic_res
                    else:
                        final_response = logic_res
                        engine_id = "RAJARAM-SUPREME-LOGIC"
                except Exception as e:
                    final_response = "🔱 Core overload. Please retry."
                    st.error(f"Logic Error: {e}")

        # --- 🔱 ४. परिणाम और याददाश्त (Memory & Output) ---
        if final_response:
            st.markdown(final_response)
            st.caption(f"Engine: {engine_id} | Location: Bareilly-05 | Status: Immortal 🔱")
            
            # आवाज़ (Voice)
            if st.session_state.get('voice_enabled'):
                rajaram_ai.speak(final_response)
            
            # मेमोरी में सेव (Optional)
            try:
                from memory_engine import save_to_memory
                save_to_memory("RAJARAM_05", prompt, final_response)
            except: pass
                
            # हिस्ट्री अपडेट
            st.session_state.history.append(AIMessage(content=final_response))
# ------------------------------------------------------------------------------
# [PHASE 8: FOOTER] - NO CHANGES
# ------------------------------------------------------------------------------
st.markdown("---")
st.caption("© 2026 RAJARAM AI - THE OMNIPOTENT CORE | BORN IN BAREILLY | BUILT FOR SUPREMACY")

# ... (ऊपर आपकी पुरानी सारी कोडिंग: Imports, Class RajaramAgent, UI, etc.)

# ---------------------------------------------------------
# 🔱 APP के बिल्कुल आखिर में यह लोडर जोड़ें
# ---------------------------------------------------------
import os
import importlib.util

def load_rajaram_features():
    """🔱 यह फंक्शन 'feature_*.py' नाम की हर फाइल को ऐप में जोड़ देगा"""
    for file in os.listdir():
        if file.startswith("feature_") and file.endswith(".py"):
            try:
                feature_name = file[:-3]
                spec = importlib.util.spec_from_file_location(feature_name, file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # अगर फीचर फाइल में 'run_feature' फंक्शन है, तो उसे चलाएं
                if hasattr(module, 'run_feature'):
                    # यह स्क्रीन पर एक सुंदर बॉक्स बना देगा
                    with st.container(border=True):
                        st.caption(f"🔱 ACTIVE POWER: {feature_name.upper()}")
                        module.run_feature()
            except Exception as e:
                st.error(f"❌ Error loading {file}: {e}")

# लोडर को कॉल करें
load_rajaram_features()
