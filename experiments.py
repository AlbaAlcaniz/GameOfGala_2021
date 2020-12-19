from tkinter import *

root = Tk()
root.title("hello")

Message(root, text=48*'xxxxx ').grid(row=0, column=0, columnspan=3)

Label(root, text='Name:').grid(row=1, column=0)
Entry(root, width=50).grid(row=1, column=1)
Button(root, text="?").grid(row=1, column=2)

Button(root, text="Left").grid(row=2, column=0)
Button(root, text="Center").grid(row=2, column=1)
Button(root, text="Right").grid(row=2, column=2)

root.mainloop()