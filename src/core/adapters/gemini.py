import os
import asyncio
from typing import Optional, Dict, Any

class GeminiAdapter:
    """
    Adapter for Gemini API integration.
    Handles API key loading, prompt generation, and error handling.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set in environment.")
        try:
            import google.generativeai as genai
            self.genai = genai
            self.genai.configure(api_key=self.api_key)
        except ImportError:
            raise ImportError("google-generativeai package not installed. Please install with 'pip install google-generativeai'.")

    async def generate(self, prompt: str, model: str, context: Optional[str] = None, user_preferences: Optional[Dict[str, Any]] = None) -> str:
        """
        Generate a completion using the Gemini API.
        """
        full_prompt = prompt
        if context:
            full_prompt = f"[CONTEXT: {context}]\n" + full_prompt
        if user_preferences:
            prefs = ', '.join(f"{k}: {v}" for k, v in user_preferences.items())
            full_prompt = f"[USER_PREFERENCES: {prefs}]\n" + full_prompt
        try:
            model_obj = self.genai.GenerativeModel(model)
            response = await asyncio.to_thread(model_obj.generate_content, full_prompt)
            return response.text if hasattr(response, 'text') else str(response)
        except Exception as e:
            return f"[GeminiAdapter] Error: {str(e)}"
