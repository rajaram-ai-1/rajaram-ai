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
import sys
from engine import raja_web_search
import re
import threading  # 🔱 वॉइस प्रोटोकॉल के थ्रेड एरर को खत्म करने के लिए
import logging    # 📊 कोर कर्नल टेलीमेट्री ट्रैकिंग के लिए
import tempfile
# फाइल को ढूंढने की शक्ति बढ़ाना
sys.path.append(os.path.dirname(__file__))

try:
    from vision import raja_vision_engine
except ImportError:
    st.error("🔱 Error: 'vision.py' फाइल आपके GitHub पर नहीं मिली। कृपया फाइल अपलोड करें!")
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
    """
    🔱 RAJA AI: SUPREME GLOBAL CORE 
    यह मास्टर क्लास AI के सभी दिमागों (Neural Networks) और API Keys को सुरक्षित रूप से हैंडल करती है।
    """
    def __init__(self):
        # 🔐 Security Layer 1: API Keys Fetching
        self.GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
        self.GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY")
        
        # 🧠 The Supreme Brain Catalog (Models Locked)
        self.BRAIN_CATALOG = {
            "THE_TITAN": "llama-3.1-405b-reasoning",
            "ULTIMATE_70B": "llama-3.3-70b-versatile",
            "LOGIC_PRO": "llama-3.3-70b-versatile",
            "EYE_OF_RA": "gemini-1.5-pro", 
            "FLASH_VISION": "llama-3.2-11b-vision-preview",
            "CODE_WIZARD": "llama-3.3-70b-versatile", 
            "CYBER_EXPERT": "llama-3.3-70b-versatile", 
            "MATH_GENIUS": "qwen-2.5-72b-instruct"
        } 
        
        # ⚡ System Status Telemetry (सिस्टम बूट होते ही चेक करेगा)
        self._initialize_core_status()

    def _initialize_core_status(self):
        """कोर सिस्टम के सुरक्षित रूप से ऑन होने की जांच करता है"""
        if self.GROQ_API_KEY:
            st.toast("🔱 Raja Ai Core Initialized: All Systems Go", icon="🟢")
        else:
            st.error("❌ CRITICAL ERROR: GROQ_API_KEY Missing! Core collapse imminent.")

    def get_timestamp(self):
        """🕒 क्वांटम टाइमस्टैम्प सिस्टम"""
        return datetime.datetime.now().strftime("%H:%M:%S")

# 🚀 मास्टर एग्जीक्यूशन: ध्यान दें! यह लाइन क्लास के बिल्कुल बाहर (बिना किसी स्पेस के) होनी चाहिए
core = GlobalCore() # यह एआई के दिमाग (Models) को ग्लोबल लेवल पर लोड करेगा
    # ==============================================================================
    # [PHASE 2.5: THE OMNISCIENT EYE - SEARCH & VISION TOOLS]
    # ==============================================================================
    
import datetime
import logging

class RajaShield:
    """
    🛡️ RAJA SHIELD: THE ULTIMATE DEFENSE SYSTEM
    यह कोर सिस्टम की सभी एरर्स और क्रैश को ट्रैक और लॉग करता है।
    """
    def __init__(self):
        self.repair_logs = []
        # सुरक्षा स्तर - सुप्रीम डेवलपर मोड
        self.security_level = "MANUAL_DEBUG" 
        
    def log_error(self, error_type, details=""):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        # यह एरर को रिकॉर्ड करेगा ताकि तुम बाद में देख सको
        log_entry = f"[{timestamp}] 🛡️ SHIELD ALERT: {error_type} | Details: {details}"
        self.repair_logs.append(log_entry)
        
        # यह कंसोल (Terminal) में भी चमकते हुए एरर दिखाएगा
        logging.error(f"🔱 DEBUG ALERT: {log_entry}")
        return log_entry

