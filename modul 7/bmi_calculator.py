import tkinter as tk

def oblicz_bmi():
    wzrost = float(entry_wzrost.get())
    waga = float(entry_waga.get())
    bmi = waga/(wzrost**2)
    label_wynik.config(text = "Twoje BMI wynosi : {:.2f}".format(bmi))

root = tk.Tk()
root.title("Kalkulator BMI")

label_wzrost = tk.Label(root, text = "Wzrost (w metrach):")
label_wzrost.grid(row=0, column=0)

entry_wzrost = tk.Entry(root)
entry_wzrost.grid(row = 0, column = 1)

label_waga = tk.Label(root, text = "Waga (w kilogramach):")
label_waga.grid(row=1, column=0)

entry_waga = tk.Entry(root)
entry_waga.grid(row = 1, column = 1)

button_oblicz = tk.Button(root, text = "Oblicz BMI", command=oblicz_bmi)
button_oblicz.grid(row=3, columnspan=2)

label_wynik = tk.Label(root, text="")
label_wynik.grid(row=3, columnspan=2)

root.mainloop()
