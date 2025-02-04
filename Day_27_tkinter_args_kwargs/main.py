import tkinter


def button_clicked():
    new_text = my_input.get()
    my_label.config(text=new_text)


# Create window object
window = tkinter.Tk()
# Title of the window
window.title("My First GUI Program")
# minimum size independent of min. elements
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label object, we create it, ONLY CREATE IT, BUT NOT ADDED OT THE WINDOW
my_label = tkinter.Label(text='I am a label', font=('Arial', 24))
# THIS PUTS IT ON THE WINDOW
my_label.grid(column=0, row=0)

# buttons
button = tkinter.Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

button_2 = tkinter.Button(text='new Button')
button_2.grid(column=2, row=0)


# Entry component
my_input = tkinter.Entry(width=10)
my_input.grid(column=3, row=2)
my_input.focus()

# This keeps the window open
window.mainloop()
