from dotenv import load_dotenv
load_dotenv()

from src.core.engine import MetaPromptEngine
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown

async def run_gemma_example():
    console = Console()
    engine = MetaPromptEngine()
    model_name = "models/gemma-3-1b-it"
    result = await engine.process_prompt(
        prompt="Explain quantum computing in simple terms.",
        model=model_name,
        context="User is a beginner in technology.",
        user_preferences={"learning_style": "visual", "expertise_level": "beginner"}
    )

    # Print a visually appealing summary
    console.print(Panel("[bold blue]Meta-Prompt Framework Output[/bold blue]", border_style="blue"))

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="white")
    table.add_row("[b]Original Prompt[/b]", result.original_prompt)
    table.add_row("[b]Enhanced Prompt[/b]", result.enhanced_prompt)
    table.add_row("[b]Model Used[/b]", model_name)
    table.add_row("[b]Safety Score[/b]", str(result.safety_score))
    table.add_row("[b]Confidence Score[/b]", str(result.confidence_score))
    console.print(table)

    console.print(Panel("[bold green]AI Response[/bold green]", border_style="green"))
    console.print(Markdown(result.output))

if __name__ == "__main__":
    asyncio.run(run_gemma_example()) 