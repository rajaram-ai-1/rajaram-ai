import google.generativeai as genai
import streamlit as st
from PIL import Image
import logging

def raja_vision_engine(uploaded_file, prompt=""):
    """🔱 RAJA AI: SELF-HEALING VISION KERNEL"""
    try:
        # १. की-प्रोटोकॉल
        api_key = st.secrets.get("GEMINI_API_KEY")
        if not api_key:
            return "❌ सुरक्षा त्रुटि: GEMINI_API_KEY अनुपस्थित है।"
        
        genai.configure(api_key=api_key)
        
        # २. ऑटो-डिस्कवरी: उपलब्ध सबसे शक्तिशाली मॉडल ढूंढना (404 एरर का अंत)
        def get_best_model():
            allowed_models = ["gemini-1.5-pro", "gemini-1.5-flash", "gemini-1.0-pro-vision"]
            for m in genai.list_models():
                if any(model_name in m.name for model_name in allowed_models):
                    return m.name
            return "gemini-1.5-flash" # फॉलबैक

        model_path = get_best_model()
        model = genai.GenerativeModel(model_path)
        
        # ३. विज़न प्रोसेसिंग (Binary Processing)
        img = Image.open(uploaded_file)
        
        # ४. न्यूरल प्रॉम्प्ट इंजीनियरिंग (Superior Reasoning)
        system_instruction = """
        तुम 'Raja AI' के विज़न मॉड्यूल हो, जिसे राजाराम द्वारा विकसित किया गया है।
        तुम्हारा काम तस्वीर का नैनो-स्तर पर विश्लेषण करना है। 
        - अगर टेक्स्ट है, तो उसे सटीक transcribe करो।
        - अगर कोई जटिल वस्तु है, तो उसका वैज्ञानिक विवरण दो।
        - हिंदी भाषा में जवाब दो और अपनी शैली 'सुप्रीम और प्रोफेशनल' रखो।
        """
        
        # ५. क्वांटम जनरेशन (Streaming Response Simulation)
        response = model.generate_content([system_instruction, prompt, img])
        
        # लॉगिंग के लिए टेलीमेट्री
        logging.info(f"Vision Success using model: {model_path}")
        
        return response.text
        
    except Exception as e:
        # क्रैश होने के बजाय, यह इंजन खुद को री-पोर्ट करेगा
        err_msg = f"🔱 Vision Kernel Mutation: {str(e)}"
        logging.error(err_msg)
        return err_msg
