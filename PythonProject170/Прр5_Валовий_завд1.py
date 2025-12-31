from tkinter import *

my_surname = "Валовий"
my_class = "8-Б1"

window = Tk()
window.title("Прр5_"+my_surname+"_завд1")
window.geometry("400x150")

entry = Entry(window, width=15, bd=3)
entry.pack(pady=30)

def on_click():
    entry.delete(0, END)
    entry['bg'] = 'red'
    entry['font'] = ('Arial', 14)
    entry['width'] += 20
    entry['fg'] = 'white'
    entry.insert(0, "Ми використовуємо властивості поля! ")

Button = Button(window, text=my_class, width=10, fg="blue", bg="yellow", command=on_click)
Button.pack(pady=10)

window.mainloop()


