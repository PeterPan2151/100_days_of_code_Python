import tkinter


def convert():
    miles = int(my_input.get())
    kms = miles * 1.609
    amount_converted_label.config(text=round(kms, 3))


window = tkinter.Tk()
window.title('Miles to Kms Converter')
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

my_input = tkinter.Entry(width=10)
my_input.grid(column=1, row=0)
my_input.focus()

my_label = tkinter.Label(text='Miles')
my_label.grid(column=2, row=0)

my_label2 = tkinter.Label(text='is equal to')
my_label2.grid(column=0, row=1)

amount_converted_label = tkinter.Label(text='0')
amount_converted_label.grid(column=1, row=1)

my_label3 = tkinter.Label(text='Km')
my_label3.grid(column=2, row=1)

button = tkinter.Button(text='Calculate', command=convert)
button.grid(column=1, row=2)


window.mainloop()
