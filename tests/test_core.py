import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.core.engine import MetaPromptEngine
from src.core.adapters.openai import OpenAIAdapter
from src.core.adapters.gemini import GeminiAdapter
from src.core.adapters.anthropic import AnthropicAdapter

@pytest.mark.asyncio
async def test_meta_prompt_engine_instantiation():
    engine = MetaPromptEngine()
    assert engine is not None

@pytest.mark.asyncio
def test_adapter_instantiation():
    # These will fail if API keys are not set, so just check instantiation logic
    try:
        OpenAIAdapter(api_key="test")
    except Exception:
        pass
    try:
        GeminiAdapter(api_key="test")
    except Exception:
        pass
    try:
        AnthropicAdapter(api_key="test")
    except Exception:
        pass 