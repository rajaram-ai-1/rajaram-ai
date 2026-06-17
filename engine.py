# ==============================================================================
# 🔱 RAJA AI: GLOBAL INTELLIGENCE KERNEL (engine.py) 🔱
# ==============================================================================
# विवरण: यह राजा एआई का मुख्य शस्त्रागार है। यहाँ से दुनिया भर के सर्वर्स (Tavily, OpenWeather) 
# से लाइव डेटा इंटरसेप्ट किया जाता है और एआई के दिमाग में इंजेक्ट किया जाता है।
# ==============================================================================

import logging
import requests
import streamlit as st
from tavily import TavilyClient
from requests.exceptions import RequestException

# ---------------------------------------------------------
# [TELEMETRY SETUP] - डार्क हैकर स्टाइल लॉगिंग
# ---------------------------------------------------------
logging.basicConfig(
    level=logging.INFO, 
    format="[%(asctime)s] [RAJA-CORE-TELEMETRY] ⚡ %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class RajaIntelligenceGateway:
    """
    🚀 OMNIPOTENT API GATEWAY: 
    यह क्लास सारे बाहरी सर्वर्स को कंट्रोल करती है। 
    इसे एक बार इनिशियलाइज़ करने पर यह सारे कनेक्शन सुरक्षित रूप से होल्ड करती है।
    """
    def __init__(self):
        try:
            # 🔐 सिक्योर वॉल्ट से चाबियां (API Keys) निकालना
            self.tavily_api_key = st.secrets.get("TAVILY_API_KEY")
            self.weather_api_key = st.secrets.get("OPENWEATHER_API_KEY")
            
            if not self.tavily_api_key or not self.weather_api_key:
                logging.error("⚠️ CRITICAL ALARM: API Keys गायब हैं! secrets.toml चेक करें।")
            else:
                self.search_client = TavilyClient(api_key=self.tavily_api_key)
                logging.info("🔱 Raja Intelligence Gateway: ALL SYSTEMS GREEN (Search & Weather Active)")
                
        except Exception as e:
            logging.error(f"💥 INITIALIZATION FAILED: {str(e)}")

    def fetch_live_search(self, query: str) -> str:
        """🌐 SATELLITE SEARCH LINK (TAVILY)"""
        try:
            logging.info(f"🔎 Tavily इंटरसेप्टर एक्टिवेटेड: '{query}'")
            response = self.search_client.search(query=query, max_results=3)
            
            intel_string = "--- 📡 SATELLITE LIVE DATA INTERCEPTED ---\n"
            for index, result in enumerate(response['results'], start=1):
                intel_string += f"[{index}] 📌 शीर्षक: {result.get('title', 'No Title')}\n"
                intel_string += f"    📄 जानकारी: {result.get('content', 'No Content')}\n"
                intel_string += f"    🔗 स्रोत: {result.get('url', 'No URL')}\n\n"
            intel_string += "----------------------------------------"
            
            return intel_string
            
        except Exception as e:
            logging.error(f"❌ सर्च इंजन क्रैश: {str(e)}")
            return "⚠️ सर्च इंजन इस समय लाइव डेटा फेच नहीं कर पा रहा है। सुरक्षा शील्ड एक्टिवेट कर दी गई है।"

    def fetch_live_weather(self, city: str) -> str:
        """⛈️ QUANTUM WEATHER LINK (OPENWEATHERMAP)"""
        try:
            logging.info(f"🌤️ मौसम सॅटेलाइट टारगेट: '{city}'")
            base_url = "http://api.openweathermap.org/data/2.5/weather"
            
            payload = {
                "q": city,
                "appid": self.weather_api_key,
                "units": "metric",  
                "lang": "hi"        
            }
            
            # 5 सेकंड का टाइमआउट (सिस्टम हैंग होने से बचाने के लिए)
            response = requests.get(base_url, params=payload, timeout=5)
            response.raise_for_status() 
            
            data = response.json()
            
            intel = f"""
            🛰️ [WEATHER UPLINK SECURE: {data['name'].upper()}, {data['sys']['country']}]
            🌡️ तापमान: {data['main']['temp']}°C (महसूस: {data['main']['feels_like']}°C)
            ☁️ मौसम का हाल: {data['weather'][0]['description'].title()}
            💧 हवा में नमी: {data['main']['humidity']}% | 💨 हवा की रफ्तार: {data['wind']['speed']} m/s
            📉 आज का न्यूनतम/अधिकतम: {data['main']['temp_min']}°C / {data['main']['temp_max']}°C
            """
            return intel
            
        except RequestException as e:
            logging.error(f"❌ वेदर लिंक फेल: {str(e)}")
            return f"⚠️ सॅटेलाइट लिंक फेल (Network Error): {str(e)}"
        except KeyError:
            logging.error(f"❌ शहर '{city}' का डेटाबेस में मिलान नहीं हुआ।")
            return f"⚠️ शहर '{city}' का डेटाबेस नहीं मिला। कृपया स्पेलिंग चेक करें।"

# ==============================================================================
# [GLOBAL BRIDGE FUNCTIONS] - app.py से कॉल करने के लिए आसान शॉर्टकट्स
# ==============================================================================

# इंजन को मेमोरी में लोड करना (Singleton Pattern)
# यह बार-बार API क्लाइंट बनाने से रोकेगा और कोड को 10x फ़ास्ट करेगा।
raja_gateway = RajaIntelligenceGateway()

def raja_web_search(query: str) -> str:
    """app.py से इंटरनेट सर्च के लिए कॉल करें"""
    return raja_gateway.fetch_live_search(query)

def raja_weather_engine(city: str = "Bareilly") -> str:
    """app.py से मौसम की जानकारी के लिए कॉल करें"""
    return raja_gateway.fetch_live_weather(city)

# ========================== END OF KERNEL =====================================
