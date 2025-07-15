from src.core.engine import MetaPromptEngine
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

async def persona_simulator():
    engine = MetaPromptEngine()
    console = Console()
    console.print(Panel("[bold blue]Persona Simulator[/bold blue]\nChoose a persona and get AI responses in that style.", border_style="blue"))
    persona = Prompt.ask("[bold green]Enter a persona (e.g., Shakespeare, Elon Musk, Yoda)[/bold green]")
    user_prompt = Prompt.ask("[bold green]Enter your prompt[/bold green]")
    prompt = f"Respond as {persona}: {user_prompt}"
    result = await engine.process_prompt(
        prompt=prompt,
        model="models/gemma-3-1b-it",
        context=f"Persona: {persona}",
        user_preferences={"persona": persona}
    )
    console.print(Panel(f"[bold]{persona} says:[/bold]\n{result.output}", border_style="magenta"))

if __name__ == "__main__":
    asyncio.run(persona_simulator()) 