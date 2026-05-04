import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# 1. सुरक्षा और कॉन्फ़िगरेशन (Streamlit Secrets से)
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error("API Key नहीं मिली! कृपया .streamlit/secrets.toml चेक करें।")

# 2. शक्तिशाली विज़न फंक्शन
def get_raja_vision_response(prompt, image_data):
    # gemini-1.5-flash सबसे तेज़ और पावरफुल है विज़न के लिए
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt, image_data])
    return response.text

# 3. इमेज को प्रोसेस करने वाला फंक्शन
def prep_image(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("कोई फाइल अपलोड नहीं की गई")

# 4. Streamlit UI सेटअप (प्रोफेशनल लुक)
st.set_page_config(page_title="Raja AI - Multi-Modal", page_icon="👑", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2e7d32; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.header("👑 RAJA AI - Powerful Vision System")
st.write("---")

# लेआउट: दो कॉलम (एक फोटो के लिए, एक इनपुट के लिए)
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 इमेज अपलोड करें")
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="आपकी तस्वीर", use_container_width=True)

with col2:
    st.subheader("💬 Raja AI से पूछें")
    user_prompt = st.text_area("तस्वीर के बारे में विस्तार से पूछें (उदा: इसमें क्या लिखा है? या इस खाने में कितनी कैलोरी है?):", 
                               placeholder="यहाँ लिखें...", height=150)
    
    submit = st.button("Analyze with Raja AI 🚀")

# 5. परिणाम दिखाना
if submit:
    if uploaded_file is not None:
        with st.spinner("Raja AI सोच रहा है... 🧠"):
            try:
                img_data = prep_image(uploaded_file)
                # अगर यूजर ने कुछ नहीं लिखा तो डिफ़ॉल्ट प्रॉम्प्ट
                final_prompt = user_prompt if user_prompt else "इस तस्वीर के बारे में विस्तार से बताओ।"
                
                response = get_raja_vision_response(final_prompt, img_data[0])
                
                st.success("विश्लेषण पूरा हुआ!")
                st.markdown("### 🤖 Raja AI का जवाब:")
                st.info(response)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("भाई, पहले एक फोटो तो डालो! 😅")

# फूटर
st.write("---")
st.caption("Powered by Raja AI Development Team | Bareilly Division")
