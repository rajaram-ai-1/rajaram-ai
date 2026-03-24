import os
import base64
import requests
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
from tavily import TavilyClient
import replicate
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

app = FastAPI()

# UI Connection Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Clients
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
ELEVENLABS_KEY = os.getenv("ELEVENLABS_API_KEY")

# --- SHAKTI 1: Taja Khabar (Internet Search) ---
def get_live_news(query):
    try:
        search = tavily_client.search(query=query, search_depth="advanced", max_results=3)
        context = "\n".join([r['content'] for r in search['results']])
        return context
    except:
        return "Internet se judne mein dikkat ho rahi hai."

# --- SHAKTI 2: Photo/Video Banana (Replicate) ---
def create_media(prompt, type="image"):
    try:
        if type == "image":
            # FLUX model for high quality images
            output = replicate.run("black-forest-labs/flux-schnell", input={"prompt": prompt})
            return output[0]
        else:
            # Video Generation
            output = replicate.run("stability-ai/stable-video-diffusion", input={"input_image": prompt})
            return output[0]
    except:
        return None

# --- SHAKTI 3: Insaani Awaaz (ElevenLabs) ---
def text_to_human_voice(text):
    try:
        url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM" # Male Voice ID
        headers = {"xi-api-key": ELEVENLABS_KEY, "Content-Type": "application/json"}
        data = {"text": text, "model_id": "eleven_multilingual_v2", "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}}
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode('utf-8')
    except:
        return None

# --- MAIN ENGINE: Raja AI Brain ---
@app.post("/raja-ai-chat")
async def raja_ai_process(message: str = Form(...), image: UploadFile = File(None)):
    user_msg = message.lower()
    final_reply = ""
    media_url = None
    voice_data = None

    # 1. Vision Check (Llama-3-Vision)
    vision_info = ""
    if image:
        vision_info = "[Raja AI is looking at the photo...]" 
        # Note: In production, upload image to cloud and send URL to Groq-Vision

    # 2. News/Live Info Check
    news_context = ""
    if any(word in user_msg for word in ["news", "khabar", "mausam", "today", "live"]):
        news_context = get_live_news(user_msg)

    # 3. Media Creation Check
    if "photo banao" in user_msg or "image" in user_msg:
        media_url = create_media(message, "image")
        final_reply = "Malik, maine aapke liye ek sundar photo banayi hai."
    elif "video banao" in user_msg:
        media_url = create_media(message, "video")
        final_reply = "Malik, video taiyar hai!"

    # 4. Thinking Process (Groq)
    if not final_reply:
        system_msg = f"Your name is Raja AI. You are a super AI with vision and internet powers. Use this context: {news_context}. Be polite and human-like."
        chat = groq_client.chat.completions.create(
            messages=[{"role": "system", "content": system_msg}, {"role": "user", "content": message}],
            model="llama3-70b-8192"
        )
        final_reply = chat.choices[0].message.content

    # 5. Voice Generation
    voice_data = text_to_human_voice(final_reply)

    return {
        "reply": final_reply,
        "media": media_url,
        "voice": voice_data
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
