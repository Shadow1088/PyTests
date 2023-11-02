import tkinter as tk

x = True

while x == True:

    root = tk.Tk()

    root.geometry("800x500")
    root.title("The 1st GUI!")

    label = tk.Label(root, text="x = True :skull:", font=("arial", 18))
    label.pack()

    root.mainloop()