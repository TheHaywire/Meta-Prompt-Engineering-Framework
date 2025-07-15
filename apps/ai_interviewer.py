from src.core.engine import MetaPromptEngine
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

async def ai_interview(role):
    engine = MetaPromptEngine()
    console = Console()
    console.print(Panel(f"[bold blue]AI Interviewer[/bold blue]\nRole: [bold]{role}[/bold]", border_style="blue"))
    for i in range(3):
        prompt = f"Ask a challenging interview question for the role of {role}."
        result = await engine.process_prompt(
            prompt=prompt,
            model="models/gemma-3-1b-it",
            context=f"Interview round {i+1}",
            user_preferences={"role": role, "difficulty": "medium"}
        )
        console.print(Panel(f"[bold]Question {i+1}:[/bold] {result.output}", border_style="yellow"))
        _ = Prompt.ask("[bold green]Your answer[/bold green]")

if __name__ == "__main__":
    import sys
    role = sys.argv[1] if len(sys.argv) > 1 else "Software Engineer"
    asyncio.run(ai_interview(role)) 