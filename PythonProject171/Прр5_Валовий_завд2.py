from tkinter import *

my_surname = "Валовий"

window = Tk()
window.title("Ппр5_"+my_surname+"_завд2")
window.geometry("320x200")

label_a = Label(window, text="Введіть a:")
label_a.place(x=30, y=30)

label_b = Label(window, text="Введіть b:")
label_b.place(x=30, y=70)

entry_a = Entry(window, width=10, bd=3)
entry_a.place(x=120, y=30)

entry_b = Entry(window, width=10, bd=3)
entry_b.place(x=120, y=70)

label_result_text = Label(window, text="Результат:")
label_result_text.place(x=30, y=150)

label_result = Label(window, text="", fg="blue", font=("Arial", 12, "bold"))
label_result.place(x=120, y=150)

def calculate():
    a = float(entry_a.get())
    b = float(entry_b.get())
    result = a * (4 * b - a)
    label_result.config(text=str(result))

button_calculate = Button(window, text="Обчислити", width=10, bg="lightblue", command=calculate)
button_calculate.place(x=120, y=110)

window.mainloop()
