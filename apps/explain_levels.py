from src.core.engine import MetaPromptEngine
import asyncio
from rich.console import Console
from rich.panel import Panel

def get_level_info():
    return [
        ("like I'm 5", "child"),
        ("like I'm 15", "teen"),
        ("like I'm 50", "expert"),
    ]

async def explain_levels(topic):
    engine = MetaPromptEngine()
    levels = get_level_info()
    console = Console()
    for suffix, level in levels:
        prompt = f"Explain {topic} {suffix}."
        result = await engine.process_prompt(
            prompt=prompt,
            model="models/gemma-3-1b-it",
            context=f"User is a {level} learner.",
            user_preferences={"learning_style": "visual", "expertise_level": level}
        )
        console.print(Panel(f"[bold]{prompt}[/bold]\n\n{result.output}", border_style="green"))

if __name__ == "__main__":
    import sys
    topic = sys.argv[1] if len(sys.argv) > 1 else "quantum computing"
    asyncio.run(explain_levels(topic))
