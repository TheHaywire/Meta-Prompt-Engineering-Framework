import importlib
import pytest

APP_MODULES = [
    "explain_levels",
    "prompt_playground",
    "ai_debate_club",
    "creative_story_generator",
    "ai_interviewer",
    "prompt_optimizer",
    "cross_domain_synthesizer",
    "ethical_ai_advisor",
    "persona_simulator",
    "prompt_to_code",
]

@pytest.mark.parametrize("app_module", APP_MODULES)
def test_app_import_and_main(app_module):
    mod = importlib.import_module(f"apps.{app_module}")
    assert mod is not None 