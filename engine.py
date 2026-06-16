import logging
from tavily import TavilyClient

# लॉगिंग सेटअप
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [RAJA-AI-CORE] : %(message)s")

class RajaLiveSearchEngine:
    def __init__(self):
       import streamlit as st
# कोड के अंदर डायरेक्ट की लिखने की बजाय ऐसे कॉल करें:
self.client = TavilyClient(api_key=st.secrets["TAVILY_API_KEY"])
        logging.info("Tavily Live Search Engine एक्टिवेटेड।")

    def fetch_live_data(self, query: str) -> str:
        try:
            logging.info(f"Tavily से लाइव डेटा निकाला जा रहा है: '{query}'")
            # AI के लिए कस्टमाइज्ड सर्च
            response = self.client.search(query=query, max_results=3)
            
            intel_string = "--- SATELLITE LIVE DATA INTERCEPTED ---\n"
            for index, result in enumerate(response['results'], start=1):
                intel_string += f"[{index}] शीर्षक: {result['title']}\n"
                intel_string += f"जानकारी: {result['content']}\n"
                intel_string += f"स्रोत लिंक: {result['url']}\n\n"
            intel_string += "----------------------------------------"
            return intel_string
            
        except Exception as e:
            logging.error(f"Tavily सर्च एरर: {str(e)}")
            return "सर्च इंजन इस समय लाइव डेटा फेच नहीं कर पा रहा है।"

# app.py के लिए ब्रिज फंक्शन
def raja_web_search(query: str) -> str:
    engine = RajaLiveSearchEngine()
    return engine.fetch_live_data(query)