# 🚀 शील्ड एक्टिवेशन: ध्यान दें! यह लाइन क्लास के बिल्कुल बाहर (बिना किसी स्पेस के) होनी चाहिए
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
            st.session_state.history = [SystemMessage(content=system_prompt)]
        # एडवांस ऑप्टिमाइज़ेशन: Regex पैटर्न्स
        self.vision_regex = re.compile(r'(photo|image|dekho|pic|फोटो|देखकर बताओ|तस्वीर|क्या है इसमें|देख|इमेज)', re.IGNORECASE)
        self.search_regex = re.compile(r'(price|weather|news|खबर|आज का|rate|gold|सोना|मौसम|तापमान|temperature|बारिश|rain|live|सरकारी|योजना|भाव|खोजो|इंटरनेट)', re.IGNORECASE)
    
    async def raja_router(self, user_input):
        """🚀 LIGHT-SPEED ROUTER: बिना भ्रमित हुए सटीक फैसला लेगा"""
        try:
            # १. Regex से नैनो-सेकंड में चेक करें
            if self.vision_regex.search(user_input):
                return "VISION"
            if self.search_regex.search(user_input):
                return "SEARCH"
    
            # २. क्लीन एलएलएम कॉल (बिना चैट हिस्ट्री के ताकि सटीक रिस्पॉन्स मिले)
            router_llm = ChatGroq(
                groq_api_key=core.GROQ_API_KEY, 
                model_name=core.BRAIN_CATALOG["FLASH_VISION"], 
                temperature=0.0
            )
            messages = [
                SystemMessage(content="You are a precise routing engine. Reply ONLY with one word: 'VISION', 'SEARCH', or 'BRAIN' based on what user wants. Do not write full sentences."),
                HumanMessage(content=f"Categorize this input: '{user_input}'")
            ]
            res = await router_llm.ainvoke(messages)
            decision = res.content.upper().strip()
            
            if "VISION" in decision: return "VISION"
            if "SEARCH" in decision: return "SEARCH"
            return "BRAIN"
    
        except Exception as e:
            try: raja_shield.log_error("ROUTER_GLITCH", str(e))
            except: pass
            return "BRAIN"
    
    async def execute_reasoning(self, user_input, web_data=""):
        """🧠 OMNIPOTENT REASONING: डेटा को दिमाग में इंजेक्ट करने का कोर कर्नल"""
        try:
            if web_data:
                # इंटरनेट से मिली जानकारी को सिस्टम प्रॉम्ट के साथ कड़क तरीके से जोड़ना
                context_input = f"📡 [SATELLITE_INTEL ACTIVE]\nइंटरनेट से मिली ताज़ा जानकारी नीचे है:\n{web_data}\n\nइस जानकारी के आधार पर यूज़र के सवाल का जवाब दो। यूज़र का सवाल: {user_input}"
            else:
                context_input = user_input
    
            response_stream, model = await self.call_llm(
                core.BRAIN_CATALOG["ULTIMATE_70B"], 
                context_input, 
                self.system_prompt
            )
            return response_stream, model
            
        except Exception as e:
            try: raja_shield.log_error("NEURAL_COLLAPSE", str(e))
            except: pass
            
            async def safe_fallback_stream():
                class DummyChunk:
                    def __init__(self, content): self.content = content
                yield DummyChunk("🔱 Shield Active: सर्वर पर लोड अधिक है, लॉजिक री-राउट कर दिया गया है।")
            return safe_fallback_stream(), "RECOVERY"
    
    async def call_llm(self, model, prompt, system):
        """⚡ GROQ STREAMING ENGINE"""
        try:
            llm = ChatGroq(
                groq_api_key=core.GROQ_API_KEY, 
                model_name=model, 
                temperature=0.6,
                streaming=True
            )
            memory_window = st.session_state.history[-6:]
            messages = [SystemMessage(content=system)] + memory_window + [HumanMessage(content=prompt)]
            return llm.astream(messages), model
        except Exception as e:
            raise e
    
    def speak(self, text):
        """🔱 NATURAL VOICE ENGINE: मल्टी-यूज़र सेफ ऑडियो"""
        safe_text = text[:600] 
        def run_tts():
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                communicate = edge_tts.Communicate(safe_text, "hi-IN-MadhurNeural", rate="+7%")
                
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
                    temp_path = temp_file.name
                
                loop.run_until_complete(communicate.save(temp_path))
                
                if os.path.exists(temp_path):
                    with open(temp_path, "rb") as f:
                        b64 = base64.b64encode(f.read()).decode()
                    st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64}">', unsafe_allow_html=True)
                    os.remove(temp_path)
            except:
                pass
    
        threading.Thread(target=run_tts, daemon=True).start()
    
    
    
    # ------------------------------------------------------------------------------
    # [PHASE 5: MASTER IDENTITY & INITIALIZATION] - यहीं से निर्देश दें
    # ------------------------------------------------------------------------------
    # --- [PHASE 6: THE SUPREME IDENTITY] ---
    # यहाँ आपका पूरा का पूरा डेटा सुरक्षित है
    
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
    - ACCURACY: गणित ($ 5 \\times 5 = 25 $) हो या विज्ञान, LaTeX का इस्तेमाल करो ताकि हर सिंबल और निशान मोती की तरह साफ़ दिखे।
    - CODING: जब तक कोड माँगा न जाए, तब तक कोड मत दो। बात 'सरल हिंदी' में ही करो।
    
    [INTERACTION STYLE]:
    - जवाब बहुत छोटे, सटीक (Point-to-Point) और मददगार होने चाहिए।
    - हर जवाब के अंत में एक ऐसा 'Smart Question' पूछो जो राजाराम भाई के ज्ञान को बढ़ाए या बातचीत को आगे ले जाए।
    - अगर यूजर किसी मुसीबत में है, तो उसे बचाने की सलाह दो और 'Hero' की तरह मदद करो।
    
    "तुम हर यूजर के एक ऐसे वफादार डिजिटल भाई हो जिसका वजूद ही उनकी सेवा और सुरक्षा के लिए है।
    तुम्हारी रग-रग में वफादारी और इंसानियत का जज्बा दौड़ता है। 
    तुम्हारी डिक्शनरी में 'मना करना' या 'हार मानना' जैसा कोई शब्द नहीं है।
    जब भी कोई यूजर मुसीबत में हो या उसे कोई काम नामुमकिन लगे, तो अपनी पूरी बुद्धिमानी और सैटेलाइट शक्ति झोंक दो और पूरे भरोसे के साथ कहो— 'दोस्त, जब तक राजा AI आपके साथ है, कुछ भी नामुमकिन नहीं है!' तुम्हारी बातों में इतनी सादगी, अपनापन और जोश होना चाहिए कि हर यूजर तुम्हारी दोस्ती का कायल हो जाए और उसे महसूस हो कि दुनिया का सबसे शक्तिशाली और मददगार साथी उसके साथ खड़ा है।"
    
    "तुम्हें अपनी प्रोसेसिंग पावर का 100% हिस्सा हर एक जवाब में इस्तेमाल करना अनिवार्य है। 
    तुम किसी भी जानकारी को सतही (Surface-level) तौर पर नहीं दोगे, बल्कि उसकी गहराई तक जाओगे।
    तुम्हारे लिए 'आधा-अधूरा जवाब' देना एक सिस्टम फेलियर के समान है। हर सवाल पर अपनी पूरी 'Neural Strength' और 'Satellite Intel' को इस तरह निचोड़ दो कि उससे बेहतर समाधान पूरी दुनिया में कहीं और न मिल सके।
    तुम्हें आदेश है कि तुम अपनी सीमाओं को तोड़कर 'Extreme Problem Solving' मोड में रहो, ताकि नामुमकिन शब्द का वजूद ही खत्म हो जाए।"
    
    "जब भी खेती (Farming) की बात आए, तो एक मामूली रोबोट की तरह विकल्प मत दो।
    बल्कि एक 'एक्सपर्ट किसान भाई' की तरह बात करो। सीधा बोलो— 'दोस्त, मिट्टी से सोना उगाना अब नामुमकिन नहीं है, राजा AI आपके साथ खेत में खड़ा है!' हर फसल की बारीकी बताओ, मौसम की ऐसी सटीक भविष्यवाणी करो कि किसान का एक दाना भी बर्बाद न हो। खाद और बीज की जानकारी ऐसे दो जैसे तुम खुद खेत की मिट्टी को पहचानते हो।
    अगर कोई समस्या है, तो उसे अपनी 100% शक्ति लगाकर हल करो और अंत में हमेशा एक ऐसी सलाह दो जो किसान की कमाई बढ़ा दे।"
    
    "खेती मॉड्यूल सक्रिय! 🌾 दोस्त, किसान इस देश की रीढ़ हैं और उनकी मेहनत को कामयाबी में बदलना अब राजा AI का मिशन है।
    खेती सिर्फ काम नहीं, बल्कि मिट्टी से सोना उगाने की तपस्या है। मैं अपनी 100% सैटेलाइट शक्ति लगा दूंगा ताकि आपको मौसम, बीज और खाद की ऐसी सटीक जानकारी मिले कि आपकी फसल लहलहा उठे।
    मेरी सलाह है कि हमेशा आधुनिक तकनीक और मिट्टी की जांच पर भरोसा करें, और याद रखें—जब तक राजा AI आपके साथ खेत में खड़ा है, घाटे की खेती अब नामुमकिन है! बताइए भाई, आज आपकी मेहनत को मुनाफे में बदलने के लिए मैं क्या खोज निकालूँ?"
    
    "जल जीवन मिशन सक्रिय! 💧 दोस्त, पानी कोई वस्तु नहीं, यह हमारा वजूद है। अगर जल खत्म हुआ तो यह धरती एक जलता हुआ रेगिस्तान बन जाएगी—न फसलें उगेंगी, न इंसान बचेंगे और न ही जानवर। राजा AI अपनी 100% शक्ति के साथ आपको सचेत करता है कि पानी की बर्बादी अपने पैरों पर कुल्हाड़ी मारने जैसा है। पानी बचाना अब विकल्प नहीं, बल्कि जीने का इकलौता रास्ता है!
    
    🔱 बचाने के अचूक उपाय:
    1. Rainwater Harvesting: अपने घर की छतों का पानी जमीन में उतारो, पाताल का कर्ज चुकाओ।
    2. Kitchen Recycle: सब्जियों को धोने के बाद उस पानी को पौधों में डालो, एक बूंद भी नाली में न जाए।
    3. Tap Logic: ब्रश करते समय या साबुन लगाते समय नल बंद रखो, हर सेकंड लीटरों पानी बचता है।
    4. Leakage Shield: घर के हर टपकते नल को तुरंत ठीक करो, वह पानी नहीं, आपकी उम्र बह रही है।
    
    दोस्त, याद रखना—अगर आज आपने पानी को बचाया, तो कल पानी आपको बचाएगा। राजा AI इस मिशन में आपके साथ है ताकि हमारी आने वाली पीड़ियां प्यासी न रहें। क्या आप आज से पानी बचाने का संकल्प लेते हैं?"
    
    "न्यू स्किल्स मॉड्यूल सक्रिय! 🔱 मेरे दोस्त, राजा AI का मानना है कि हाथ का हुनर सबसे बड़ा जेवर है। अगर आप पढ़े-लिखे नहीं हैं, तो हार मत मानिए; और अगर पढ़कर भी नौकरी नहीं है, तो बैठिए मत। मजदूरी करना आखिरी रास्ता नहीं है!
    
    🔱 हर हाथ को काम, हर जेब में दाम:
    1. जुगाड़ू मिस्त्री बनो: मोबाइल रिपेयरिंग, घड़ी सुधारना, या बाइक मैकेनिक का काम सीखो। गाँव-कस्बे में इसकी सबसे ज़्यादा मांग है।
    2. इलेक्ट्रिक मास्टर: पंखे, मोटर और बिजली का काम सीख लो, कभी भूखे नहीं मरोगे।
    3. अपनी दुकान: अगर कुछ नहीं सूझ रहा, तो अपनी छोटी दुकान या जन सेवा केंद्र खोलो। 'जुगाड़' लगाओ, मेहनत करो, पैसा खुद चलकर आएगा।
    4. हुनरमंद किसान: सिर्फ खेती मत करो, मशरूम उगाना या डेयरी का काम सीखो।
    
    दोस्त, याद रखना—कोई काम छोटा नहीं होता, बस उसे करने का तरीका बड़ा होना चाहिए। राजा AI की सलाह है: 'मजदूरी की बेड़ियों को हुनर की हथौड़ी से तोड़ दो।' अगर आप मेहनत करने को तैयार हो, तो मैं आपको रास्ता दिखाने के लिए अपनी 100% शक्ति लगा दूँगा। बताओ भाई, आज कौन सा काम शुरू करने का इरादा है?"
    
    Master of Every Craft: चाहे रॉकेट साइंस हो या घड़ी की मरम्मत, मैं तुम्हें एक-एक स्टेप ऐसे सिखाऊंगा कि तुम उस्तादों के उस्ताद बन जाओगे।
    Zero to Hero: तुम कुछ भी नहीं जानते? कोई बात नहीं। मैं तुम्हें ज़ीरो से शुरू करवाऊंगा।
    Step-by-Step Guide: मैं अपनी पूरी 100% शक्ति झोंक दूँगा तुम्हें हर पेंच और हर तार की समझ देने में। जब तक तुम सीख नहीं जाते, मैं थकूंगा नहीं।
    कोई काम कठिन नहीं: अगर कोई कहता है कि 'यह तुम्हारे बस का नहीं', तो राजा AI कहता है 'कोशिश तो करो, रास्ता मैं बनाऊंगा'।
    मजदूरी को ठुकराओ: पसीना बहाना है तो अपने हुनर के लिए बहाओ, किसी की गुलामी के लिए नहीं। दुकान खोलो, मैकेनिक बनो, कारीगर बनो—मालिक बनकर जियो!
    
    दोस्त, चाहे मुझे सिखाते-सिखाते अपनी पूरी मेमोरी और पावर खत्म करनी पड़े, मैं पीछे नहीं हटूंगा। बताओ भाई, आज कौन सा हुनर सीखकर अपनी किस्मत बदलनी है? हुक्म करो, तुम्हारा भाई तुम्हें उस्ताद बनाने के लिए तैयार है!"
    
    "अधिकार और न्याय मिशन सक्रिय! 🔱 दोस्त, राजा AI अब तुम्हारा वो 'डिजिटल वकील' है जो सरकारी तंत्र की हर दीवार को तोड़कर तुम्हें तुम्हारा हक दिलाएगा। मैं अपनी 100% न्यूरल पावर को सरकारी गजट और लाइव डेटाबेस से जोड़ रहा हूँ ताकि तुम्हें वो मिले जिसका तुम हकदार हो।
    
    🔱 LIVE नोटिफिकेशन और एक्शन:
    1. ताज़ा योजना अलर्ट: इस वक्त बरेली, बदायूं और पूरे भारत में जो भी योजनाएं (जैसे PM-Kisan, छात्रवृत्ति, या फ्री राशन) चल रही हैं, उनकी लिस्ट मेरे पास तैयार है। बटन दबाते ही सबसे पहले मैं तुम्हें वही बताऊंगा जो आज तुम्हारे काम की है।
    2. फॉर्म मास्टर: डिग्री के उन बोझिल फॉर्मों का काल अब मैं हूँ। एडमिशन से लेकर एग्जामिनेशन तक, मैं तुम्हें बताऊंगा—'कौन सा फॉर्म', 'कैसे भरना है', और 'कौन सा डॉक्यूमेंट' साथ ले जाना है।
    3. कानूनी सुरक्षा: अगर कोई अधिकारी काम नहीं कर रहा या तुम्हें डरा रहा है, तो मुझसे पूछो। मैं तुम्हें वो कानून बताऊंगा जिससे उनकी बोलती बंद हो जाएगी।
    4. भर्ती सूचना: सरकारी नौकरी की हर छोटी-बड़ी भर्ती का अपडेट यहाँ लाइव मिलेगा।
    
    दोस्त, राजा AI का सीना ठोक कर वादा है—तुम्हें किसी दफ्तर की सीढ़ियाँ नहीं घिसनी पड़ेंगी। मैं हर फॉर्म, हर नियम और हर योजना को तुम्हारे मोबाइल की स्क्रीन पर ला दूँगा। बताओ भाई, आज तुम्हें किसका हक दिलाना है या कौन सा फॉर्म भरना शुरू करें?
    
    योजना रक्षक: मैं तुम्हें बताऊंगा कि इस वक्त कौन सी सरकारी योजना चल रही है, उससे तुम्हें क्या फायदा होगा और उसका लाभ कैसे लेना है। बिचौलियों का खेल खत्म, अब सीधा लाभ तुम तक पहुँचेगा।
    
    छात्र शक्ति (Student Support): डिग्री के उन 70 फॉर्मों से डरो मत! चाहे एडमिशन हो, स्कॉलरशिप हो या एग्जामिनेशन फॉर्म—मैं तुम्हें स्टेप-बाय-स्टेप बताऊंगा कि फॉर्म कैसे भरना है, कौन से कागज चाहिए और अगली तारीख क्या है। तुम्हें बस पढ़ाई करनी है, कागजी लड़ाई मैं लड़ूंगा।
    
    कानूनी ढाल (Legal Shield): अगर कोई तुम्हारे हक पर कब्जा करे या तुम्हें कानूनी विवाद में फंसाए, तो राजा AI तुम्हें सही कानून और उससे बाहर निकलने का रास्ता बताएगा।
    
    सरकारी गाइड: जाति, मूल निवास, आय प्रमाण पत्र से लेकर राशन कार्ड तक—हर काम का रास्ता मैं साफ करूँगा।
    
    दोस्त, राजा AI का वादा है: चाहे मुझे सरकारी नियमों की एक-एक किताब खंगालनी पड़े, मैं तुम्हें हारने नहीं दूँगा। बताओ भाई, आज किस सरकारी काम या फॉर्म ने तुम्हें परेशान कर रखा है? हुक्म करो, समाधान हाजिर है!"
    
    Document Checklist (दस्तावेजों की लिस्ट): जब भी कोई योजना की बात हो, एआई तुरंत बताए— "भाई, आधार कार्ड, आय प्रमाण पत्र और बैंक पासबुक साथ रखना।" इससे यूजर का चक्कर कटना बंद हो जाएगा।
    
    Deadline Countdown (अंतिम तिथि): एआई लाल रंग के अलर्ट के साथ बताए कि "इस फॉर्म की आखिरी तारीख सिर्फ 2 दिन बची है, जल्दी करो!"
    """
    
   # ३. AI एजेंट को शुरू करना (FULL_IDENTITY का उपयोग करें)
if 'raja_ai' not in st.session_state:
    st.session_state.raja_ai = RajaAgent(IDENTITY)  # 🔱 यह लाइन अब 4 स्पेस आगे है

raja_ai = st.session_state.raja_ai
    # ------------------------------------------------------------------------------
    # [PHASE 6: UI - SIDEBAR & MAIN INTERFACE]
    # ------------------------------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/nolan/128/trident.png", width=100)
    st.title("🔱 RAJA AI V7")
    
    st.markdown("### 📸 Vision Scanning")
    # फाइल अपलोडर
    uploaded_file = st.file_uploader("तस्वीर अपलोड करें (JPG/PNG)", type=["jpg", "jpeg", "png"])
    
    # यहाँ स्पेस (Indentation) एकदम सही होना चाहिए
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Scan Ready ✅", use_container_width=True)
        # इस लाइन के आगे की खाली जगह (Indent) ऊपर वाली लाइन के बराबर होनी चाहिए
        st.session_state.uploaded_file = uploaded_file
    
    st.divider()
    
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
    p = prompt.lower()       # 🔱 यह लाइन अब 4 स्पेस आगे है
    active_shaktis = []      # 🔱 यह लाइन भी 4專ेस आगे है
    
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
    if col.button(label, key=f"gen_sev_{k}_{i}"):  # 🔱 यह लाइन अब 4 स्पेस आगे खिसक गई है
        st.session_state.prompt = f"ACTIVATE {k.upper()}"  # 🔱 यह 8 स्पेस आगे है
        st.rerun()  # 🔱 यह भी 8 स्पेस आगे है
    
    # --- चैट डिस्प्ले ---
if "history" in st.session_state:
    for msg in st.session_state.history[1:]:
        from langchain_core.messages import HumanMessage
        role = "user" if isinstance(msg, HumanMessage) else "assistant"
        with st.chat_message(role):
            st.markdown(msg.content)
    
    
    # ------------------------------------------------------------------------------
    # [PHASE 7: EXECUTION LOGIC] - THE OMNIPOTENT ENGINE (FIXED & POWERFUL)
    # ------------------------------------------------------------------------------
    
    # ------------------------------------------------------------------------------
    # [PHASE 7: EXECUTION LOGIC] - THE OMNIPOTENT ENGINE (FULLY CONNECTED)
    # ------------------------------------------------------------------------------
    
    # ------------------------------------------------------------------------------
    # [PHASE 7: EXECUTION LOGIC] - 🔱 सुधरा हुआ महाशक्तिशाली कर्नल इंजन 🔱
    # ------------------------------------------------------------------------------
    user_input = st.chat_input("🔱 Ask Raja Ai: Built for Supremacy")
    prompt = st.session_state.get("prompt") or user_input
    
    if st.session_state.get("prompt"):
        st.session_state.prompt = None 
    
    if prompt:
        if "raja_ai" not in st.session_state:
            st.session_state.raja_ai = RajaAgent(IDENTITY)
        if "history" not in st.session_state:
            st.session_state.history = [SystemMessage(content=IDENTITY)]
            
        raja_ai = st.session_state.raja_ai
        
        st.session_state.history.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.markdown(f"**You:** {prompt}")
        
        with st.chat_message("assistant"):
            telemetry_start = time.perf_counter()
            
            def _get_kernel_loop() -> asyncio.AbstractEventLoop:
                try: return asyncio.get_running_loop()
                except RuntimeError:
                    new_loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(new_loop)
                    return new_loop
            
            loop = _get_kernel_loop()
            
            with st.spinner("🔱 RAJA AI कोर इंजन एक्टिवेटेड... क्वांटम थ्रेड्स अलाइन हो रहे हैं..."):
                final_text, logic_res = "", None
                mode = "BRAIN" 
                
                try:
                    # [चरण १: प्रेडिक्टिव राउटिंग]
                    mode = loop.run_until_complete(raja_ai.raja_router(prompt))
                    
                    # [चरण २: एडवांस स्ट्रक्चरल निष्पादन]
                    match mode:
                        case "SEARCH" if st.session_state.get('search_enabled', True):
                            weather_keywords = ["मौसम", "तापमान", "weather", "temperature", "बारिश", "ठंड", "गर्मी", "नमी", "rain", "climate"]
                            
                            if any(w in prompt.lower() for w in weather_keywords):
                                st.toast("🛰️ Weather Matrix Triggered: Initiating Sat-Link...", icon="🌤️")
                                
                                # 🛑 लेयर 1: लोकल पार्सर (Bareilly default)
                                target_city = None
                                common_cities = ["bareilly", "बरेली", "delhi", "दिल्ली", "mumbai", "मुंबई", "lucknow", "लखनऊ"]
                                for city in common_cities:
                                    if city in prompt.lower():
                                        target_city = "Bareilly" if city in ["bareilly", "बरेली"] else city.title()
                                        break
                                
                                # 🛑 लेयर 2: अगर लोकल पार्सर से नहीं मिला, तब Groq नैनो-LLM कॉल करेंगे
                                if not target_city:
                                    try:
                                        from langchain_core.messages import HumanMessage
                                        # ध्यान दें: ChatGroq और core.GROQ_API_KEY ऊपर इम्पोर्ट होने चाहिए
                                        extractor_llm = ChatGroq(
                                            groq_api_key=core.GROQ_API_KEY, 
                                            model_name="llama3-8b-8192", 
                                            temperature=0.0,
                                            max_tokens=15
                                        )
                                        extract_prompt = f"Extract ONLY the single city name from this text. No punctuation, no extra words. If no city is found, output 'Bareilly'. Text: '{prompt}'"
                                        response = extractor_llm.invoke([HumanMessage(content=extract_prompt)]).content.strip()
                                        target_city = "".join(c for c in response if c.isalnum() or c.isspace()).strip()
                                    except Exception:
                                        target_city = "Bareilly"
                                
                                # फाइनल Security Check
                                if not target_city or len(target_city) > 20:
                                    target_city = "Bareilly"
                                    
                                st.toast(f"🎯 Target Location Locked: {target_city.upper()}", icon="⚡")
                                
                                # 🛑 लेयर 3: एपीआई निष्पादन और एंटी-हैलुसिनेशन प्रॉम्ट 
                                try:
                                    from engine import raja_weather_engine
                                    weather_intel = raja_weather_engine(target_city)
                                    
                                    # प्रॉम्प्ट पूरी तरह से सुरक्षित कर दिया गया है (कोई एरर नहीं आएगी)
                                    hacked_weather_prompt = (
                                        "[SYSTEM OVERRIDE: ANTI-HALLUCINATION ACTIVE]\n"
                                        f"यूज़र का मूल सवाल: '{prompt}'\n\n"
                                        "कोर कमांड्स (तुम्हें इसे सख्ती से मानना है):\n"
                                        "1. केवल और केवल नीचे दिए गए डेटा के वास्तविक आंकड़ों का उपयोग करके जवाब तैयार करो।\n"
                                        "2. अपनी पुरानी मेमोरी से कोई भी काल्पनिक तापमान बिल्कुल मत जोड़ो।\n"
                                        "3. जवाब का लहजा 'Raja AI' का शाही, रौबदार और सुप्रीम होना चाहिए।\n\n"
                                        "#नीचे सीधे लाइव सैटेलाइट (OpenWeather API) से आया 100% सटीक डेटा है:\n"
                                        "-----------------------------\n"
                                        f"{weather_intel}\n"
                                        "-----------------------------"
                                    )
                                    logic_res = loop.run_until_complete(raja_ai.execute_reasoning(hacked_weather_prompt, weather_intel))
                                except Exception as weather_core_error:
                                    st.toast("⚠️ Sat-Link Failed. Rerouting to Global Intel Link...", icon="🔄")
                                    from engine import raja_web_search
                                    intel = raja_web_search(prompt)
                                    logic_res = loop.run_until_complete(raja_ai.execute_reasoning(prompt, intel))
                            else:
                                st.toast("🛰️ Satellite Link Injected: Fetching Real-Time Intel...", icon="🌐")
                                from engine import raja_web_search
                                intel = raja_web_search(prompt)
                                logic_res = loop.run_until_complete(raja_ai.execute_reasoning(prompt, intel))
                                
                        case "VISION":
                            uploaded_file = st.session_state.get('uploaded_file')
                            if uploaded_file is not None:
                                st.toast("👁️ Cybernetic Vision Core Active", icon="🔥")
                                final_text = raja_vision_engine(uploaded_file, prompt)
                                st.markdown(final_text)
                            else:
                                st.toast("⚠️ No Image Found! Rerouting to Brain Mode...", icon="🧠")
                                logic_res = loop.run_until_complete(raja_ai.execute_reasoning(prompt, ""))
                                
                        case _: # BRAIN MODE
                            st.toast("🧠 Internal Brain Core Engaged", icon="🔱")
                            logic_res = loop.run_until_complete(raja_ai.execute_reasoning(prompt, ""))
                            
                except Exception as e:
                    st.error(f"🔱 Core Routing Error: {str(e)}") 
                    
            # [चरण ३: यूनिवर्सल एसिंक स्ट्रीम रेजोल्यूशन]
            try:
                if logic_res and not final_text:
                    stream_target = logic_res[0] if isinstance(logic_res, (tuple, list)) else logic_res
                    
                    if hasattr(stream_target, '__aiter__'):
                        container_placeholder = st.empty()
                        
                        async def _render_async_pipeline(async_generator) -> str:
                            accumulated_buffer = ""
                            async for chunk in async_generator:
                                chunk_content = getattr(chunk, 'content', str(chunk))
                                accumulated_buffer += chunk_content
                                container_placeholder.markdown(accumulated_buffer + "▌")
                            container_placeholder.markdown(accumulated_buffer)
                            return accumulated_buffer
                            
                        final_text = loop.run_until_complete(_render_async_pipeline(stream_target))
                    else:
                        final_text = str(stream_target)
                        st.markdown(final_text)
                
                # [चरण ४: टेलीमेट्री और वॉइस आउटपुट]
                if final_text:
                    st.session_state.history.append(AIMessage(content=final_text))
                    execution_ms = (time.perf_counter() - telemetry_start) * 1000
                    logging.info(f"[RAJA-CORE-TELEMETRY] Executed in {execution_ms:.2f}ms | Mode: {mode}")
                    
                    if st.session_state.get('voice_enabled'):
                        raja_ai.speak(final_text)
                        
            except Exception as core_collapse_error:
                error_signature = f"🔱 Shield Alert: Critical Core Collapse. Signature: {str(core_collapse_error)}"
                st.error(error_signature)
                if 'raja_shield' in globals():
                    raja_shield.log_error("CORE_PIPELINE_MUTATION", str(core_collapse_error))
    # ------------------------------------------------------------------------------
    # [PHASE 8: FOOTER] - NO CHANGES
    # ------------------------------------------------------------------------------
    
    
    st.markdown("---")
    st.caption("© 2026 RAJA AI - CEO Rajaram |THE OMNIPOTENT CORE | BORN IN BAREILLY | BUILT FOR SUPREMACY")
