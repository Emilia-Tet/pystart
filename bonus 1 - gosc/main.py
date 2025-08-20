# można zamienić argumenty na opcje. Wtedy nie będą użyte w kolejności, w której je podaliśmy, tylko trzeba podac ich nazwy.
# już nie "python .\main.py Hi Maciej", tylko "python .\main.py --greet Hi --name Maciej"

import typer

def print_hi(
        yell: bool = typer.Option(False, help="Krzyk", prompt="Krzyk?"),
        greet: str =  typer.Option("Hi", help="Pozdrowienie", prompt="Pozdrowienie"),
        name: str =  typer.Option("World", help="Imię do pozdrowienia", prompt="Imię")
        ):
    '''Program do pozdrawiania'''
    if yell:
        typer.echo(typer.style(
            f'{greet}, {name} !!!',
            fg=typer.colors.BRIGHT_WHITE,
            bg=typer.colors.BRIGHT_RED
            ))
    else:
        typer.echo(f'{greet}, {name}')

if __name__ == '__main__':
    typer.run(print_hi)