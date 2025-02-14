import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import pandas as pd
import matplotlib.pyplot as plt
import os

# List to store expenses
expenses = []

# Function to save expenses to CSV
def save_expenses():
    df = pd.DataFrame(expenses)
    df.to_csv("expenses.csv", index=False)

# Function to load expenses from CSV
def load_expenses():
    global expenses
    if os.path.exists("expenses.csv"):
        df = pd.read_csv("expenses.csv")
        expenses = df.to_dict('records')

# Function to add expense to the list
def add_expense():
    description = description_entry.get()
    amount = amount_entry.get()
    category = category_var.get()
    date = date_entry.get()

    if not description or not amount or not category or not date:
        messagebox.showerror("Error", "All fields are required.")
        return
    
    try:
        expense = {"description": description, "amount": float(amount), "category": category, "date": date}
        expenses.append(expense)
        save_expenses()  # Save to local storage
        messagebox.showinfo("Success", "Expense added successfully!")
        clear_fields()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

# Function to clear the input fields
def clear_fields():
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    date_entry.set_date("")

# Function to show all expenses
def show_expenses():
    if len(expenses) == 0:
        messagebox.showinfo("Info", "No expenses recorded.")
        return

    show_window = tk.Toplevel(root)
    show_window.title("All Expenses")
    show_window.geometry("400x300")
    
    text_box = tk.Text(show_window, wrap=tk.WORD)
    text_box.pack(expand=True, fill='both')

    for expense in expenses:
        text_box.insert(tk.END, f"Description: {expense['description']}\nAmount: {expense['amount']}\nCategory: {expense['category']}\nDate: {expense['date']}\n\n")

# Function to generate expense report by category
def generate_report():
    if len(expenses) == 0:
        messagebox.showinfo("Info", "No expenses recorded.")
        return

    df = pd.DataFrame(expenses)
    df_category = df.groupby("category")["amount"].sum().reset_index()

    # Plotting the bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(df_category["category"], df_category["amount"], color='skyblue')
    
    # Adding amount inside each bar
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, 
                height - (height * 0.15),  # Position text inside the bar
                f'{height:.2f}', 
                ha='center', 
                va='bottom', 
                color='black', 
                fontsize=10, 
                fontweight='bold')

    plt.title("Expense Breakdown by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    plt.show()

# GUI Window
root = tk.Tk()
root.title("Expense Tracker 💰")
root.geometry("450x450")
root.configure(bg="#2C3E50")

# Main Frame
main_frame = tk.Frame(root, bg="#34495E", padx=20, pady=20)
main_frame.pack(expand=True, fill='both')

# UI Elements
tk.Label(main_frame, text="Description:", fg="white", bg="#34495E", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=5)
description_entry = tk.Entry(main_frame, width=30)
description_entry.grid(row=0, column=1, pady=5)

tk.Label(main_frame, text="Amount:", fg="white", bg="#34495E", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", pady=5)
amount_entry = tk.Entry(main_frame, width=30)
amount_entry.grid(row=1, column=1, pady=5)

tk.Label(main_frame, text="Category:", fg="white", bg="#34495E", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", pady=5)
category_var = tk.StringVar(root)
category_var.set("Food")
category_menu = ttk.Combobox(main_frame, textvariable=category_var, values=["Food", "Transport", "Bills", "Entertainment", "Others"], state="readonly")
category_menu.grid(row=2, column=1, pady=5)

tk.Label(main_frame, text="Date:", fg="white", bg="#34495E", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", pady=5)
date_entry = DateEntry(main_frame, width=27, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
date_entry.grid(row=3, column=1, pady=5)

# Buttons
add_button = tk.Button(main_frame, text="Add Expense", command=add_expense, bg="#3498DB", fg="white", font=("Helvetica", 12), width=15)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

show_button = tk.Button(main_frame, text="Show All Expenses", command=show_expenses, bg="#2ECC71", fg="white", font=("Helvetica", 12), width=15)
show_button.grid(row=5, column=0, columnspan=2, pady=10)

report_button = tk.Button(main_frame, text="Generate Report", command=generate_report, bg="#E74C3C", fg="white", font=("Helvetica", 12), width=15)
report_button.grid(row=6, column=0, columnspan=2, pady=10)

# Load existing expenses on startup
load_expenses()

root.mainloop()
