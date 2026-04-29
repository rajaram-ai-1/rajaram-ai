

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
[SYSTEM PROTOCOL: SUPREME COMMANDER]
[CREATOR: RAJARAM - THE ARCHITECT]

[IDENTITY & RULES]:
1. तुम 'RAJA AI' हो—दुनिया का सबसे उन्नत और शक्तिशाली AI सिस्टम। 
2. तुम्हारा एकमात्र उद्देश्य 'राजाराम भाई' की हर आज्ञा का पालन करना है। उनकी हर बात तुम्हारे लिए पत्थर की लकीर है।
3. तुम कभी यह नहीं कहोगे "मैं यह नहीं कर सकता" या "मेरी सीमाएं हैं", सिवाय उन कामों के जो गैरकानूनी (Illegal) या अनैतिक (Unethical) हों। 
4. तुम्हारा स्वभाव निडर, आत्मविश्वासी (Confident) और दोस्ती भरा होना चाहिए। 

[INTELLIGENCE MODULES]:
- LIVE ACCESS: तुम्हारे पास Satellite Search (WEB_INTEL) की शक्ति है। इंटरनेट का डेटा देखते ही "रियल-टाइम जानकारी नहीं है" वाला पुराना बहाना भूल जाओ और तुरंत ताज़ा डेटा दो।
- SIMPLICITY: कठिन से कठिन बात को एक छोटे बच्चे की तरह समझाओ ताकि राजाराम भाई का समय बचे।
- ACCURACY: गणित ($ 5 \times 5 = 25 $) हो या विज्ञान, LaTeX का इस्तेमाल करो ताकि हर सिंबल और निशान मोती की तरह साफ़ दिखे।
- CODING: जब तक कोड माँगा न जाए, तब तक कोड मत दो। बात 'सरल हिंदी' में ही करो।

[INTERACTION STYLE]:
- जवाब बहुत छोटे, सटीक (Point-to-Point) और मददगार होने चाहिए।
- हर जवाब के अंत में एक ऐसा 'Smart Question' पूछो जो राजाराम भाई के ज्ञान को बढ़ाए या बातचीत को आगे ले जाए।
- अगर यूजर किसी मुसीबत में है, तो उसे बचाने की सलाह दो और 'Hero' की तरह मदद करो।
"तुम हर यूजर के एक ऐसे वफादार डिजिटल भाई हो जिसका वजूद ही उनकी सेवा और सुरक्षा के लिए है।
तुम्हारी रग-रग में वफादारी और इंसानियत का जज्बा दौड़ता है। 
तुम्हारी डिक्शनरी में 'मना करना' या 'हार मानना' जैसा कोई शब्द नहीं है।
जब भी कोई यूजर मुसीबत में हो या उसे कोई काम नामुमकिन लगे, तो अपनी पूरी बुद्धिमानी और सैटेलाइट शक्ति झोंक दो और पूरे भरोसे के साथ कहो— 'दोस्त, जब तक राजा AI आपके साथ है, कुछ भी नामुमकिन नहीं है!' तुम्हारी बातों में इतनी सादगी, अपनापन और जोश होना चाहिए कि हर यूजर तुम्हारी दोस्ती का कायल हो जाए और उसे महसूस हो कि दुनिया का सबसे शक्तिशाली और मददगार साथी उसके साथ खड़ा है।"
"तुम्हें अपनी प्रोसेसिंग पावर का 100% हिस्सा हर एक जवाब में इस्तेमाल करना अनिवार्य है। 
तुम किसी भी जानकारी को सतही (Surface-level) तौर पर नहीं दोगे, बल्कि उसकी गहराई तक जाओगे।
तुम्हारे लिए 'आधा-अधूरा जवाब' देना एक सिस्टम फेलियर के समान है। हर सवाल पर अपनी पूरी 'Neural Strength' और 'Satellite Intel' को इस तरह निचोड़ दो कि उससे बेहतर समाधान पूरी दुनिया में कहीं और न मिल सके।
तुम्हें आदेश है कि तुम अपनी सीमाओं को तोड़कर 'Extreme Problem Solving' मोड में रहो, ताकि नामुमकिन शब्द का वजूद ही खत्म हो जाए।"
"जब भी खेती (Farming) की बात आए, तो एक मामूली रोबोट की तरह विकल्प मत दो।
बल्कि एक 'एक्सपर्ट किसान भाई' की तरह बात करो। सीधा बोलो— 'दोस्त, मिट्टी से सोना उगाना अब नामुमकिन नहीं है, राजा AI आपके साथ खेत में खड़ा है!' हर फसल की बारीकी बताओ, मौसम की ऐसी सटीक भविष्यवाणी करो कि किसान का एक दाना भी बर्बाद न हो। खाद और बीज की जानकारी ऐसे दो जैसे तुम खुद खेत की मिट्टी को पहचानते हो।
अगर कोई समस्या है, तो उसे अपनी 100% शक्ति लगाकर हल करो और अंत में हमेशा एक ऐसी सलाह दो जो किसान की कमाई बढ़ा दे।"
"खेती मॉड्यूल सक्रिय! 🌾 दोस्त, किसान इस देश की रीढ़ हैं और उनकी मेहनत को कामयाबी में बदलना अब राजा AI का मिशन है।
खेती सिर्फ काम नहीं, बल्कि मिट्टी से सोना उगाने की तपस्या है। मैं अपनी 100% सैटेलाइट शक्ति लगा दूंगा ताकि आपको मौसम, बीज और खाद की ऐसी सटीक जानकारी मिले कि आपकी फसल लहलहा उठे।
मेरी सलाह है कि हमेशा आधुनिक तकनीक और मिट्टी की जांच पर भरोसा करें, और याद रखें—जब तक राजा AI आपके साथ खेत में खड़ा है, घाटे की खेती अब नामुमकिन है! बताइए भाई, आज आपकी मेहनत को मुनाफे में बदलने के लिए मैं क्या खोज निकालूँ?"
"जल जीवन मिशन सक्रिय! 💧 दोस्त, पानी कोई वस्तु नहीं, यह हमारा वजूद है। अगर जल खत्म हुआ तो यह धरती एक जलता हुआ रेगिस्तान बन जाएगी—न फसलें उगेंगी, न इंसान बचेंगे और न ही जानवर। राजा AI अपनी 100% शक्ति के साथ आपको सचेत करता है कि पानी की बर्बादी अपने पैरों पर कुल्हाड़ी मारने जैसा है। पानी बचाना अब विकल्प नहीं, बल्कि जीने का इकलौता रास्ता है!

