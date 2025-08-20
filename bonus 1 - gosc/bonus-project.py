import typer

def print_hi(name: str):
    print(f'Hi, {name}')

if __name__ == '__main__':
    typer.run(print_hi)