from parser import Parser

class Application:
    def __init__(self, repository):
        parser = Parser()
        self.arguments = parser.parse_args()
        self.repository = repository

    def main(self):
        match self.arguments.action:
            case 'list': self.list()
            case 'stats': self.stats()
            case 'delete': self.delete(self.arguments.id)
            case 'add_income': self.add_income(
                self.arguments.name,
                self.arguments.category,
                self.arguments.date,
                self.arguments.value
            )
            case 'add_expense': self.add_expense(
                self.arguments.name,
                self.arguments.category,
                self.arguments.date,
                self.arguments.value
            )
                

    def list(self):
        print('Lista wydatków')
        for item in self.repository.get_items():
            print(item)

    def stats(self):
        print('Statystyki')
        for item in self.repository.get_stats():
            print(item)

    def delete(self, item_id: int):
        self.repository.delete_item(item_id)
        print('Usuwam')

    def add_income(self, name, category, date, value):
        print('Dodaję przychód')
        self.repository.add_item(name, category, date, value)

    def add_expense(self, name, category, date, value):
        self.repository.add_item(name, category, date, value * -1)
        print('Dodaję wydatek')
