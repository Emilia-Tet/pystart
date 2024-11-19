import sqlite3


# można dać INTEGER DEFAULT 0
with sqlite3.connect('todos.db') as connection:
    sql = ''' CREATE TABLE IF NOT EXISTS todos(
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name VARCHAR(100) UNIQUE NOT NULL,
    is_done INTEGER
    )'''

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()



while True:
    print("Oto Twoja lista zadań do zrobienia: ")
    with sqlite3.connect('todos.db') as connection:
        cursor = connection.cursor()
        for task in cursor.execute('SELECT task_id, task_name, is_done FROM todos'):
            if task[2] == 0:
                print(f"{task[0]}. {task[1]}")
    print(5*"-----------------")

    print('Co chcesz zrobić?')
    answer = input('''
    0 - dodaj nowe zadanie
    1 - Ustaw zadanie jako zrealizowane.
    Którą czynność chcesz wykonać?
    Q - Wyjdź z programu
                   ''')

    if answer == '0':
        with sqlite3.connect('todos.db') as connection:
            cursor = connection.cursor()
            new_task = input("Podaj treść nowego zadania: ")
            cursor.execute(
            'INSERT INTO todos(task_name, is_done) VALUES(?, ?)', 
            (new_task, '0')
            )
            connection.commit()
        

    elif answer =='1':
        given_id = input("Podaj ID zadania, które chcesz oznaczyć jako wykonane: ")
        with sqlite3.connect('todos.db') as connection:
            cursor = connection.cursor()
            cursor.execute(f'UPDATE todos SET is_done = 1 WHERE task_id = {given_id}')
            connection.commit()


    elif answer =="Q":
        print("Twoja lista to do pozdrawia Cię serdecznie, do zobaczenia następnym razem!")
        break

    else:
        print("nie wiem co chcesz zrobić.")
    
quit()