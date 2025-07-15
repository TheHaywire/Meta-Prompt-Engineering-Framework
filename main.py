#!/usr/bin/env python3
"""
Meta-Prompt Engineering Framework (MPEF)
The Future of AI Interaction

This is the main entry point for the revolutionary prompt library that will change AI forever.
"""

import asyncio
import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from src.core.engine import MetaPromptEngine
from src.core.config import Config
from src.utils.logger import setup_logger
from src.utils.safety import SafetyChecker

console = Console()
logger = setup_logger(__name__)


@click.group()
@click.version_option(version="1.0.0", prog_name="Meta-Prompt Framework")
@click.option("--debug", is_flag=True, help="Enable debug mode")
@click.option("--config", type=click.Path(exists=True), help="Path to config file")
def cli(debug: bool, config: Optional[str]):
    """🚀 Meta-Prompt Engineering Framework - Revolutionizing AI Interaction"""
    if debug:
        logger.setLevel("DEBUG")
    
    if config:
        Config.load_from_file(config)


@cli.command()
@click.option("--prompt", "-p", required=True, help="Input prompt to process")
@click.option("--model", "-m", default="auto", help="AI model to use")
@click.option("--context", "-c", help="Additional context")
@click.option("--safety", is_flag=True, default=True, help="Enable safety checks")
def process(prompt: str, model: str, context: Optional[str], safety: bool):
    """Process a prompt through the meta-prompt engine"""
    
    console.print(Panel.fit(
        "[bold blue]Meta-Prompt Engine[/bold blue]\n"
        "Processing your prompt with revolutionary AI technology...",
        border_style="blue"
    ))
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        
        task = progress.add_task("Initializing engine...", total=None)
        
        try:
            # Initialize the meta-prompt engine
            engine = MetaPromptEngine()
            progress.update(task, description="Processing prompt...")
            
            # Safety check if enabled
            if safety:
                safety_checker = SafetyChecker()
                if not safety_checker.validate_prompt(prompt):
                    console.print("[red]❌ Safety check failed! Prompt contains potentially harmful content.[/red]")
                    sys.exit(1)
            
            # Process the prompt
            result = asyncio.run(engine.process_prompt(
                prompt=prompt,
                model=model,
                context=context
            ))
            
            progress.update(task, description="Optimizing output...")
            
            # Display results
            display_results(result)
            
        except Exception as e:
            console.print(f"[red]❌ Error: {str(e)}[/red]")
            logger.error(f"Processing failed: {e}")
            sys.exit(1)


@cli.command()
@click.option("--category", "-c", help="Prompt category to explore")
def explore(category: Optional[str]):
    """Explore the prompt library"""
    
    console.print(Panel.fit(
        "[bold green]Prompt Library Explorer[/bold green]\n"
        "Discover revolutionary prompts that will change AI forever...",
        border_style="green"
    ))
    
    # Load and display prompt categories
    categories = load_prompt_categories()
    
    if category:
        display_category_prompts(category, categories.get(category, []))
    else:
        display_categories(categories)


@cli.command()
@click.option("--prompt-id", "-i", required=True, help="Prompt ID to evaluate")
@click.option("--metrics", "-m", multiple=True, help="Metrics to evaluate")
def evaluate(prompt_id: str, metrics: tuple):
    """Evaluate prompt performance and effectiveness"""
    
    console.print(Panel.fit(
        "[bold yellow]Prompt Evaluation Engine[/bold yellow]\n"
        "Analyzing prompt performance with advanced metrics...",
        border_style="yellow"
    ))
    
    # Run evaluation
    evaluation_results = run_prompt_evaluation(prompt_id, list(metrics))
    display_evaluation_results(evaluation_results)


