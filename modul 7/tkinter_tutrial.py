import tkinter as tk
from tkinter import messagebox

def send_name():
    if first_name.get() == 'Emilia':
        messagebox.showinfo(title='OK!', message='Witam Panią!')
    else:
        messagebox.showerror(title='Kurza twarz', message='Nie znam Cię')
    print('click')

# tworzę obiekt
window = tk.Tk()

# obiekt ma różne metody
window.title('tutorial')
label = tk.Label(window, text="Jak masz na imię?")
# label zajmuje poszczególne wiersze dzięki pack, a dzięki grid mogłyby być obok siebie
label.pack()

#entry musi być przypisany do zmiennej, żeby dało się pobierać wartość, np w funkcji send_name
first_name = tk.Entry()
first_name.pack()

button = tk.Button(text="OK", command=send_name)
button.pack()

window.mainloop()
