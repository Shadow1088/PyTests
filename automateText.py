import pyautogui
import time

def type_text(text, interval=0.3):
    for char in text:
        pyautogui.press(char)
        

if __name__ == "__main__":
    text_to_type = "ahoj Tome, jak se mas, mam se fajn\n"
    for i in range(25):
        type_text(text_to_type)
        