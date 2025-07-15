import os
from typing import Optional, Dict, Any

class AnthropicAdapter:
    """
    Adapter for Anthropic API integration.
    Handles API key loading, prompt generation, and error handling.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not set in environment or provided.")
        try:
            import anthropic
            self.anthropic = anthropic
            self.client = anthropic.AsyncAnthropic(api_key=self.api_key)
        except ImportError:
            raise ImportError("anthropic package not installed. Please install with 'pip install anthropic'.")

    async def generate(self, prompt: str, model: str, context: Optional[str] = None, user_preferences: Optional[Dict[str, Any]] = None) -> str:
        """
        Generate a completion using the Anthropic API.
        """
        full_prompt = prompt
        if context:
            full_prompt = f"[CONTEXT: {context}]\n" + full_prompt
        if user_preferences:
            prefs = ', '.join(f"{k}: {v}" for k, v in user_preferences.items())
            full_prompt = f"[USER_PREFERENCES: {prefs}]\n" + full_prompt
        try:
            response = await self.client.completions.create(
                model=model,
                prompt=full_prompt,
                max_tokens_to_sample=1024,
                temperature=0.7
            )
            return response.completion.strip()
        except Exception as e:
            return f"[AnthropicAdapter] Error: {str(e)}"
