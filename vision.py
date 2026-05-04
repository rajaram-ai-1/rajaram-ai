import google.generativeai as genai
import streamlit as st
from PIL import Image

def raja_vision_engine(uploaded_file, prompt=""):
    """🔱 RAJA AI: विज़न इंजन (शक्तिशाली और सुरक्षित)"""
    try:
        # Secrets से चाबी उठाना
        api_key = st.secrets.get("GEMINI_API_KEY")
        if not api_key:
            return "❌ विज़न एरर: 'GEMINI_API_KEY' नहीं मिली। कृपया secrets.toml चेक करें।"
            
        genai.configure(api_key=api_key)
        
        # सबसे आधुनिक विज़न मॉडल (Flash 1.5)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # इमेज को प्रोसेस करना
        img = Image.open(uploaded_file)
        
        # अगर राजाराम भाई ने कुछ नहीं पूछा, तो AI अपनी मर्जी से सब कुछ बताएगा
        final_prompt = f"""
        तुम 'Raja AI' के विज़न मॉड्यूल हो। इस तस्वीर को बारीकी से देखो।
        अगर कोई सवाल है तो उसका जवाब दो: {prompt}
        अगर सवाल नहीं है, तो इस तस्वीर का पूरा विवरण हिंदी में दो।
        लिखा हुआ टेक्स्ट है तो उसे पढ़कर सुनाओ।
        """
        
        response = model.generate_content([final_prompt, img])
        return response.text
        
    except Exception as e:
        return f"🔱 Vision System Alert: {str(e)}"
