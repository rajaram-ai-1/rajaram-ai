# =============================================================
# RAJA AI - SATELLITE SEARCH MODULE (engine.py)
# =============================================================
from duckduckgo_search import DDGS
import datetime
import requests
from bs4 import BeautifulSoup

def raja_web_search(query):
    """🛰️ SUPREME SEARCH: भारत के ताज़ा लाइव डेटा के साथ"""
    try:
        with DDGS() as ddgs:
            # भारत (India) के लिए क्षेत्र सेट करना (Region: in-en)
            full_query = f"{query}"
            
            # परिणामों में Title और Link भी शामिल करें
            results = ddgs.text(
                full_query, 
                region='in-en', 
                safesearch='off', 
                timelimit='d', # 'd' मतलब पिछले 24 घंटे की ताज़ा खबरें
                max_results=5
            )
            
            if results:
                intel_output = []
                for r in results:
                    source = f"\n📍 Source: {r['title']} ({r['href']})\nInfo: {r['body']}\n"
                    intel_output.append(source)
                
                return "\n---\n".join(intel_output)
            
            return "🛰️ सैटेलाइट लिंक में कोई ताज़ा डेटा नहीं मिला।"
    except Exception as e:
        return f"🔱 Search Engine Failure: {str(e)}"

def raja_link_reader(url):
    """🔱 DEEP SCAN: वेबसाइट के अंदर का गुप्त डेटा निकालना"""
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        # Timeout को कम रखा है ताकि ऐप हैंग न हो
        response = requests.get(url, headers=header, timeout=7)
        response.raise_for_status() # अगर लिंक खराब है तो एरर दे देगा
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # फालतू चीज़ें हटाना
        for element in soup(["script", "style", "nav", "footer", "header"]):
            element.decompose()
            
        text = soup.get_text(separator=' ')
        # फालतू स्पेस हटाना
        clean_text = " ".join(text.split())
        
        return clean_text[:3000] # अब 3000 अक्षर तक बढ़ाया (ज्यादा डेटा = बेहतर जवाब)
    except Exception as e:
        return f"🔱 Link Reader Error: {e}"
