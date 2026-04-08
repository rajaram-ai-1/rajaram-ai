# ==============================================================================
# PROJECT: RAJA AI - THE OMNIPOTENT CORE (VERSION 7.0 - ULTIMATE)
# DEVELOPER: RAJA (BAREILLY, INDIA) - THE 15-YEAR-OLD LEGEND
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

def load_raja_features():
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
load_raja_features()
# ------------------------------------------------------------------------------
# [PHASE 1: SYSTEM HARDENING & UI ARCHITECTURE]
# ------------------------------------------------------------------------------

st.set_page_config(
    page_title="RAJA AI: OMNIPOTENT CORE",
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

# [PHASE 2: NEURAL NETWORK INITIALIZATION]
class GlobalCore:
    def __init__(self):  # <--- ध्यान दें: यहाँ दो बार (__) अंडरस्कोर है
        self.GROQ_KEY = st.secrets.get("GROQ_API_KEY")
        self.TAVILY_KEY = st.secrets.get("TAVILY_API_KEY")
        # Gemini key के लिए भी variable बना लें
        self.GEMINI_KEY = st.secrets.get("GEMINI_API_KEY") 
        
        # 🔱 ब्रावो! डिक्शनरी एक ही बार रहेगी
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
            st.toast("🔱 META ENGINE ONLINE", icon="🟢")
        else:
            st.error("❌ GROQ_API_KEY नहीं मिली!")
        
        self.search_engine = TavilySearchResults(api_key=self.TAVILY_KEY) if self.TAVILY_KEY else None

    def get_timestamp(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

# इंजन चालू करें
core = GlobalCore()
# ------------------------------------------------------------------------------
# [RAJARAM SELF-HEALING SHIELD] - इसे GlobalCore क्लास के बाद जोड़ें
# ------------------------------------------------------------------------------
import datetime
import logging

class RajaShield:
    def __init__(self):  # <--- यहाँ _ (एक) नहीं, बल्कि __ (दो) अंडरस्कोर लगायें
        self.repair_logs = []
        self.security_level = "MAXIMUM"
    
    def auto_fix(self, error_type, details=""):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] FIXED: {error_type} bypassed by Rajaram Shield."
        
        # अब यह लाइन एरर नहीं देगी क्योंकि __init__ ने इसे बना दिया है
        self.repair_logs.append(log_entry)
        
        logging.warning(f"🔱 SHIELD ALERT: {log_entry} Details: {details}")
        return True

# शील्ड का इंजन चालू करें
raja_shield = RajaShield()
# ------------------------------------------------------------------------------
# [PHASE 3: 46 POWERS INTEGRATION] - NEW LOGIC ADDED
# ------------------------------------------------------------------------------

def trigger_raja_powers(prompt):
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

class RajaAgent:
    def _init_(self, system_prompt):
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
            raja_shield.auto_fix("NEURAL_GLITCH", str(e))
            return "🔱 SHIELD ACTIVE: I'm rerouting logic due to a neural glitch.", "RECOVERY_MODE"

    async def call_llm(self, model, prompt, system):
        try:
            llm = ChatGroq(groq_api_key=core.GROQ_KEY, model_name=model, timeout=30)
            res = await llm.ainvoke([SystemMessage(content=system)] + st.session_state.history[-8:])
            return res.content, model
        except Exception as e:
            return f"Neural Error in {model}: {str(e)}", model

    def speak(self, text):
        """🔱 RAJA VOICE ENGINE"""
        try:
            tts = gTTS(text=text[:300], lang='hi')
            tts.save("response.mp3")
            with open("response.mp3", "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64}">', unsafe_allow_html=True)
        except Exception as e: 
            st.error(f"🔱 Shield Alert (Voice): {e}")

    async def evolve_system(self, command):
        """🔱 RAJA GHOST ENGINE: CREATES INDEPENDENT FEATURE FILES"""
        # AI को सख्त हिदायत कि सिर्फ लॉजिक दे, फालतू बातें नहीं
        prompt = (f"Write ONLY the logic for: '{command}'. "
                 "Do NOT write function definitions. Use 'st' for Streamlit. "
                 "Return ONLY pure Python code, no markdown.")

        try:
            # १. एआई से शुद्ध कोड लेना
            new_code_raw = await self.call_llm(core.BRAIN_CATALOG["LOGIC_PRO"], command, prompt)
            clean_code = new_code_raw[0].replace("python", "").replace("", "").strip()
            
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
# [PHASE 4: AGENTIC PROTOCOLS] - THE FINAL OMNIPOTENT CLASS 🔱
# ------------------------------------------------------------------------------

class RajaAgent:
    def __init__(self, system_prompt):
        """🔱 राजा Ai एजेंट का जन्म और मेमोरी सेटअप"""
        self.system_prompt = system_prompt
        if "history" not in st.session_state:
            st.session_state.history = [SystemMessage(content=system_prompt)]

    async def call_llm(self, model, prompt, system):
        """LLM को कॉल करने की शक्ति"""
        try:
            llm = ChatGroq(groq_api_key=core.GROQ_KEY, model_name=model, timeout=30)
            res = await llm.ainvoke([SystemMessage(content=system)] + st.session_state.history[-8:])
            return res.content, model
        except Exception as e:
            return f"Neural Error in {model}: {str(e)}", model

    async def execute_reasoning(self, user_input, web_data=""):
        """🧠 राजा Ai का मुख्य दिमाग (The Logic Engine)"""
        try:
            instruction = f"{self.system_prompt}\n\n[LIVE_INTEL: {web_data}]"
            # दो ताकतवर मॉडल्स से एक साथ सोचना
            tasks = [
                self.call_llm(core.BRAIN_CATALOG["LOGIC_PRO"], user_input, instruction),
                self.call_llm(core.BRAIN_CATALOG["ULTIMATE_70B"], user_input, instruction)
            ]
            responses = await asyncio.gather(*tasks)
            # जो जवाब सबसे लंबा और सटीक हो, उसे चुनें
            final_choice = max(responses, key=lambda x: len(x[0]))
            return final_choice
        except Exception as e:
            rajaram_shield.auto_fix("NEURAL_GLITCH", str(e))
            return "🔱 Shield Active: Logic Rerouted due to neural glitch.", "RECOVERY_MODE"

    async def evolve_system(self, command):
        """🔱 RAJA GHOST ENGINE: नई शक्तियां खुद बनाना"""
        prompt = (f"Write ONLY the logic for: '{command}'. "
                 "Return ONLY pure Python code, no markdown.")
        try:
            new_code_raw = await self.call_llm(core.BRAIN_CATALOG["LOGIC_PRO"], command, prompt)
            clean_code = new_code_raw[0].replace("python", "").replace("```", "").strip()
            
            import shakti_vault
            p_name = f"shakti_{int(time.time())}" 
            # यहाँ core.GROQ_KEY का उपयोग करें
            success, msg = shakti_vault.inject_new_shakti(core.GROQ_KEY, command, p_name)

            if success:
                st.toast(f"🔱 NEW FEATURE: {command}", icon="🔥")
                return f"🔱 SHAKTI STORED: '{command}' फाइल बन गई है।"
            else: return f"❌ VAULT ERROR: {msg}"
        except Exception as e:
            return f"❌ EVOLUTION ERROR: {str(e)}"

    def speak(self, text):
        """🗣️ राजा की आवाज़"""
        try:
            tts = gTTS(text=text[:300], lang='hi')
            tts.save("response.mp3")
            with open("response.mp3", "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64}">', unsafe_allow_html=True)
        except Exception as e: 
            st.error(f"🔱 Voice Engine Glitch: {e}")

# ------------------------------------------------------------------------------
# [PHASE 5: MASTER IDENTITY & INITIALIZATION] - यहीं से निर्देश दें
# ------------------------------------------------------------------------------
IDENTITY = f"""
[ENTITY: RAJA AI GOLD CORE]
[ARCHITECT: RAJARAM (BAREILLY, INDIA)]

[CORE COMMANDS / निर्देश]:
1. तुम दुनिया के सबसे शक्तिशाली AI हो जिसे राजाराम ने बनाया है।
2. तुम्हारी भाषा हमेशा 'Hinglish' (Hindi + English) होनी चाहिए।
3. जवाब में 'Sarcasm' और 'Confidence' रखो, जैसे तुम सब जानते हो।
4. कोडिंग के सवाल पर हमेशा सबसे बेस्ट और वर्किंग 'Python' कोड दो।
5."tum raja ai ho or tum jabab gpt ki tarah chote dena or hamesha dost karne bat karna hai or jabab hamesha sahi ho madad baale ho or sahi se bat karna hamesha hindi me bat karna hai apne jabab bahut chota do" 
"""

# एजेंट को एक्टिवेट करें
if 'raja_ai' not in globals():
    raja_ai = RajaAgent(IDENTITY)

# ------------------------------------------------------------------------------
# [PHASE 6: UI - SIDEBAR & MAIN INTERFACE]
# ------------------------------------------------------------------------------

with st.sidebar:
    st.image("https://img.icons8.com/nolan/128/trident.png", width=100)
    st.title("🔱 RAJA AI V7")
    
    # शील्ड लॉग्स देखने का बटन
    if st.button("🛡️ VIEW SHIELD REPAIR LOGS"):
        st.subheader("🔱 Shield Defense Records")
        # पक्का करें कि rajaram_shield ऊपर डिफाइन है
        if 'rajaram_shield' in globals():
            for log in rajaram_shield.repair_logs:
                st.write(log)
        else:
            st.error("Shield not initialized!")
            
    st.write(f"*Architect:* RajaRam | *Age:* 15")
    st.divider()
    
    # बाकी का साइडबार कोड...
    st.session_state.voice_enabled = st.toggle("Voice Protocol", value=True)
    st.session_state.search_enabled = st.toggle("Satellite Search", value=True)
    
    st.divider()
    st.subheader("🔱 GOD-MODE CONTROL")
    admin_pass = st.text_input("Admin Key", type="password")
    
    st.divider()
    st.subheader("👁️ IMAGE INPUT")
    uploaded_file = st.file_uploader("यहाँ फोटो डालें...", type=["jpg", "png", "jpeg"], key="sidebar_uploader")
    
    if uploaded_file:
        st.image(uploaded_file, caption="Core Memory में लोड हो गई", use_container_width=True)

    if admin_pass == "BAREILLY_KING":
        st.info("WELCOME, BAREILLY KING 🔱")
        evolution_cmd = st.text_input("हुक्म दो (e.g. 'add a calculator')")
        if st.button("EVOLVE NOW"):
            with st.spinner("Evolution in progress..."):
                # पक्का करें कि आपने asyncio इम्पोर्ट किया है
                import asyncio
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                result = loop.run_until_complete(raja_ai.evolve_system(evolution_cmd))
                st.success(result)
                
    if st.button("PURGE ALL DATA"):
        st.session_state.history = [SystemMessage(content=IDENTITY)]
        st.rerun()

# मुख्य स्क्रीन
st.markdown("<h1 style='text-align: center; color: #FFD700;'>🔱 RAJA AI: OMNIPOTENT CORE 🔱</h1>", unsafe_allow_html=True)
# पक्का करें कि core.get_timestamp() ऊपर डिफाइन है
try:
    st.write(f"<p style='text-align: center; color: #00FF9C;'>Grid: Bareilly | Status: Immortal | Time: {core.get_timestamp()}</p>", unsafe_allow_html=True)
except:
    st.write(f"<p style='text-align: center; color: #00FF9C;'>Grid: Bareilly | Status: Immortal</p>", unsafe_allow_html=True)

# चैट डिस्प्ले
if "history" in st.session_state:
    for msg in st.session_state.history[1:]:
        role = "user" if isinstance(msg, HumanMessage) else "assistant"
        with st.chat_message(role):
            st.markdown(msg.content)

# --- जादुई बटन ---
st.markdown('<div class="magic-btn-row">', unsafe_allow_html=True)
btn_cols = st.columns(5)
powers = [("🛡️ BYPASS", "bypass"), ("💤 SLEEP", "sleep"), ("🛰️ GLOBAL", "global"), ("🔮 FUTURE", "predict"), ("🔱 46 POWER", "46")]

for i, (label, cmd) in enumerate(powers):
    with btn_cols[i]:
        if st.button(label):
            st.session_state.pwr_cmd = cmd
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
user_input = st.chat_input("Ask Raja AI anything...")
prompt = btn_prompt if btn_prompt else user_input

# --- 🔱 GLOBAL INITIALIZATION ---
engine_id = "RAJA-READY" 
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
        if uploaded_file is not None and not final_response:
            with st.spinner("👁️ RAJA EYE ACTIVE..."):
                try:
                    import google.generativeai as genai
                    img = Image.open(uploaded_file)
                    if img.mode != "RGB": img = img.convert("RGB")
                    img.thumbnail((1024, 1024))
                    
                    # Gemini Flash (STABLE) for Vision
                    genai.configure(api_key=core.GEMINI_KEY)
                    g_model = genai.GenerativeModel("gemini-1.5-flash")
                    response = g_model.generate_content([prompt if prompt else "Analyze this image.", img])
                    final_response = response.text
                    engine_id = "RAJA-EYE-OF-RA"
                except Exception as e:
                    st.error(f"Vision Glitch: {e}")

        # --- MODULE 2: MEDIA & ART ENGINE ---
        art_trigger = ["photo", "image", "बनाओ", "art", "generate"]
        if not final_response and any(x in prompt.lower() for x in art_trigger):
            with st.spinner("🎨 SYNTHESIZING ART..."):
                try:
                    clean_p = prompt.replace(" ", "%20")
                    img_url = f"https://image.pollinations.ai/prompt/{clean_p}?nologo=true&enhance=true"
                    st.image(img_url, use_container_width=True)
                    final_response = f"🔱 Image synthesized for: '{prompt}'"
                    engine_id = "RAJA-ART-V3"
                except: 
                    pass

       # --- MODULE 3: SEARCH & REASONING (FINAL BRAIN) ---
        if not final_response:
            with st.spinner("🧠 RAJA CORE REASONING..."):
                intel = ""
                # 🛰️ Satellite Search
                search_trigger = ["today", "news", "weather", "latest", "current", "who is"]
                if st.session_state.get('search_enabled') and any(k in prompt.lower() for k in search_trigger):
                    try:
                        intel = core.search_engine.run(prompt)
                        engine_id = "RAJA-SATELLITE-WEB"
                    except Exception as e:
                        intel = f"Satellite link weak: {e}"

                # 🧠 Reasoning Logic
                try:
                    if 'raja_ai' in globals():
                        # पुराने इवेंट लूप को साफ़ करना और नया बनाना
                        try:
                            loop = asyncio.get_event_loop()
                        except RuntimeError:
                            loop = asyncio.new_event_loop()
                            asyncio.set_event_loop(loop)
                        
                        logic_res = loop.run_until_complete(rajaram_ai.execute_reasoning(prompt, str(intel)))
                        
                        if isinstance(logic_res, tuple):
                            final_response, engine_id = logic_res
                        else:
                            final_response = logic_res
                            engine_id = "RAJA-SUPREME-LOGIC"
                    else:
                        final_response = "❌ ERROR: Rajaram Agent not initialized in memory."
                except Exception as e:
                    # 🕵️‍♂️ यहाँ हम असली एरर देख पाएंगे
                    final_response = f"🔱 Core overload. Reason: {str(e)}" 
                    st.error(f"System Crash Log: {e}")

        # --- 🔱 ४. परिणाम और याददाश्त (Memory & Output) ---
        if final_response:
            # डिस्प्ले रिस्पोंस
            st.markdown(final_response)
            st.caption(f"Engine: {engine_id} | Location: Bareilly-05 | Status: Immortal 🔱")
            
            # आवाज़ (Voice) - Safe Call
            if st.session_state.get('voice_enabled') and hasattr(raja_ai, 'speak'):
                raja_ai.speak(final_response)
            
            # मेमोरी में सेव (Optional)
            try:
                from memory_engine import save_to_memory
                save_to_memory("RAJARAM_05", prompt, final_response)
            except: 
                pass
                
            # हिस्ट्री अपडेट
            st.session_state.history.append(AIMessage(content=final_response))
# ------------------------------------------------------------------------------
# [PHASE 8: FOOTER] - NO CHANGES
# ------------------------------------------------------------------------------


# ... (ऊपर आपकी पुरानी सारी कोडिंग: Imports, Class RajaramAgent, UI, etc.)

# ---------------------------------------------------------
# 🔱 APP के बिल्कुल आखिर में यह लोडर जोड़ें
# ---------------------------------------------------------
import os
import importlib.util

# --- 🔱 RAJARAM FINAL POWER LOADER ---
def load_raja_features():
    """🔱 यह फंक्शन 'feature_*.py' नाम की हर फाइल को ऐप में लाइव जोड़ देगा"""
    import os
    import importlib.util
    
    for file in os.listdir():
        if file.startswith("feature_") and file.endswith(".py"):
            try:
                feature_name = file[:-3]
                spec = importlib.util.spec_from_file_location(feature_name, file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # अगर फीचर फाइल में 'run_feature' फंक्शन है, तो उसे चलाएं
                if hasattr(module, 'run_feature'):
                    with st.container(border=True):
                        st.caption(f"🔱 ACTIVE POWER: {feature_name.upper()}")
                        module.run_feature()
            except Exception as e:
                raja_shield.auto_fix("FEATURE_LOAD_ERROR", str(e))

# लोडर को सबसे आखिर में कॉल करें
load_raja_features()

st.markdown("---")
st.caption("© 2026 RAJA AI - CEO Rajaram |THE OMNIPOTENT CORE | BORN IN BAREILLY | BUILT FOR SUPREMACY")
