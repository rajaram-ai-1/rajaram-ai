Import logging
import time
from typing import List, Dict, Optional
from googlesearch import search

# 1. एडवांस लॉगिंग सेटअप (टर्मिनल में प्रो-लेवल आउटपुट के लिए)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [RAJA-AI-CORE] : %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class RajaLiveSearchEngine:
    """
    Raja AI Omnipotent Core - Live Internet Data Extraction Module.
    Author: Rajaram (CEO & Chief Architect)
    """
    
    def __init__(self, max_results: int = 3, delay: float = 1.5):
        """
        सिस्टम को इनिशियलाइज़ करता है।
        :param max_results: कितने रिज़ल्ट्स चाहिए।
        :param delay: गूगल के एंटी-बॉट सिस्टम से बचने के लिए स्लीप टाइम।
        """
        self.max_results = max_results
        self.delay = delay
        logging.info("RajaLiveSearchEngine इनिशियलाइज़ हो गया है। सिस्टम लाइव डेटा के लिए तैयार है।")

    def fetch_live_data(self, query: str) -> Optional[List[Dict[str, str]]]:
        """
        इंटरनेट से लाइव डेटा कैप्चर करता है।
        """
        logging.info(f"टारगेट क्वेरी प्रोसेस हो रही है: '{query}'")
        extracted_data = []
        
        try:
            # एडवांस पैरामीटर्स के साथ लाइव सर्च
            results = search(query, num_results=self.max_results, advanced=True)
            
            for index, result in enumerate(results, start=1):
                # डेटा पैकेट तैयार करना
                data_packet = {
                    "rank": index,
                    "title": result.title,
                    "snippet": result.description,
                    "source_url": result.url
                }
                extracted_data.append(data_packet)
                logging.info(f"डेटा पैकेट {index} सफलतापूर्वक कैप्चर किया गया: {result.title[:30]}...")
                
                # सर्वर को ब्लॉक करने से रोकने के लिए स्मार्ट डिले
                time.sleep(self.delay)

            logging.info(f"डेटा एक्सट्रैक्शन पूरा हुआ। कुल {len(extracted_data)} रिज़ल्ट्स मिले।")
            return extracted_data

        except Exception as e:
            logging.error(f"लाइव डेटा लिंक टूट गया या सिस्टम एरर: {str(e)}")
            return None

# ==========================================
# 2. सिस्टम एग्जीक्यूशन ब्लॉक (Testing Area)
# ==========================================
if __name__ == "__main__":
    # राजा AI का सर्च मॉड्यूल एक्टिवेट करें
    raja_search = RajaLiveSearchEngine(max_results=3, delay=1.0)
    
    # आप यहाँ कोई भी क्वेरी डाल सकते हैं
    target_query = "आज की सबसे बड़ी टेक्नोलॉजी न्यूज़"
    
    # डेटा फेच करें
    live_results = raja_search.fetch_live_data(target_query)
    
    # रिज़ल्ट्स को टर्मिनल पर साफ-सुथरे तरीके से प्रिंट करें
    if live_results:
        print("\n" + "="*60)
        print("👑 RAJA AI - OMNIPOTENT LIVE DATA STREAM 👑")
        print("="*60)
        for item in live_results:
            print(f"[{item['rank']}] {item['title']}")
            print(f"    > जानकारी : {item['snippet']}")
            print(f"    > लिंक    : {item['source_url']}\n")
        print("="*60)
