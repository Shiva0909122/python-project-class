from flask import Flask, render_template, request, redirect
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

# Database setup
DB_FILE = "database.db"
if not os.path.exists(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount REAL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to add a new expense
def add_expense(category, amount, date):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)", (category, amount, date))
    conn.commit()
    conn.close()

# Function to get all expenses
def get_expenses():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    return df

# Function to generate expense report
def generate_report():
    df = get_expenses()
    if df.empty:
        return

    category_expense = df.groupby("category")["amount"].sum()

    plt.figure(figsize=(8,5))
    sns.barplot(x=category_expense.index, y=category_expense.values, palette="coolwarm")
    plt.xticks(rotation=45)
    plt.title("Expense by Category")
    plt.ylabel("Total Spent ($)")
    plt.savefig("static/expense_chart.png")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        category = request.form["category"]
        amount = float(request.form["amount"])
        date = request.form["date"]
        add_expense(category, amount, date)
        return redirect("/")

    expenses = get_expenses()
    generate_report()
    return render_template("index.html", expenses=expenses.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
