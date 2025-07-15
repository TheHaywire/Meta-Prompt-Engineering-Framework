from src.core.engine import MetaPromptEngine
import asyncio
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

def print_intro():
    console = Console()
    console.print(Panel("[bold blue]Prompt Playground[/bold blue]\nType your prompt and see AI responses in real time! Type 'exit' to quit.", border_style="blue"))

async def playground():
    engine = MetaPromptEngine()
    console = Console()
    print_intro()
    while True:
        user_prompt = Prompt.ask("[bold green]Enter your prompt[/bold green]")
        if user_prompt.strip().lower() == "exit":
            break
        result = await engine.process_prompt(
            prompt=user_prompt,
            model="models/gemma-3-1b-it"
        )
        console.print(Panel(f"[bold]Prompt:[/bold] {user_prompt}\n\n[bold]AI Response:[/bold]\n{result.output}", border_style="green"))

if __name__ == "__main__":
    asyncio.run(playground()) 