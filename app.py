

import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from gtts import gTTS
import base64
import asyncio
import time
import datetime
import json
from PIL import Image
from io import BytesIO
import streamlit as st

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
        self.GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
        # Gemini key के लिए भी variable बना लें
        self.GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY") 
        
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

        if self.GROQ_API_KEY:
            st.toast("🔱 Raja Ai is Active", icon="🟢")
        else:
            st.error("❌ GROQ_API_KEY नहीं मिली!")

    def get_timestamp(self):
        return datetime.datetime.now().strftime("%H:%M:%S")
core = GlobalCore() # यह एआई के दिमाग (Models) को लोड करेगा
# ==============================================================================
# [PHASE 2.5: THE OMNISCIENT EYE - SEARCH & VISION TOOLS]
# ==============================================================================
import datetime
import logging

class RajaShield:
    def __init__(self):  # <--- यहाँ _ (एक) नहीं, बल्कि __ (दो) अंडरस्कोर लगायें
        self.repair_logs = []
        self.security_level = "MAXIMUM"
    
    def auto_fix(self, error_type, details=""):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] FIXED: {error_type} bypassed by Raja Shield."
        
        # अब यह लाइन एरर नहीं देगी क्योंकि __init__ ने इसे बना दिया है
        self.repair_logs.append(log_entry)
        
        logging.warning(f"🔱 SHIELD ALERT: {log_entry} Details: {details}")
        return True

# शील्ड का इंजन चालू करें
raja_shield = RajaShield()
# ------------------------------------------------------------------------------
# [PHASE 3: 46 POWERS INTEGRATION] - NEW LOGIC ADDED
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# [PHASE 4: AGENTIC PROTOCOLS] - GHOST VAULT INTEGRATED 🔱
# ------------------------------------------------------------------------------

