from rich import console

console = console.Console()

def print_error(message: str):
    console.print(f"[bold red]Error: {message}[/bold red]")

def print_success(message: str):
    console.print(f"[bold green]Success: {message}[/bold green]")

def print_warning(message: str):
    console.print(f"[bold yellow]Warning: {message}[/bold yellow]")

def print_info(message: str):
    console.print(f"[bold blue]Info: {message}[/bold blue]")
