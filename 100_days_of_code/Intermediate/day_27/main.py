import tkinter
FONT = ("Arial", 16, "normal")

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

def convert(): 
    user_input = int(input.get())
    kms = round(user_input*1.609)
    output_label.config(text=kms)

input =        tkinter.Entry(width=10)
equal_label =  tkinter.Label(text="is equal to", font=FONT)
miles_label =  tkinter.Label(text="Miles", font=FONT)
km_label =     tkinter.Label(text="Km", font=FONT)
output_label = tkinter.Label(text="0", font=FONT)
button =       tkinter.Button(text="Calculate", command=convert)

input.grid       (column=1, row=0)
equal_label.grid (column=0, row=1)
miles_label.grid (column=2, row=0)
km_label.grid    (column=2, row=1)
output_label.grid(column=1, row=1)
button.grid      (column=1, row=2)

window.mainloop()