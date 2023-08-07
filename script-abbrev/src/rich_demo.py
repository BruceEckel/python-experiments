import typer
from rich import print
from rich.console import Console
from rich.table import Table

console = Console()

data = {
    "name": "Rick",
    "age": 42,
    "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
    "active": True,
    "affiliation": None,
}


def main():
    print("Here's the data")
    print(data)
    print("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")
    table = Table("Name", "Item")
    table.add_row("Rick", "Portal Gun")
    table.add_row("Morty", "Plumbus")
    console.print(table)


if __name__ == "__main__":
    typer.run(main)
