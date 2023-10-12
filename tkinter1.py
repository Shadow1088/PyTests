import tkinter as tk

root = tk.Tk()

root.geometry("1200x500")
root.title("Yep")

label0 =tk.Label(root, text = "kys", font = ("Arial",18))
label0.pack()

def button_click():
    label1 =tk.Label(root, text = "You clicked", font = ("Arial",18))
    label1.pack()

button0 = tk.Button(root, text= "Click", command=(button_click))
button0.pack()



root.mainloop()
