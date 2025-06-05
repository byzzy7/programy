import tkinter as tk

# Vytvoření hlavního okna
window = tk.Tk()
window.title("Kalkulačka")
window.minsize(200, 200)
window.resizable(False, False)

# Vytvoření proměnných pro vstupy
prvni_cislo = tk.StringVar()
druhe_cislo = tk.StringVar()
vysledek = tk.StringVar()

# Funkce pro výpočet
def vypocet():
    try:
        num1 = float(prvni_cislo.get())
        num2 = float(druhe_cislo.get())
        operator = operace.get()

        if operator == "+":
            vysledek.set(num1 + num2)
        elif operator == "-":
            vysledek.set(num1 - num2)
        elif operator == "*":
            vysledek.set(num1 * num2)
        elif operator == "/":
            if num2 != 0:
                vysledek.set(num1 / num2)
            else:
                vysledek.set("Nejded dělit nulou")
    except ValueError:
        vysledek.set("Není co počítat")

# Vytvoření widgetů
label1 = tk.Label(window, text="První číslo:", font=("Arial", 10))
label1.pack(pady=5)
entry1 = tk.Entry(window, textvariable=prvni_cislo, font=("Arial", 10))
entry1.pack(pady=5)
label2 = tk.Label(window, text="Druhé číslo:", font=("Arial", 10))
label2.pack(pady=5)
entry2 = tk.Entry(window, textvariable=druhe_cislo, font=("Arial", 10))
entry2.pack(pady=5)
label3 = tk.Label(window, text="Výsledek:", font=("Arial", 10))
label3.pack(pady=5)
entry3 = tk.Entry(window, textvariable=vysledek, state='readonly', font=("Arial", 10))
entry3.pack(pady=5)

# Výběr operace
operace = tk.StringVar(value="+")
operace_frame = tk.Frame(window)
operace_frame.pack(pady=5)
for znak in ["+", "-", "*", "/"]:
    radio = tk.Radiobutton(operace_frame, text=znak, variable=operace, value=znak, font=("Arial", 10))
    radio.pack(side=tk.LEFT)

# Tlačítko pro výpočet
button = tk.Button(window, text="Vypočítat", command=vypocet, font=("Arial", 10))
button.pack(pady=10)

# Tlačítko pro ukončení
exit_button = tk.Button(window, text="Ukončit", command=window.quit, font=("Arial", 10))
exit_button.pack(pady=5)

if __name__ == "__main__":
    #spuštění porgramu
    window.mainloop()