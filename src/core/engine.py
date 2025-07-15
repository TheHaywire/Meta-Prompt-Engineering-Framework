import asyncio
from src.core.adapters.gemini import GeminiAdapter
from src.core.adapters.openai import OpenAIAdapter
from src.core.adapters.anthropic import AnthropicAdapter

class MetaPromptEngine:
    def __init__(self):
        self.adapters = {
            "gemini": GeminiAdapter(),
            "gemma": GeminiAdapter(),  # Gemma is handled by GeminiAdapter
            "openai": OpenAIAdapter(),
            "anthropic": AnthropicAdapter(),
        }

    def _get_adapter(self, model):
        if model.startswith("models/gemini") or model.startswith("models/gemma"):
            return self.adapters["gemini"]
        elif model.startswith("gpt-") or model.startswith("text-"):
            return self.adapters["openai"]
        elif model.startswith("claude"):
            return self.adapters["anthropic"]
        else:
            raise ValueError(f"No adapter found for model: {model}")

    async def process_prompt(self, prompt, model, context=None, user_preferences=None):
        adapter = self._get_adapter(model)
        output = await adapter.generate(prompt, model, context, user_preferences)
        class Result:
            pass
        result = Result()
        result.original_prompt = prompt
        result.enhanced_prompt = f"[CONTEXT: {context}]\n[USER_PREFERENCES: {user_preferences}]\n{prompt}"
        result.output = output
        result.safety_score = 1.0  # Placeholder
        result.confidence_score = 1.0  # Placeholder
        return result 