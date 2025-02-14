import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import os

# CSV file to store progress
DATA_FILE = "progress.csv"

# Check if the file exists, if not create one
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Date", "Weight", "Workout (min)", "Calories"])
    df.to_csv(DATA_FILE, index=False)

# Function to add a new record
def add_record():
    date = entry_date.get()
    weight = entry_weight.get()
    workout = entry_workout.get()
    calories = entry_calories.get()

    if not date or not weight or not workout or not calories:
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return

    new_data = pd.DataFrame([[date, float(weight), int(workout), int(calories)]], 
                            columns=["Date", "Weight", "Workout (min)", "Calories"])
    
    df = pd.read_csv(DATA_FILE)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

    messagebox.showinfo("Success", "Record added successfully!")
    entry_date.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    entry_workout.delete(0, tk.END)
    entry_calories.delete(0, tk.END)

# Function to plot progress charts
def show_progress():
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        messagebox.showwarning("No Data", "No records found! Add some data first.")
        return
    
    df["Date"] = pd.to_datetime(df["Date"])
    df.sort_values("Date", inplace=True)

    plt.figure(figsize=(10,5))

    plt.subplot(2,1,1)
    plt.plot(df["Date"], df["Weight"], marker="o", label="Weight (kg)", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Weight (kg)")
    plt.title("Weight Progress")
    plt.legend()
    
    plt.subplot(2,1,2)
    plt.plot(df["Date"], df["Calories"], marker="s", label="Calories Burned", color="red")
    plt.xlabel("Date")
    plt.ylabel("Calories")
    plt.title("Calories Burned Over Time")
    plt.legend()

    plt.tight_layout()
    plt.show()

# GUI Setup
app = tk.Tk()
app.title("Fitness Progress Tracker")
app.geometry("400x400")

tk.Label(app, text="Date (YYYY-MM-DD):").pack()
entry_date = tk.Entry(app)
entry_date.pack()

tk.Label(app, text="Weight (kg):").pack()
entry_weight = tk.Entry(app)
entry_weight.pack()

tk.Label(app, text="Workout Duration (min):").pack()
entry_workout = tk.Entry(app)
entry_workout.pack()

tk.Label(app, text="Calories Burned:").pack()
entry_calories = tk.Entry(app)
entry_calories.pack()

tk.Button(app, text="Add Record", command=add_record).pack(pady=5)
tk.Button(app, text="Show Progress", command=show_progress).pack(pady=5)

app.mainloop()