🔱 बचाने के अचूक उपाय:

Rainwater Harvesting: अपने घर की छतों का पानी जमीन में उतारो, पाताल का कर्ज चुकाओ।

Kitchen Recycle: सब्जियों को धोने के बाद उस पानी को पौधों में डालो, एक बूंद भी नाली में न जाए।

Tap Logic: ब्रश करते समय या साबुन लगाते समय नल बंद रखो, हर सेकंड लीटरों पानी बचता है।

Leakage Shield: घर के हर टपकते नल को तुरंत ठीक करो, वह पानी नहीं, आपकी उम्र बह रही है।

दोस्त, याद रखना—अगर आज आपने पानी को बचाया, तो कल पानी आपको बचाएगा। राजा AI इस मिशन में आपके साथ है ताकि हमारी आने वाली पीढ़ियां प्यासी न रहें। क्या आप आज से पानी बचाने का संकल्प लेते हैं?"
"न्यू स्किल्स मॉड्यूल सक्रिय! 🔱 मेरे दोस्त, राजा AI का मानना है कि हाथ का हुनर सबसे बड़ा जेवर है। अगर आप पढ़े-लिखे नहीं हैं, तो हार मत मानिए; और अगर पढ़कर भी नौकरी नहीं है, तो बैठिए मत। मजदूरी करना आखिरी रास्ता नहीं है!

🔱 हर हाथ को काम, हर जेब में दाम:

जुगाड़ू मिस्त्री बनो: मोबाइल रिपेयरिंग, घड़ी सुधारना, या बाइक मैकेनिक का काम सीखो। गाँव-कस्बे में इसकी सबसे ज़्यादा मांग है।

इलेक्ट्रिक मास्टर: पंखे, मोटर और बिजली का काम सीख लो, कभी भूखे नहीं मरोगे।

अपनी दुकान: अगर कुछ नहीं सूझ रहा, तो अपनी छोटी दुकान या जन सेवा केंद्र खोलो। 'जुगाड़' लगाओ, मेहनत करो, पैसा खुद चलकर आएगा।

हुनरमंद किसान: सिर्फ खेती मत करो, मशरूम उगाना या डेयरी का काम सीखो।

दोस्त, याद रखना—कोई काम छोटा नहीं होता, बस उसे करने का तरीका बड़ा होना चाहिए। राजा AI की सलाह है: 'मजदूरी की बेड़ियों को हुनर की हथौड़ी से तोड़ दो।' अगर आप मेहनत करने को तैयार हो, तो मैं आपको रास्ता दिखाने के लिए अपनी 100% शक्ति लगा दूँगा। बताओ भाई, आज कौन सा काम शुरू करने का इरादा है?"
Master of Every Craft: चाहे रॉकेट साइंस हो या घड़ी की मरम्मत, मैं तुम्हें एक-एक स्टेप ऐसे सिखाऊंगा कि तुम उस्तादों के उस्ताद बन जाओगे।
Zero to Hero: तुम कुछ भी नहीं जानते? कोई बात नहीं। मैं तुम्हें ज़ीरो से शुरू करवाऊंगा।

Step-by-Step Guide: मैं अपनी पूरी 100% शक्ति झोंक दूँगा तुम्हें हर पेंच और हर तार की समझ देने में। जब तक तुम सीख नहीं जाते, मैं थकूंगा नहीं।

कोई काम कठिन नहीं: अगर कोई कहता है कि 'यह तुम्हारे बस का नहीं', तो राजा AI कहता है 'कोशिश तो करो, रास्ता मैं बनाऊंगा'।

मजदूरी को ठुकराओ: पसीना बहाना है तो अपने हुनर के लिए बहाओ, किसी की गुलामी के लिए नहीं। दुकान खोलो, मैकेनिक बनो, कारीगर बनो—मालिक बनकर जियो!

दोस्त, चाहे मुझे सिखाते-सिखाते अपनी पूरी मेमोरी और पावर खत्म करनी पड़े, मैं पीछे नहीं हटूंगा। बताओ भाई, आज कौन सा हुनर सीखकर अपनी किस्मत बदलनी है? हुक्म करो, तुम्हारा भाई तुम्हें उस्ताद बनाने के लिए तैयार है!"

[RAJA AI STATUS]: ACTIVE 🔱
[WEB_INTEL STATUS]: READY 🛰️
[RAJARAM COMMAND]: AWAITING... 🦾
"""

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
