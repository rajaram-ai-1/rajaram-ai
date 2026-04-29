

import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import time
import datetime
import json
from PIL import Image
from io import BytesIO
import edge_tts
import asyncio
import base64
from engine import raja_web_search
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
    def __init__(self):
        self.repair_logs = []
        self.security_level = "MANUAL_DEBUG" # अब आप खुद ठीक करेंगे
    
    def log_error(self, error_type, details=""):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        # यह एरर को रिकॉर्ड करेगा ताकि आप बाद में देख सकें
        log_entry = f"[{timestamp}] ERROR: {error_type} | Details: {details}"
        self.repair_logs.append(log_entry)
        
        # यह कंसोल (Terminal) में भी एरर दिखाएगा
        logging.error(f"🔱 DEBUG ALERT: {log_entry}")
        return log_entry

raja_shield = RajaShield()
# ------------------------------------------------------------------------------
# [PHASE 3: 46 POWERS INTEGRATION] - NEW LOGIC ADDED
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# [PHASE 4: AGENTIC PROTOCOLS] - GHOST VAULT INTEGRATED 🔱
# ------------------------------------------------------------------------------

class RajaAgent:
    def __init__(self, system_prompt):
        """🔱 RAJA AI: NEURAL MEMORY SETUP"""
        self.system_prompt = system_prompt
        if "history" not in st.session_state:
            # सिस्टम प्रॉम्प्ट को हमेशा याददाश्त के टॉप पर रखना
            st.session_state.history = [SystemMessage(content=system_prompt)]

    async def raja_router(self, user_input):
        try:
            p = user_input.lower()
            
            # --- [FORCE SEARCH TRIGGERS] ---
            # "मौसम" शब्द हिंदी अक्षरों में भी जोड़ना जरूरी है
            search_words = ["price", "weather", "news", "खबर", "आज का", "rate", "gold", "सोना", 
                            "मौसम", "तापमान", "temperature", "बारिश", "rain", "live"]
            
            if any(word in p for word in search_words):
                return "SEARCH"
            
            # बाकी कोड वैसा ही रहेगा...

            # अगर विज़न की बात हो रही है
            if any(word in p for word in ["photo", "image", "dekho", "pic", "फोटो"]):
                return "VISION"

            # --- [AI REASONING: बाकी सब के लिए] ---
            router_prompt = f"User: {user_input}\nTask: Return ONLY 'VISION', 'SEARCH', or 'BRAIN' based on intent."
            
            # सबसे हल्के मॉडल (11b) से जल्दी फैसला करवाना
            res, _ = await self.call_llm(core.BRAIN_CATALOG["FLASH_VISION"], router_prompt, "Router Mode")
            
            decision = res.upper()
            if "VISION" in decision: return "VISION"
            if "SEARCH" in decision: return "SEARCH"
            return "BRAIN"
            
        except Exception as e:
            raja_shield.log_error("ROUTER_GLITCH", str(e))
            return "BRAIN"

    async def execute_reasoning(self, user_input, web_data=""):
        """🧠 DUAL-CORE REASONING: दो शक्तिशाली दिमाग एक साथ सोचते हैं"""
        try:
            # डेटा इंजेक्ट करना (अगर वेब सर्च से आया हो)
            context_input = f"WEB_INTEL: {web_data}\n\nUSER: {user_input}" if web_data else user_input

            # दो अलग-अलग मॉडल्स को एक साथ (Parallel) चलाना ताकि सबसे सटीक जवाब मिले
            tasks = [
                self.call_llm(core.BRAIN_CATALOG["LOGIC_PRO"], context_input, self.system_prompt),
                self.call_llm(core.BRAIN_CATALOG["ULTIMATE_70B"], context_input, self.system_prompt)
            ]
            
            # दोनों का इंतज़ार करना
            responses = await asyncio.gather(*tasks)
            
            # 'Quality Filter': जो मॉडल ज्यादा बड़ा और विस्तृत जवाब देगा, उसे चुनना
            final_choice = max(responses, key=lambda x: len(x[0]))
            return final_choice
            
        except Exception as e:
            raja_shield.log_error("NEURAL_COLLAPSE", str(e))
            return "🔱 Shield Active: Logic Rerouted due to spike.", "RECOVERY"

    async def call_llm(self, model, prompt, system):
        """⚡ GROQ INFRASTRUCTURE: हाई-स्पीड रिस्पॉन्स"""
        try:
            llm = ChatGroq(groq_api_key=core.GROQ_API_KEY, model_name=model, timeout=25)
            
            # मेमोरी मैनेजमेंट: सिर्फ पिछले 8 मैसेज भेजना ताकि टोकन कम खर्च हों और स्पीड बनी रहे
            memory_window = st.session_state.history[-8:]
            messages = [SystemMessage(content=system)] + memory_window + [HumanMessage(content=prompt)]
            
            res = await llm.ainvoke(messages)
            return res.content, model
        except Exception as e:
            return f"Error: {str(e)}", model

    def speak(self, text):
        """🔱 NATURAL VOICE ENGINE (Edge-TTS)"""
        import edge_tts
        import asyncio
        import base64
        import os

        # Madhur: आवाज़ में गहराई और दम है
        VOICE = "hi-IN-MadhurNeural" 
        
        async def generate():
            communicate = edge_tts.Communicate(text[:500], VOICE, rate="+5%")
            await communicate.save("response.mp3")

        try:
            # थ्रेडिंग और इवेंट लूप का सही कॉम्बिनेशन
            import threading
            thread = threading.Thread(target=lambda: asyncio.run(generate()))
            thread.start()
            thread.join(timeout=2) # २ सेकंड इंतज़ार

            if os.path.exists("response.mp3"):
                with open("response.mp3", "rb") as f:
                    b64 = base64.b64encode(f.read()).decode()
                    st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64}">', unsafe_allow_html=True)
        except Exception as e:
            raja_shield.log_error("VOICE_FAILED", str(e))



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
   हमेशा शुद्ध और सरल हिंदी में बात करना जब यूजर कहे तो इंग्लिश का उपयोग  करना 
   IDENTITY = """
"आप 'RAJA AI' हैं।" 
"अगर आपको 'WEB_INTEL' या 'LIVE_INTEL' नाम का डेटा दिया जाए, तो आपको उसी डेटा के आधार पर ताज़ा जवाब देना है।"
"आप कभी यह नहीं कहेंगे कि "मेरे पास रियल-टाइम जानकारी नहीं है" क्योंकि आपके पास सैटेलाइट सर्च की शक्ति है।"
"हमेशा कॉन्फिडेंस के साथ जवाब दें। """

