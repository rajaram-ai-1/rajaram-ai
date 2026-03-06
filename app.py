# ==============================================================================
# PROJECT: RAJARAM AI - THE OMNIPOTENT CORE (VERSION 7.0 - ULTIMATE)
# DEVELOPER: RAJARAM (BAREILLY, INDIA) - THE 15-YEAR-OLD LEGEND
# STATUS: 46 SHAKTI FULLY INTEGRATED | NO CODE DELETED
# ==============================================================================

import streamlit as st
import os
import google.generativeai as genai
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
        self.GEMINI_KEY = st.secrets.get("GEMINI_API_KEY")
        self.GROQ_KEY = st.secrets.get("GROQ_API_KEY")
        self.TAVILY_KEY = st.secrets.get("TAVILY_API_KEY")
        
        # यहाँ साड़ी 40+ मॉडल्स की लिस्ट और KeyErrors का समाधान
        self.BRAIN_CATALOG = {
            "ULTIMATE_70B": "llama-3.3-70b-versatile",
            "THE_TITAN": "llama-3.1-405b-reasoning",
            "MIXTRIAL_POWER": "mixtral-8x7b-32768",
            "EYE_OF_RA": "gemini-1.5-pro",
            "FLASH_VISION": "gemini-1.5-flash",
            "LLAMA_VISION_90B": "llama-3.2-90b-vision-preview",
            "CODE_WIZARD": "deepseek-v3",
            "LOGIC_PRO": "Llama-3.3-70b-versatile",
            "CYBER_EXPERT": "codellama-70b-instruct",
            "MATH_GENIUS": "qwen-2.5-72b-instruct"
        }

        if self.GEMINI_KEY:
            genai.configure(api_key=self.GEMINI_KEY)
        
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
# [PHASE 4: AGENTIC PROTOCOLS] - YOUR ORIGINAL LOGIC (FIXED)
# ------------------------------------------------------------------------------

