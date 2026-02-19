import os
import json
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

class AIChatbot:
    def __init__(self):
        """Initialize the AI Chatbot with Groq API"""
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.conversation_history = []
        self.model_meta_70b = "llama-3.1-70b-versatile"
        self.model_google_gemma = "gemma-7b-it"
        
    def add_message(self, role, content):
        """Add message to conversation history"""
        self.conversation_history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
    
    def get_chat_history(self):
        """Get chat history without timestamps for API"""
        return [
            {"role": msg["role"], "content": msg["content"]}
            for msg in self.conversation_history[-10:]  # Last 10 messages
        ]
    
    def stream_response(self, user_message, model="llama"):
        """Get streaming response from Groq API"""
        try:
            # Add user message to history
            self.add_message("user", user_message)
            
            # Select model
            selected_model = (
                self.model_meta_70b if model == "llama" 
                else self.model_google_gemma
            )
            
            # Create message for API
            messages = self.get_chat_history()
            
            # Get streaming response
            response_text = ""
            with self.client.messages.stream(
                model=selected_model,
                messages=messages,
                max_tokens=1024,
                temperature=0.7,
            ) as stream:
                for text in stream.text_stream:
                    response_text += text
                    yield text
            
            # Add assistant response to history
            self.add_message("assistant", response_text)
            
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            print(error_msg)
            yield error_msg
    
    def get_conversation_history(self):
        """Get formatted conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
    
    def save_conversation(self, filename="conversation.json"):
        """Save conversation to file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_history, f, indent=2, ensure_ascii=False)
            return f"✅ Conversation saved to {filename}"
        except Exception as e:
            return f"❌ Error saving conversation: {str(e)}"
    
    def load_conversation(self, filename="conversation.json"):
        """Load conversation from file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.conversation_history = json.load(f)
            return f"✅ Conversation loaded from {filename}"
        except Exception as e:
            return f"❌ Error loading conversation: {str(e)}"
