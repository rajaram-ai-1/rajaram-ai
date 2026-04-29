# =============================================================
# RAJA AI - SATELLITE SEARCH MODULE (engine.py)
# =============================================================
from duckduckgo_search import DDGS
import datetime
import requests
from bs4 import BeautifulSoup

def raja_web_search(query):
    """🛰️ DuckDuckGo से लाइव डेटा खींचने वाली शक्ति"""
    try:
        with DDGS() as ddgs:
            # ताज़ा जानकारी के लिए आज की तारीख जोड़ना
            full_query = f"{query} today {datetime.date.today()}"
            results = [r['body'] for r in ddgs.text(full_query, max_results=5)]
            if results:
                return "\n---\n".join(results)
            return "सैटेलाइट लिंक में कोई ताज़ा डेटा नहीं मिला।"
    except Exception as e:
        return f"🔱 Search Engine Failure: {str(e)}"

def raja_link_reader(url):
    """🔱 लिंक के अंदर घुसकर जानकारी निकालने वाली शक्ति"""
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=header, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # कचरा हटाना
        for script in soup(["script", "style"]):
            script.decompose()
            
        text = soup.get_text()
        # साफ़ सफाई
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text[:2000] # सिर्फ शुरुआती 2000 अक्षर
    except Exception as e:
        return f"🔱 Link Reader Error: {e}"