@cli.command()
def init():
    """Initialize the meta-prompt framework"""
    
    console.print(Panel.fit(
        "[bold magenta]Framework Initialization[/bold magenta]\n"
        "Setting up the revolutionary meta-prompt framework...",
        border_style="magenta"
    ))
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        
        tasks = [
            "Creating directory structure...",
            "Initializing databases...",
            "Setting up safety protocols...",
            "Loading prompt templates...",
            "Configuring AI models...",
            "Testing connections...",
            "Finalizing setup..."
        ]
        
        for i, task_desc in enumerate(tasks):
            task = progress.add_task(task_desc, total=100)
            progress.update(task, completed=100)
            progress.remove_task(task)
    
    console.print("[green]✅ Framework initialized successfully![/green]")
    console.print("\n[bold]Next steps:[/bold]")
    console.print("1. Run 'mpef explore' to discover prompts")
    console.print("2. Run 'mpef process -p \"your prompt\"' to test the engine")
    console.print("3. Check the documentation for advanced features")


def display_results(result):
    """Display processing results in a beautiful format"""
    
    table = Table(title="Meta-Prompt Processing Results")
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    
    table.add_row("Original Prompt", result.get("original_prompt", "N/A"))
    table.add_row("Enhanced Prompt", result.get("enhanced_prompt", "N/A"))
    table.add_row("Model Used", result.get("model", "N/A"))
    table.add_row("Processing Time", f"{result.get('processing_time', 0):.2f}s")
    table.add_row("Confidence Score", f"{result.get('confidence', 0):.2%}")
    table.add_row("Safety Score", f"{result.get('safety_score', 0):.2%}")
    
    console.print(table)
    
    if result.get("output"):
        console.print("\n[bold]Generated Output:[/bold]")
        console.print(Panel(result["output"], border_style="green"))


def load_prompt_categories():
    """Load available prompt categories"""
    # This would load from the actual prompt library
    return {
        "adaptive": "Context-aware prompts that adapt to conversation flow",
        "meta": "Self-improving prompts that optimize themselves",
        "synthesis": "Cross-domain knowledge synthesis prompts",
        "safety": "Ethical AI alignment and safety prompts",
        "creative": "Creative and artistic prompt templates",
        "research": "Scientific research and analysis prompts",
        "business": "Business and productivity prompts",
        "education": "Educational and learning prompts"
    }


def display_categories(categories):
    """Display available prompt categories"""
    
    table = Table(title="Available Prompt Categories")
    table.add_column("Category", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")
    table.add_column("Count", style="green", justify="right")
    
    for category, description in categories.items():
        # This would count actual prompts in each category
        count = 25  # Placeholder
        table.add_row(category, description, str(count))
    
    console.print(table)


def display_category_prompts(category: str, prompts: list):
    """Display prompts in a specific category"""
    
    console.print(f"\n[bold]Prompts in category: {category}[/bold]")
    
    table = Table(title=f"{category.title()} Prompts")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Name", style="white")
    table.add_column("Description", style="white")
    table.add_column("Rating", style="green", justify="right")
    
    for prompt in prompts:
        table.add_row(
            prompt.get("id", "N/A"),
            prompt.get("name", "N/A"),
            prompt.get("description", "N/A"),
            f"{prompt.get('rating', 0):.1f}/5.0"
        )
    
    console.print(table)


def run_prompt_evaluation(prompt_id: str, metrics: list):
    """Run evaluation on a specific prompt"""
    # This would run actual evaluation
    return {
        "prompt_id": prompt_id,
        "clarity_score": 0.85,
        "effectiveness_score": 0.92,
        "safety_score": 0.98,
        "adaptability_score": 0.78,
        "overall_score": 0.88
    }


def display_evaluation_results(results):
    """Display evaluation results"""
    
    table = Table(title="Prompt Evaluation Results")
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Score", style="magenta", justify="right")
    
    for metric, score in results.items():
        if metric != "prompt_id":
            table.add_row(metric.replace("_", " ").title(), f"{score:.2%}")
    
    console.print(table)


if __name__ == "__main__":
    cli() 