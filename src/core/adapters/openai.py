import os
import openai
from typing import Optional, Dict, Any

class OpenAIAdapter:
    """
    Adapter for OpenAI API integration.
    Handles API key loading, prompt generation, and error handling.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set in environment or provided.")
        openai.api_key = self.api_key

    async def generate(self, prompt: str, model: str, context: Optional[str] = None, user_preferences: Optional[Dict[str, Any]] = None) -> str:
        """
        Generate a completion using the OpenAI API.
        """
        full_prompt = prompt
        if context:
            full_prompt = f"[CONTEXT: {context}]\n" + full_prompt
        if user_preferences:
            prefs = ', '.join(f"{k}: {v}" for k, v in user_preferences.items())
            full_prompt = f"[USER_PREFERENCES: {prefs}]\n" + full_prompt
        try:
            response = await openai.ChatCompletion.acreate(
                model=model,
                messages=[{"role": "user", "content": full_prompt}],
                temperature=0.7,
                max_tokens=1024
            )
            return response.choices[0].message["content"].strip()
        except Exception as e:
            return f"[OpenAIAdapter] Error: {str(e)}"
