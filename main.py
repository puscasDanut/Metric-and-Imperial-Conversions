from tkinter import *

if __name__ == '__main__':
    window = Tk()
    window.minsize(height=100, width=400)
    window.title("Metric and Imperial Conversions")

    empty_label = Label(text="", padx=50)
    empty_label.grid(column=0, row=0)

    input = Entry(width=10)
    input.grid(column=1, row=0, pady=10)

    initial_units = Label(text="Miles")
    initial_units.grid(column=2, row=0, padx=20)

    equals_label = Label(text="is equal to")
    equals_label.grid(column=0, row=1, pady=10)

    final_value = Label(text="0")
    final_value.grid(column=1, row=1)

    other_units = Label(text="Km")
    other_units.grid(column=2, row=1)


    window.mainloop()
