import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import datetime

# Create the main window
root = tk.Tk()
root.title("Note App")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# Function to save notes
def save_note():
    note_title = simpledialog.askstring("Note Title", "Enter note title:")
    if note_title:
        note_content = text_box.get("1.0", "end-1c")
        if note_content:
            with open(f"{note_title}.txt", "w") as file:
                file.write(note_content)
            messagebox.showinfo("Success", "Note saved successfully!")
        else:
            messagebox.showwarning("Warning", "Note cannot be empty!")
    else:
        messagebox.showwarning("Warning", "Title cannot be empty!")

# Function to load a saved note
def load_note():
    note_title = simpledialog.askstring("Load Note", "Enter note title to load:")
    if note_title and os.path.exists(f"{note_title}.txt"):
        with open(f"{note_title}.txt", "r") as file:
            note_content = file.read()
        text_box.delete("1.0", "end")
        text_box.insert("1.0", note_content)
    else:
        messagebox.showinfo("Info", "Note not found.")

# Function to clear the text box
def clear_note():
    text_box.delete("1.0", "end")

# Function to update the date and time
def update_datetime():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datetime_label.config(text=f"Date & Time: {now}")
    root.after(1000, update_datetime)

# Create a heading label
heading_label = tk.Label(root, text="Simple Note App", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
heading_label.pack(pady=10)

# Create a label for date and time
datetime_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="#555")
datetime_label.pack()
update_datetime()

# Create a label for description
description_label = tk.Label(root, text="Note Description:", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333")
description_label.pack(pady=5)

# Create a text box for note input
text_box = tk.Text(root, wrap="word", height=15, width=55, font=("Arial", 12), bd=2, relief="sunken")
text_box.pack(pady=10, padx=20)

# Create a frame for buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

# Create buttons for save, load, and clear
save_button = tk.Button(button_frame, text="Save Note", command=save_note, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=12)
save_button.grid(row=0, column=0, padx=5)

load_button = tk.Button(button_frame, text="Load Note", command=load_note, bg="#2196F3", fg="white", font=("Arial", 10, "bold"), width=12)
load_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear Note", command=clear_note, bg="#F44336", fg="white", font=("Arial", 10, "bold"), width=12)
clear_button.grid(row=0, column=2, padx=5)

root.mainloop()