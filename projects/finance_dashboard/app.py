from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)
            return analyze_data(file_path)
    return render_template("upload.html")

def analyze_data(file_path):
    df = pd.read_csv(file_path)
    
    # Assume columns: Date, Category, Amount
    category_expense = df.groupby("Category")["Amount"].sum()

    # Plot
    plt.figure(figsize=(8,5))
    sns.barplot(x=category_expense.index, y=category_expense.values)
    plt.xticks(rotation=45)
    plt.title("Expense by Category")
    plt.savefig("static/expense_chart.png")
    
    return render_template("index.html", categories=category_expense.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
