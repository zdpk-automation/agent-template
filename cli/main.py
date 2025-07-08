import typer

from cli.commands import init, list

app = typer.Typer()

app.add_typer(init.app, name="init", help="Initialize a new project or content.")
app.add_typer(list.app, name="list", help="List available templates or other resources.")

@app.callback()
def main():
    """
    A CLI tool for managing agent templates and project generation.
    """
    pass

if __name__ == "__main__":
    app()