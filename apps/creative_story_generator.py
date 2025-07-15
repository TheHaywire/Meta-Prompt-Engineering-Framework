from src.core.engine import MetaPromptEngine
import asyncio
from rich.console import Console
from rich.panel import Panel

async def generate_story(seed):
    engine = MetaPromptEngine()
    console = Console()
    prompt = f"Write a creative, engaging story based on this seed: {seed}"
    result = await engine.process_prompt(
        prompt=prompt,
        model="models/gemma-3-1b-it",
        context="Creative writing",
        user_preferences={"genre": "fiction", "length": "medium"}
    )
    console.print(Panel(f"[bold]Story Seed:[/bold] {seed}\n\n[bold]Generated Story:[/bold]\n{result.output}", border_style="cyan"))

if __name__ == "__main__":
    import sys
    seed = sys.argv[1] if len(sys.argv) > 1 else "A robot discovers a hidden garden on Mars."
    asyncio.run(generate_story(seed)) 