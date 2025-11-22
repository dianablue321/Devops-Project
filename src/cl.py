import typer
from infra_simulator import prompt_user

app = typer.Typer()

@app.command()
def create_vm():
    """Prompt for a new VM and store configuration."""
    prompt_user()

if __name__ == "__main__":
    app()
