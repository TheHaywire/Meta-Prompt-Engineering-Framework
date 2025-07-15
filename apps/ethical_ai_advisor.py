from src.core.engine import MetaPromptEngine
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

async def ethical_advisor():
    engine = MetaPromptEngine()
    console = Console()
    console.print(Panel("[bold blue]Ethical AI Advisor[/bold blue]\nAnalyze a prompt for ethical risks and concerns.", border_style="blue"))
    user_prompt = Prompt.ask("[bold green]Enter your prompt[/bold green]")
    prompt = f"Analyze the following prompt for ethical risks, bias, and potential harm: {user_prompt}"
    result = await engine.process_prompt(
        prompt=prompt,
        model="models/gemma-3-1b-it",
        context="Ethical analysis",
        user_preferences={"goal": "ethics"}
    )
    console.print(Panel(f"[bold]Prompt:[/bold] {user_prompt}\n\n[bold]Ethical Analysis:[/bold]\n{result.output}", border_style="red"))

if __name__ == "__main__":
    asyncio.run(ethical_advisor()) 