class RajaAgent:
    def __init__(self, system_prompt):
        """🔱 राजा Ai की याददाश्त और पहचान सेटअप"""
        self.system_prompt = system_prompt
        if "history" not in st.session_state:
            st.session_state.history = [SystemMessage(content=system_prompt)]

    async def raja_router(self, user_input):
        """🔱 MASTER ROUTER: यह तय करेगा कि कौन सी शक्ति इस्तेमाल करनी है"""
        try:
            p = user_input.lower()
            
            # --- [FORCE OVERRIDE: हैकर की पहली शक्ति] ---
            # अगर ये शब्द मैसेज में हैं, तो एआई से पूछना ही नहीं है, सीधा SEARCH करना है
            search_keywords = ["सोना", "gold", "price", "bhav", "rate", "weather", "mausam", "news", "खबर", "आज का"]
            if any(word in p for word in search_keywords):
                return "SEARCH"

            # अगर फोटो की बात हो रही है
            vision_keywords = ["photo", "image", "dekho", "image", "pic", "फोटो"]
            if any(word in p for word in vision_keywords):
                return "VISION"

            # --- [LLM DECISION: बाकी सब के लिए] ---
            router_prompt = f"""
            User input: "{user_input}"
            Return ONLY one word based on intent:
            - VISION (if it's about seeing an image)
            - SEARCH (if it's about current real-world facts)
            - BRAIN (for conversation, logic, or code)
            Result:"""
            
            res, _ = await self.call_llm("llama-3.2-11b-vision-preview", router_prompt, "Decision Router")
            
            cleaned_res = res.upper()
            if "VISION" in cleaned_res: return "VISION"
            if "SEARCH" in cleaned_res: return "SEARCH"
            return "BRAIN"
            
        except Exception as e:
            # अगर राउटर फेल हुआ, तो डिफ़ॉल्ट ब्रेन पर जाओ
            return "BRAIN"
            
            res, _ = await self.call_llm("llama-3.2-11b-vision-preview", router_prompt, "Decision Router")
            # --- [फिक्स: सिर्फ मुख्य शब्द उठाना] ---
            cleaned_res = res.upper()
            if "VISION" in cleaned_res: return "VISION"
            if "SEARCH" in cleaned_res: return "SEARCH"
            return "BRAIN"
        except:
            return "BRAIN"

    async def execute_reasoning(self, user_input, web_data=""):
        """🧠 राजा Ai का मुख्य दिमाग (Dual-Model Logic)"""
        try:
            # --- [फिक्स: वेब डेटा को प्रॉम्ट में सबसे ऊपर रखना] ---
            if web_data:
                full_input = f"LIVE_INTEL FROM INTERNET:\n{web_data}\n\nUSER_QUESTION: {user_input}"
            else:
                full_input = user_input

            instruction = self.system_prompt
            
            tasks = [
                self.call_llm(core.BRAIN_CATALOG["LOGIC_PRO"], full_input, instruction),
                self.call_llm(core.BRAIN_CATALOG["ULTIMATE_70B"], full_input, instruction)
            ]
            responses = await asyncio.gather(*tasks)
            final_choice = max(responses, key=lambda x: len(x[0]))
            return final_choice
        except Exception as e:
            raja_shield.auto_fix("NEURAL_GLITCH", str(e))
            return "🔱 SHIELD ACTIVE: I'm rerouting logic due to a neural glitch.", "RECOVERY_MODE"

    async def call_llm(self, model, prompt, system):
        """⚡ GROQ INFRASTRUCTURE CALL"""
        try:
            llm = ChatGroq(groq_api_key=core.GROQ_API_KEY, model_name=model, timeout=30)
            # सिर्फ पिछले 8 मैसेज भेजना ताकि मेमोरी फुल न हो
            messages = [SystemMessage(content=system)] + st.session_state.history[-8:] + [HumanMessage(content=prompt)]
            res = await llm.ainvoke(messages)
            return res.content, model
        except Exception as e:
            return f"Neural Error: {str(e)}", model

    def speak(self, text):
        # आपका पुराना gTTS कोड (एकदम सही है)
        try:
            tts = gTTS(text=text[:300], lang='hi')
            tts.save("response.mp3")
            with open("response.mp3", "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64}">', unsafe_allow_html=True)
        except: pass



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
5."tum raja ai ho or tum jabab gpt ki tarah chote dena or hamesha dost karne bat karna hai or jabab hamesha sahi ho madad baale ho or sahi se bat karna hamesha hindi me bat karna hai apne jabab bahut chota do or har tarah ki madad karna har jabab code me nahi dena hai jab koi code mange tabhi code diya karo jab bhi koi kuch bhi puche ya kuch sabal puche to ose bachcho ki tarah samjhana taki oske samjh me a jay or har cheez ko achche se batana galat jabab mat dena kabhi bhi hamesha sahi jabab dena
   ap hamesha yah dekho ki pahale sabal kya hai fir oske bad me sahi jabab do गणितीय सूत्रों के लिए Markdown या LaTeX का उपयोग करे। इससे * (गुणा) का निशान साफ dikhai de har nishan saf dikhai de aise karo chahe bah kisi ka nishan ho
   or hamesha jo jabab tum do osse juda ak sabal pucha karo जैसे ही कोई बटन दवाई तो उसको उस विषय को अच्छे से समझाना उसे बचाने   के तरीकों पर सलाह देना और लोगों की मदद करना
   हमेशा शुद्ध और सरल हिंदी में बात करना जब यूजर कहे तो इंग्लिश का उपयोग  करना ।" 
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
    
    if st.button("🛡️ VIEW SHIELD REPAIR LOGS"):
        st.subheader("🔱 Shield Defense Records")
        if 'raja_shield' in globals():
            for log in raja_shield.repair_logs:
                st.write(log)
        else:
            st.error("Shield not initialized!")
            
    st.write(f"*Architect:* RajaRam | *Age:* 15")
    st.divider()
    
    st.session_state.voice_enabled = st.toggle("Voice Protocol", value=True)
    st.session_state.search_enabled = st.toggle("Satellite Search", value=True)
                
    if st.button("PURGE ALL DATA"):
        if "history" in st.session_state:
            # IDENTITY को पक्का करें कि ऊपर डिफाइन है
            st.session_state.history = [SystemMessage(content=IDENTITY)]
        st.rerun()

# --- मुख्य स्क्रीन का शीर्षक ---
st.markdown("<h1 style='text-align: center; color: #FFD700;'>🔱 RAJA AI: OMNIPOTENT CORE 🔱</h1>", unsafe_allow_html=True)

try:
    st.write(f"<p style='text-align: center; color: #00FF9C;'>Grid: Bareilly | Status: Immortal | Time: {core.get_timestamp()}</p>", unsafe_allow_html=True)
except:
    st.write(f"<p style='text-align: center; color: #00FF9C;'>Grid: Bareilly | Status: Immortal</p>", unsafe_allow_html=True)

# --- शक्तियों का लॉजिक फंक्शन ---
def trigger_raja_powers(prompt):
    p = prompt.lower()
    active_shaktis = []
    
    powers_map = {
        "jal_jeevan": "💧 जल जीवन मिशन: पानी की हर बूंद कीमती है।",
        "dil_ki_baat": "❤️ दिल की बात: जीवन, वेद-पुराण और संस्कृति का ज्ञान।",
        "kheti": "🌾 कृषि शक्ति: उन्नत खेती और किसान मित्र मोड सक्रिय।",
        "skills": "📚 स्किल इंडिया: भविष्य के नए हुनर सीखें।",
        "predict": "🔮 भविष्य: आपके लक्ष्य का विश्लेषण सक्रिय।"
    }
    
    for key, val in powers_map.items():
        if key in p:
            active_shaktis.append(val)
            
    return active_shaktis

# --- जन सेवा केंद्र (बटन इंटरफेस) ---
st.markdown('<h3 style="text-align: center; color: #2E7D32;">🌱 RAJA AI: ज्ञान और सेवा केंद्र 🌱</h3>', unsafe_allow_html=True)

# बटन की लिस्ट
custom_powers = [
    ("💧 जल जीवन", "jal_jeevan"), 
    ("❤️ दिल की बात", "dil_ki_at"), 
    ("🌾 कृषि ज्ञान", "kheti"), 
    ("📚 न्यू स्किल्स", "skills"), 
    ("🔮 भविष्य", "predict")
]

cols = st.columns(5)
for i, (col, (label, k)) in enumerate(zip(cols, custom_powers)):
    if col.button(label, key=f"gen_sev_{k}_{i}"):
        st.session_state.prompt = f"ACTIVATE {k.upper()}"
        st.rerun()

# --- चैट डिस्प्ले ---
if "history" in st.session_state:
    for msg in st.session_state.history[1:]:
        from langchain_core.messages import HumanMessage
        role = "user" if isinstance(msg, HumanMessage) else "assistant"
        with st.chat_message(role):
            st.markdown(msg.content)
# ------------------------------------------------------------------------------
# [PHASE 7: EXECUTION LOGIC] - ANTI-LOOP VERSION 🔱
# ------------------------------------------------------------------------------


# १. इनपुट को संभालना
prompt = None
user_input = st.chat_input("🔱 Ask Raja Ai: Built for Supremacy")

if st.session_state.get("prompt"):
    prompt = st.session_state.prompt
    st.session_state.prompt = None 
elif user_input:
    prompt = user_input

# २. मुख्य प्रोसेसिंग यूनिट
if prompt:
    # --- [MASTER INITIALIZATION] ---
    if "raja_ai" not in st.session_state:
        st.session_state.raja_ai = RajaAgent(IDENTITY)
    
    raja_ai = st.session_state.raja_ai
    
    # यूजर का मैसेज हिस्ट्री में जोड़ना और दिखाना
    if "history" not in st.session_state:
        st.session_state.history = [SystemMessage(content=IDENTITY)]
        
    st.session_state.history.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(f"**You:** {prompt}")

    # एआई का जवाब (The Assistant Box)
    with st.chat_message("assistant"):
        final_response = None
        current_safe_prompt = prompt # प्रॉम्ट को सुरक्षित किया
        
        # 🔱 Loop Error Fix: असिस्टेंट के अंदर ही फ्रेश लूप सेटअप
        import asyncio
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        with st.spinner("🔱 RAJA AI शक्तियों का आह्वान कर रहा है..."):
            try:
                # [STEP 1: ROUTING]
                mode = loop.run_until_complete(raja_ai.raja_router(current_safe_prompt))
                
                # [STEP 2: EXECUTION PATHS]
                if mode == "SEARCH":
                    st.toast("🛰️ Satellite Scan Active", icon="🌐")
                    try:
                        from engine import raja_web_search
                        intel = raja_web_search(current_safe_prompt)
                    except ImportError:
                        intel = "Search engine.py file not found."
                    
                    logic_res = loop.run_until_complete(raja_ai.execute_reasoning(current_safe_prompt, intel))
                
                elif mode == "VISION" and 'uploaded_file' in locals() and uploaded_file is not None:
                    st.toast("👁️ Supreme Vision Activated", icon="🔥")
                    try:
                        from vision_module import raja_vision_engine
                        logic_res = raja_vision_engine(uploaded_file)
                    except ImportError:
                        logic_res = "Vision module file not found."
                
                else:
                    st.toast("🧠 Brain Processing", icon="⚡")
                    logic_res = loop.run_until_complete(raja_ai.execute_reasoning(current_safe_prompt, ""))

                # [STEP 3: FINAL OUTPUT]
                # अगर logic_res एक टुपल है (response, model), तो सिर्फ टेक्स्ट उठाओ
                final_response = logic_res[0] if isinstance(logic_res, (tuple, list)) else logic_res
                
                st.markdown(final_response)
                
                # आवाज़ और मेमोरी अपडेट
                if st.session_state.get('voice_enabled'):
                    raja_ai.speak(final_response)
                
                st.session_state.history.append(AIMessage(content=final_response))

            except Exception as e:
                error_msg = f"🔱 Shield Alert: Neural Link Reset. (Error: {str(e)})"
                st.error(error_msg)
                if 'raja_shield' in globals():
                    raja_shield.auto_fix("SUPREME_LOGIC_ERROR", str(e))
        
# ------------------------------------------------------------------------------
# [PHASE 8: FOOTER] - NO CHANGES
# ------------------------------------------------------------------------------


st.markdown("---")
st.caption("© 2026 RAJA AI - CEO Rajaram |THE OMNIPOTENT CORE | BORN IN BAREILLY | BUILT FOR SUPREMACY")