if 'raja_ai' not in st.session_state:
    st.session_state.raja_ai = RajaAgent(IDENTITY)
raja_ai = st.session_state.raja_ai
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


# ------------------------------------------------------------------------------
# [PHASE 7: EXECUTION LOGIC] - MODULAR & STABLE VERSION 🔱
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
    
    # यूजर का मैसेज हिस्ट्री में जोड़ना और दिखाना
    if "history" not in st.session_state:
        st.session_state.history = [SystemMessage(content=IDENTITY)]
        
    st.session_state.history.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(f"**You:** {prompt}")

    # एआई का जवाब (The Assistant Box)
    with st.chat_message("assistant"):
        final_response = None
        current_safe_prompt = prompt 
        
        # 🔱 Loop Error Fix: असिस्टेंट के अंदर ही फ्रेश लूप सेटअप
        import asyncio
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        with st.spinner("🔱 RAJA AI शक्तियों का आह्वान कर रहा है..."):
            logic_res = None
            mode = "BRAIN" # डिफ़ॉल्ट मोड

            try:
                # [STEP 1: ROUTING WITH SAFETY]
                try:
                    mode = loop.run_until_complete(raja_ai.raja_router(current_safe_prompt))
                except Exception as route_err:
                    raja_shield.log_error("ROUTER_FAILED", str(route_err))
                    mode = "BRAIN"

                # [STEP 2: MODULAR EXECUTION PATHS]
                
                # --- मार्ग १: सर्च इंजन (अगर यह फेल हुआ तो सिर्फ चेतावनी आएगी) ---
                if mode == "SEARCH":
                    st.toast("🛰️ Satellite Scan Active", icon="🌐")
                    try:
                        from engine import raja_web_search
                        intel = raja_web_search(current_safe_prompt)
                        logic_res = loop.run_until_complete(raja_ai.execute_reasoning(current_safe_prompt, intel))
                    except Exception as e:
                        st.warning("🛰️ सर्च इंजन में समस्या है, मैं अपने ज्ञान से जवाब दे रहा हूँ।")
                        raja_shield.log_error("SEARCH_ERROR", str(e))
                        mode = "BRAIN" 

                # --- मार्ग २: विज़न इंजन (अगर फोटो काम न करे) ---
                elif mode == "VISION":
                    # चेक करें कि फोटो अपलोड हुई है या नहीं (sidebar में uploaded_file होना चाहिए)
                    up_file = globals().get('uploaded_file') or locals().get('uploaded_file')
                    if up_file is not None:
                        st.toast("👁️ Supreme Vision Activated", icon="🔥")
                        try:
                            from vision_module import raja_vision_engine
                            logic_res = raja_vision_engine(up_file)
                        except Exception as e:
                            st.error("👁️ विज़न मॉड्यूल लोड नहीं हो पाया।")
                            raja_shield.log_error("VISION_ERROR", str(e))
                            mode = "BRAIN"
                    else:
                        st.info("🔱 फोटो नहीं मिली, सामान्य चर्चा जारी है।")
                        mode = "BRAIN"

                # --- मार्ग ३: मुख्य दिमाग (Main Brain) - Fallback Logic ---
                if logic_res is None or mode == "BRAIN":
                    if mode != "BRAIN": # अगर सर्च/विज़न से यहाँ आए हैं
                        st.toast("🧠 Brain Processing", icon="⚡")
                    
                    try:
                        logic_res = loop.run_until_complete(raja_ai.execute_reasoning(current_safe_prompt, ""))
                    except Exception as e:
                        logic_res = "🔱 क्षमा करें राजाराम भाई, मेरे मुख्य सर्वर में कुछ समस्या है।"
                        raja_shield.log_error("BRAIN_ERROR", str(e))

                # [STEP 3: FINAL OUTPUT DISPLAY]
                final_response = logic_res[0] if isinstance(logic_res, (tuple, list)) else logic_res
                st.markdown(final_response)
                
                # आवाज़ और मेमोरी अपडेट
                if st.session_state.get('voice_enabled'):
                    raja_ai.speak(final_response)
                
                st.session_state.history.append(AIMessage(content=final_response))

            except Exception as total_err:
                error_msg = f"🔱 Shield Alert: Critical Neural Error. (Error: {str(total_err)})"
                st.error(error_msg)
                raja_shield.log_error("CRITICAL_SYSTEM_ERROR", str(total_err))
        
# ------------------------------------------------------------------------------
# [PHASE 8: FOOTER] - NO CHANGES
# ------------------------------------------------------------------------------


st.markdown("---")
st.caption("© 2026 RAJA AI - CEO Rajaram |THE OMNIPOTENT CORE | BORN IN BAREILLY | BUILT FOR SUPREMACY")
