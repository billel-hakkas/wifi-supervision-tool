
import rich
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
import typer
from database.db_manager import all_devices
from database.db_manager import inserting_data 

app=typer.Typer()
console=Console()
@app.command()
def init():
    rich.print("[bold red]Initialisation du scanner[/bold red]")

    liste= all_devices()
    if not liste:
        message=Panel("Votre base de donnée est vide. Commencer par scannner votre wifi avec la commande 'scanner'",border_style="red")
        console.print(message)
    else:
        message=Panel ("Votre base de donnée est déja initialiser. Vous pouvez poursuivre sur des commandes plus poussée",border_style="green")
        console.print(message)
    


@app.command()
def scan():
    """Lance un scan du réseau Wi-Fi."""
    print("Scan en cours...")


@app.command()
def inserting():
    inserting_data()


@app.command()
def display():
    table=Table(title="Résultat du scan wifi")
    table.add_column("Nom de l'appareil",justify="right",style="cyan",no_wrap=True)
    table.add_column("Mac",justify="right",style="magenta")
    table.add_column("IP",justify="right",style="red")
    table.add_column("OS",justify="right",style="green")

    liste=all_devices()
    for appareil in liste:
        table.add_row(appareil['nom'],appareil['mac'],appareil['ip'],appareil['os'])

    console.print(table)


if __name__ == "__main__":
    app()