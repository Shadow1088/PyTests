import tkinter as tk

x = False

while x == True:

    root = tk.Tk()

    root.geometry("800x500")
    root.title("The 1st GUI!")

    label = tk.Label(root, text="Filip smokes weed", font=("arial", 18))
    label.pack()

    root.mainloop()