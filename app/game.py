import typer
from Timer import Timer
from rich import print
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from rich.padding import Padding


app = typer.Typer(add_completion=True)

@app.callback(invoke_without_command=True)
def main():
    actions = {
        'manger': manger,
        'dormir': dormir,
        'baiser': sex,
    }

    choices = []

    for action in actions:
        choices.append(action)


    console = Console()

    inventory = Table(title='Inventory')
    inventory.add_column('Item', justify="left", style='green')
    inventory.add_column('quantity', justify="right", style='cyan')

    user_input = Prompt.ask("Entrez 'start' pour commencer l'aventure (ou 'stop' pour quitter à tout moment.) :sunglasses: ", default="start")
    while True:
        if user_input.lower() == "stop":
            break
        if user_input.lower() == "start":
            print(f">> Vous avez saisi : {user_input}")
            print("[bold red]Welcome to Bruybruyland[/bold red]")
            user_input = Prompt.ask("Que voulez-vous faire ?" , choices=choices)

        if user_input.lower() == "manger":
            print(Padding(f">> Vous avez saisi : {user_input}"))
            print(Padding("[bold]Vous mangez une pomme verte[/bold]"))
            print(Padding("[bold green][ +1 ] Pomme verte[/bold green] [bold blue]has been added to[/bold blue] [bold yellow]your inventory[/bold yellow]", (2,0,1,0)))

            inventory.add_row("Pomme", "1")
            console.print(inventory)

            user_input = Prompt.ask("Que voulez-vous faire ?" , choices=choices)

        else:
            print(f"Vous avez saisi : {user_input}")
            user_input = Prompt.ask("Que voulez-vous faire ?" , choices=choices)


@app.command()
def game():
    pass
   
@app.command()
def manger():
    pass

@app.command()
def dormir():
    pass

@app.command()
def sex():
    pass


# def asking(choices):
#     return Prompt.ask(Prompt.ask("Que voulez-vous faire ?" , choices=choices))

if __name__ == "__main__":
    app()