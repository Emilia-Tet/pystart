# można zamienić argumenty na opcje. Wtedy nie będą użyte w kolejności, w której je podaliśmy, tylko trzeba podac ich nazwy.
# już nie "python .\main.py Hi Maciej", tylko "python .\main.py --greet Hi --name Maciej"

import typer
from cli.greeting import app as greeting
from cli.gen import app as gen
from cli.system import app as system

app = typer.Typer()

app.add_typer(greeting, name='greeting')
app.add_typer(gen, name='gen', help='generator danych')
app.add_typer(system, name='system', help='Polecenia systemowe')

# if __name__ == '__main__':
#     typer.run(greeting)

if __name__ == '__main__':
    app()