from src.core.engine import MetaPromptEngine
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

async def optimize_prompt():
    engine = MetaPromptEngine()
    console = Console()
    console.print(Panel("[bold blue]Prompt Optimizer[/bold blue]\nEnter a prompt to receive suggestions for improvement.", border_style="blue"))
    user_prompt = Prompt.ask("[bold green]Enter your prompt[/bold green]")
    prompt = f"Analyze and suggest improvements for the following prompt: {user_prompt}"
    result = await engine.process_prompt(
        prompt=prompt,
        model="models/gemma-3-1b-it",
        context="Prompt engineering",
        user_preferences={"goal": "improvement"}
    )
    console.print(Panel(f"[bold]Original Prompt:[/bold] {user_prompt}\n\n[bold]Suggestions:[/bold]\n{result.output}", border_style="green"))

if __name__ == "__main__":
    asyncio.run(optimize_prompt()) 