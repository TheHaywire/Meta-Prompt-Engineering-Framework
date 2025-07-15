from src.core.engine import MetaPromptEngine
import asyncio
from rich.console import Console
from rich.panel import Panel

def get_debate_roles():
    return [
        ("Pro", "Argue in favor of the topic."),
        ("Con", "Argue against the topic.")
    ]

async def ai_debate(topic):
    engine = MetaPromptEngine()
    console = Console()
    roles = get_debate_roles()
    console.print(Panel(f"[bold blue]AI Debate Club[/bold blue]\nDebate Topic: [bold]{topic}[/bold]", border_style="blue"))
    for role, instruction in roles:
        prompt = f"Debate the topic: '{topic}'. {instruction}"
        result = await engine.process_prompt(
            prompt=prompt,
            model="models/gemma-3-1b-it",
            context=f"Debater: {role}",
            user_preferences={"debate_role": role}
        )
        console.print(Panel(f"[bold]{role} Argument:[/bold]\n{result.output}", border_style="magenta" if role=="Pro" else "red"))

if __name__ == "__main__":
    import sys
    topic = sys.argv[1] if len(sys.argv) > 1 else "Should AI be regulated?"
    asyncio.run(ai_debate(topic)) 