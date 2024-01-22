import os
import sys
import time
import shutil
import send2trash
import tkinter as tk
from tkinter import filedialog

tk.Tk()

cwd = os.getcwd() # get current working directory

def ls(): 
    for file in os.listdir(cwd):
        print(file)

def cd(path): os.chdir(path); print(os.getcwd() + ":") 

def mkdir(path): os.mkdir(path)
    
def rmdir(path): os.rmdir(path)
    
def rm(path): os.remove(path)
    
def mv(src, dst): shutil.move(src, dst)

def goback(): os.chdir(".."); #print(os.getcwd() + ":")

while True:
    cwd = os.getcwd() # get current working directory
    print(os.getcwd() + ":")
    ## handling input
    cmd = input()
    cmd = cmd.split(" ")
    try:
        if cmd[0] == "ls": ls()
        elif cmd[0] == "cd": cd(cmd[1])
        elif cmd[0] == "mkdir": mkdir(cmd[1])
        elif cmd[0] == "rmdir":rmdir(cmd[1])
        elif cmd[0] == "rm": rm(cmd[1])
        elif cmd[0] == "mv": mv(cmd[1], cmd[2])
        elif cmd[0] == "exit" or "kys" or "kill": break
        elif cmd[0] == "goback": goback()
        else: print("invalid command")
    except: print("error")


    
