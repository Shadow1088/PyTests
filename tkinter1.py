import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("The 1st GUI!")

label = tk.Label(root, text="Yoyoyyo", font=("arial", 18))
label.pack()

root.mainloop()
