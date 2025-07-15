from src.core.engine import MetaPromptEngine
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

async def prompt_to_code():
    engine = MetaPromptEngine()
    console = Console()
    console.print(Panel("[bold blue]Prompt to Code[/bold blue]\nDescribe what you want to build, and AI will generate code.", border_style="blue"))
    user_prompt = Prompt.ask("[bold green]Describe your coding task[/bold green]")
    prompt = f"Write Python code for the following task: {user_prompt}"
    result = await engine.process_prompt(
        prompt=prompt,
        model="models/gemma-3-1b-it",
        context="Code generation",
        user_preferences={"language": "python"}
    )
    console.print(Panel(f"[bold]Task:[/bold] {user_prompt}\n\n[bold]Generated Code:[/bold]\n{result.output}", border_style="green"))

if __name__ == "__main__":
    asyncio.run(prompt_to_code()) 