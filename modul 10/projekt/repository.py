class Repository:
    def __init__(self, connection):
        self.connection = connection

    def add_item(self, name:str, category:str, date:str, value:float):
        category_id = self.get_or_create_category(category)
        sql = 'INSERT INTO items VALUES(null, ?, ?, ?, ?)'
        cursor = self.connection.cursor()
        cursor.execute(sql, (name, category_id, value, date))

    def get_or_create_category(self, name):
        cursor = self.connection.cursor()
        cursor.execute('SELECT id FROM categories WHERE name=?', (name,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute('INSERT INTO categories VALUES(null, ?)', (name,))
            self.connection.commit()
            category_id = cursor.lastrowid
        else:
            category_id = result[0]

        return category_id
    
    def delete_item(self, item_id):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM items WHERE id=?', (item_id,))
        cursor.execute('DELETE FROM categories WHERE id=?', (item_id,))
        self.connection.commit()

    def get_items(self):
        cursor = self.connection.cursor()
        return cursor.execute('SELECT * FROM items')
    
    def get_stats(self):
        cursor = self.connection.cursor()
        return cursor.execute('''SELECT strftime('%m', date) as month, SUM(amount) as total 
                       FROM items
                       GROUP BY month''')