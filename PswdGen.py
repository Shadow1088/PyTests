import tkinter as tk
from tkinter import filedialog, messagebox
import random

root = tk.Tk()
root.geometry("500x250")
root.title("PswdGen")
root.resizable(False, False)

randomChoice = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9", "0"]
pswd = []

def pswdShow():
    textbox = tk.Entry(root, font=("arial", 12))
    textbox.insert(0, ''.join(pswd))  # insert the password into the Entry widget
    textbox.place(x=200, y=150)
    textbox.select_range(0, 'end')  # select all text in textbox
    textbox.focus()  # set focus on textbox

def pswdGen():
    global pswd
    pswd = [] 
    try:
        for i in range(int(lenEntry.get())):
            k = random.choice(randomChoice)
            pswd.append(k)
    except: pass
    random.shuffle(pswd)

    if pswd != []:
        button2 = tk.Button(
            root,
            text="Copy",
            font=("arial", 12),
            command=btn_click2)
        button2.place(x=430, y=140)

        button3 = tk.Button(
            root,
            text="Expand/Shrink",
            font=("arial", 12),
            command=btn_click3)
        button3.place(x=200, y=200)

    pswdShow()

def pswdCopy():
    root.clipboard_clear()
    root.clipboard_append(''.join(pswd))

def btn_click():
    pswdGen()
    
def btn_click2():
    pswdCopy()

def btn_click3():
    
    global Expand
    if Expand == "Expand":
        Expand = "Shrink"
        root.geometry("500x250")
    else:
        Expand = "Expand"
        root.geometry("500x500")    
Expand = "Shrink"

def btn_click4():
    #save
    content = []
    global path
    password = ''.join(pswd)
    try:
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                content.append(line)
            content.append(f"{infoEntry.get()}: {password}\n")
        with open(path, "w") as file:
            file.writelines(content)
    except: messagebox.showerror("Error", "No such file or directory.")


def btn_click5():
    global path
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    label5.config(text=f"Current path: {path}")

label = tk.Label(
    root,
    text="Password Generator - ZZ",
    font=("arial", 18))
label.place(x=90, y=0)

label2 = tk.Label(
    root,
    text="Enter the length of the password: ",
    font=("arial", 12))
label2.place(x=50, y=60)

label3 = tk.Label(
    root,
    text="Your password: ",
    font=("arial", 12))
label3.place(x=50, y=150)

label4 = tk.Label(
    root,
    text=pswd,
    font=("arial", 12))
label4.place(x=200, y=150)

path = ""
label5 = tk.Label(
    root,
    text=f"Current path: {path}",
    font=("arial", 12))
label5.place(x=50, y=350)

label6 = tk.Label(
    root,
    text="Additional info: ",
    font=("arial", 12))
label6.place(x=50, y=413)

label7 = tk.Label(
    root,
    text="(optional)",
    font=("arial", 6))
label7.place(x=50, y=440)

label8 = tk.Label(
    root,
    text="(path=*.txt)",
    font=("arial", 6))
label8.place(x=430, y=440)

lenEntry = tk.Entry(
    root,
    width=3)
lenEntry.place(x=360, y=63)

infoEntry = tk.Entry(
    root,
    width=21,
    font=("arial", 12))
infoEntry.place(x=190, y=415)

button = tk.Button(
    root,
    text="Generate",
    font=("arial", 12),
    command=btn_click)
button.place(x=200, y=100)

button4 = tk.Button(
    root,
    text="Save",
    font=("arial", 12),
    command=btn_click4)
button4.place(x=430, y=405)

button5 = tk.Button(
    root,
    text="Choose path",
    font=("arial", 12),
    command=btn_click5)
button5.place(x=200, y=300)

root.mainloop()

#  USER WILL CHOOSE LENGHT, yes
#  TAKE USER INPUT AND GENERATE TEXT USER CAN COPY OR/AND BUTTON THAT COPIES IT, yes
#  USER WILL CHOOSE WHERE TO STORE PASSWORDS (PATH), yes
#  USER WILL BE ABLE TO ADD COMMENT TO PASSWORD SAVE, yes