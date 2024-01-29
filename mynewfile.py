import os
import tkinter as tk
from tkinter import filedialog, ttk

class DarkFileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Dark File Manager")

        # Dark theme colors
        bg_color = "#2E2E2E"
        fg_color = "white"

        # Style configuration for Treeview
        style = ttk.Style()
        style.configure("Treeview", background=bg_color, foreground=fg_color, fieldbackground=bg_color)
        style.configure("Treeview.Heading", background=bg_color, foreground=fg_color)

        self.root.configure(bg=bg_color)

        # Use Treeview widget for better file and directory display
        self.treeview = ttk.Treeview(root)
        self.treeview.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        # Button frame
        button_frame = tk.Frame(root, bg=bg_color)
        button_frame.pack(fill=tk.X, padx=10, pady=10)

        self.refresh_button = tk.Button(button_frame, text="Refresh", command=self.refresh, bg=bg_color, fg=fg_color)
        self.refresh_button.pack(side=tk.LEFT)

        self.open_button = tk.Button(button_frame, text="Open", command=self.open_file, bg=bg_color, fg=fg_color)
        self.open_button.pack(side=tk.LEFT)

        # Set initial directory
        self.current_path = os.getcwd()
        self.refresh()

    def refresh(self):
        # Clear the Treeview
        for i in self.treeview.get_children():
            self.treeview.delete(i)

        # Populate the Treeview with the current directory structure
        for dirpath, dirnames, filenames in os.walk(self.current_path):
            for filename in filenames:
                self.treeview.insert('', 'end', text=filename)

    def open_file(self):
        # Open the selected file
        selected_item = self.treeview.selection()[0]  # get selected item
        file_to_open = self.treeview.item(selected_item)['text']
        os.startfile(file_to_open)

root = tk.Tk()
dfm = DarkFileManager(root)
root.mainloop()