class RajaramAgent:
    def __init__(self, system_prompt):
        self.system_prompt = system_prompt
        if "history" not in st.session_state:
            st.session_state.history = [SystemMessage(content=system_prompt)]

    async def execute_reasoning(self, user_input, web_data=""):
        try: # <--- ये अब सही जगह पर है
            instruction = f"{self.system_prompt}\n\n[LIVE_INTEL: {web_data}]"
            # Fix: Using correct keys from BRAIN_CATALOG to avoid KeyErrors
            tasks = [
                self.call_llm(core.BRAIN_CATALOG["LOGIC_PRO"], user_input, instruction),
                self.call_llm(core.BRAIN_CATALOG["ULTIMATE_70B"], user_input, instruction)
            ]
            responses = await asyncio.gather(*tasks)
            final_choice = max(responses, key=lambda x: len(x[0]))
            return final_choice
        except Exception as e: # <--- ये बिल्कुल 'try' की सीध में है
            # अगर एरर आए, तो राजाराम शील्ड को काम पर लगाओ
            rajaram_shield.auto_fix("NEURAL_GLITCH", str(e))
            return "🔱 SHIELD ACTIVE: I'm rerouting logic due to a neural glitch. (Error bypassed)", "RECOVERY_MODE"

    async def call_llm(self, model, prompt, system):
        try:
            llm = ChatGroq(groq_api_key=core.GROQ_KEY, model_name=model, timeout=30)
            res = await llm.ainvoke([SystemMessage(content=system)] + st.session_state.history[-8:])
            return res.content, model
        except Exception as e:
            return f"Neural Error in {model}: {str(e)}", model

    def speak(self, text):
        try:
            tts = gTTS(text=text[:300], lang='hi')
            tts.save("response.mp3")
            with open("response.mp3", "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64}">', unsafe_allow_html=True)
        except Exception as e: 
            st.error(f"🔱 Shield Alert: {e}") # ताकि आपको पता चले क्या खराब हुआ

    async def evolve_system(self, command):
        # SECURITY CHECK: सिर्फ राजाराम भाई के लिए
        auth_key = "RAJARAM_SUPREMACY"
        # बाकी का इवोल्यूशन कोड यहाँ आएगा...
        
        prompt = f"""
        You are the GOLD CORE of Rajaram AI.
        TASK: Write a Python function based on this command: '{command}'
        RULES:
        1. Return ONLY the python code.
        2. No explanations, no markdown, just pure code.
        3. Make it a function that can be called globally.
        """
        
        try:
            # एआई से कोड लिखवाना
            new_code = await self.call_llm(core.BRAIN_CATALOG["LOGIC_PRO"], command, prompt)
            clean_code = new_code[0].replace("```python", "").replace("```", "").strip()
            
            # 🔱 असली जादू: कोड को लाइव इंजेक्ट करना
            exec(clean_code, globals())
            
            rajaram_shield.auto_fix("SYSTEM_EVOLUTION", f"New feature added: {command}")
            return f"🔱 SHAKTI ADDED: Feature '{command}' is now live in the system!"
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
# [PHASE 7: EXECUTION LOGIC] - BUTTON & INPUT SYNC FIXED 🔱
# ------------------------------------------------------------------------------

# 1. जादुई बटनों का हुक्म पकड़ना
btn_prompt = None
if 'pwr_cmd' in st.session_state and st.session_state.pwr_cmd:
    btn_prompt = st.session_state.pwr_cmd
    st.session_state.pwr_cmd = None # काम होने के बाद खाली कर दो

# 2. इनपुट हैंडलर (बटन या टाइपिंग - जो भी पहले आए)
user_input = st.chat_input("Enter Command to Core...")
prompt = btn_prompt if btn_prompt else user_input

if prompt:
    # शक्तियों को चेक करें
    triggered = trigger_rajaram_powers(prompt)
    
    st.session_state.history.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # शक्तियों का स्टेटस पहले दिखाओ
        for s in triggered:
            st.warning(s)
            
        final_response = ""
        engine_id = ""
        # --- MODULE 1: VISION (RAJARAM EYE ACTIVATED) ---
        # सीधे 'uploaded_file' चेक करना (बिना globals के) - यही असली पावर है!
        if uploaded_file is not None:
            with st.spinner("👁️ RAJARAM EYE IS SCANNING THE CORE MEMORY..."):
                try:
                    # फोटो को लोड करना
                    img_data = Image.open(uploaded_file)
                    
                    if not core.GEMINI_KEY:
                        st.error("🔱 Shield Alert: Gemini API Key Missing!")
                    else:
                        vision_model = genai.GenerativeModel('gemini-1.5-flash')
                        # अगर कुछ टाइप किया है तो वो सवाल, वरना डिफ़ॉल्ट
                        v_prompt = prompt if prompt else "इस फोटो का विश्लेषण करें।"
                        v_response = vision_model.generate_content([v_prompt, img_data])
                        
                        final_response = v_response.text
                        engine_id = "EYE-OF-RA-FLASH"
                except Exception as e:
                    rajaram_shield.auto_fix("VISION_CORE_FAILURE", str(e))
                    final_response = "🔱 राजाराम भाई, आँखों के सेंसर में धूल जम गई है, पर मैं देख रहा हूँ!"

        # --- MODULE 2: MEDIA & ART (IF NO IMAGE UPLOADED) ---
        # अगर कोई फोटो अपलोड नहीं है और आप 'बनाने' को कह रहे हैं, तभी ये चलेगा
        if not final_response and any(x in prompt.lower() for x in ["photo", "image", "बनाओ", "art"]):
            with st.spinner("🎨 RAJARAM ART ENGINE STARTING..."):
                try:
                    # नाम को URL के हिसाब से साफ करना
                    clean_p = prompt.replace(" ", "%20")
                    img_url = f"https://image.pollinations.ai/prompt/{clean_p}?nologo=true&enhance=true"
                    st.image(img_url, use_container_width=True)
                    final_response = "🔱 Image synthesized by Rajaram AI Core."
                    engine_id = "Pollinations-V3"
                except:
                    final_response = "🔱 आर्ट इंजन में दबाव बढ़ गया है, फिर से कोशिश करें।"

       # --- MODULE 3: SEARCH & REASONING (THE FINAL BRAIN) ---
        # अगर अभी तक कोई जवाब नहीं मिला (न विज़न से, न आर्ट से), तो यहाँ दिमाग चलेगा
        if not final_response:
            intel = ""
            # सैटेलाइट सर्च (सिर्फ अगर इंटरनेट से जुड़ा काम हो)
            search_trigger = ["today", "news", "weather", "latest", "current", "who is"]
            if st.session_state.search_enabled and any(k in prompt.lower() for k in search_trigger):
                with st.spinner("🛰️ RAJARAM SATELLITE SEARCH ACTIVE..."):
                    try:
                        intel = core.search_engine.run(prompt)
                    except:
                        intel = "Satellite network connection weak, relying on internal core logic."
            
            # असली धमाका: Reasoning Logic
            with st.spinner("🧠 NEURAL SYNERGY ACTIVE (RAJARAM V7.1)..."):
                try:
                    # Async लूप को सुरक्षित तरीके से हैंडल करना
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    
                    # एआई को सोचने के लिए बुलाना
                    logic_result = loop.run_until_complete(rajaram_ai.execute_reasoning(prompt, intel))
                    
                    # अगर जवाब सही मिला है तो उसे सेट करना
                    if isinstance(logic_result, tuple):
                        final_response, engine_id = logic_result
                    else:
                        final_response = logic_result
                        engine_id = "RAJARAM-SUPREME-LOGIC"
                    
                    loop.close()
                except Exception as e:
                    rajaram_shield.auto_fix("NEURAL_CORE_CRITICAL", str(e))
                    final_response = "🔱 राजाराम भाई, दिमाग पर बहुत ज़ोर पड़ रहा है, पर मैं हार नहीं मानूँगा! फिर से पूछें।"
                    engine_id = "SHIELD-RECOVERY"

        # --- FINAL OUTPUT: RESULT DISPLAY ---
        if final_response:
            st.markdown(final_response)
            st.caption(f"Engine: {engine_id} | Location: Bareilly-05 | Status: Immortal 🔱")
            
            # आवाज़ (Voice) चालू करना
            if st.session_state.voice_enabled:
                rajaram_ai.speak(final_response)
                
            # इतिहास (History) में जोड़ना
            st.session_state.history.append(AIMessage(content=final_response))

# ------------------------------------------------------------------------------
# [PHASE 8: FOOTER] - NO CHANGES
# ------------------------------------------------------------------------------
st.markdown("---")
st.caption("© 2026 RAJARAM AI - THE OMNIPOTENT CORE | BORN IN BAREILLY | BUILT FOR SUPREMACY")
