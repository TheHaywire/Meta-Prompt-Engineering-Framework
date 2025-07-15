from src.core.engine import MetaPromptEngine
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

async def synthesize_domains():
    engine = MetaPromptEngine()
    console = Console()
    console.print(Panel("[bold blue]Cross-Domain Synthesizer[/bold blue]\nCombine knowledge from two fields for creative insights.", border_style="blue"))
    domain1 = Prompt.ask("[bold green]Enter the first domain[/bold green]")
    domain2 = Prompt.ask("[bold green]Enter the second domain[/bold green]")
    prompt = f"Synthesize knowledge from {domain1} and {domain2} to generate a novel insight or application."
    result = await engine.process_prompt(
        prompt=prompt,
        model="models/gemma-3-1b-it",
        context=f"Domains: {domain1}, {domain2}",
        user_preferences={"goal": "synthesis"}
    )
    console.print(Panel(f"[bold]Synthesis of {domain1} and {domain2}:[/bold]\n{result.output}", border_style="cyan"))

if __name__ == "__main__":
    asyncio.run(synthesize_domains()) 