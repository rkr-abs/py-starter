import typer
from calculator import calculator

app = typer.Typer()

@app.command()
def main( operator: str, x: float, y: float):

    typer.echo(f"Result: {calculator([operator,x,y])}")

if __name__ == "__main__":
    app()
