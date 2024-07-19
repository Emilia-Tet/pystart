# kolejność: Kacepr zaczął od zbudowania interfejsu krok po kroku i od wyświetlania danych
# abs to wartość bezwzględna
# jeśli zmienna jest poza funkcją, to możemy mieć do niej dostęp, ale nie możemy jej modyfikowac (chyba, że zrobimy z niej global)

import tkinter as tk
from tkinter import messagebox
from random import randint

def reset_game():
    global previous_difference, steps, target
    previous_difference = None
    steps = 0
    target = randint(1,50)
    field.delete(0, tk.END)  # Wyczyść pole tekstowe

def on_submit():
    global previous_difference, steps

    steps += 1
  
    value = int(field.get())
    difference = abs(target - value)

    if value > 50:
        messagebox.showinfo('Stan', f'Podałeś liczbę większą niż 50. Szukaj w zakresie 1-50.')
    if previous_difference == 0:
        messagebox.showinfo('Stan', f'Gratulacje! Chodziło właśnie o tę liczbę! Zgadłeś w {steps} krokach.')
        if messagebox.askyesno('Gra zakończona', 'Czy chcesz zagrać jeszcze raz?'):
                reset_game()
        else:
                window.quit()


    elif previous_difference == None or difference < previous_difference:
        messagebox.showinfo('Stan', 'Robi się cieplej')

    else:
        messagebox.showinfo('Stan', 'Robi się zimniej')

    previous_difference = difference

steps = 0
previous_difference = None
target = randint(1,50)

window = tk.Tk()
window.title('Zgadnij liczbę')
label = tk.Label(window, text="Zgadnij liczbe od 1 do 50")
label.pack()

field = tk.Entry()
field.pack()

button = tk.Button(text="Zgaduje!", command=on_submit)
button.pack()

window.mainloop()
