import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned marksheet data
file_path = "marksheet.csv" # Update if needed
df_marksheet = pd.read_csv(file_path)

# Compute Total Marks, Average Marks, and Grade (if not already computed)
df_marksheet["Total Marks"] = df_marksheet[["Science", "English", "History", "Maths"]].sum(axis=1)
df_marksheet["Average Marks"] = df_marksheet["Total Marks"] / 4

# Assign grades based on average marks
def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

df_marksheet["Grade"] = df_marksheet["Average Marks"].apply(assign_grade)

# Set Seaborn style
sns.set_style("whitegrid")

# 1. Histogram of Subject Scores
plt.figure(figsize=(12, 6))
df_marksheet[["Science", "English", "History", "Maths"]].plot(kind="hist", alpha=0.6, bins=20, figsize=(12, 6))
plt.title("Distribution of Marks in Different Subjects")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend(["Science", "English", "History", "Maths"])
plt.grid(True)
plt.show()

# 2. Bar Chart of Top 10 Students by Average Marks
plt.figure(figsize=(12, 6))
top_students = df_marksheet.sort_values(by="Average Marks", ascending=False).head(10)  # Top 10 students
plt.bar(top_students["Name"], top_students["Average Marks"], color="skyblue")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.title("Top 10 Students by Average Marks")
plt.xticks(rotation=45)
plt.show()

# 3. Pie Chart of Grade Distribution
grade_counts = df_marksheet["Grade"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%", colors=sns.color_palette("pastel"))
plt.title("Grade Distribution Among Students")
plt.show()

# 4. Boxplot for Marks Distribution
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_marksheet[["Science", "English", "History", "Maths"]])
plt.title("Boxplot of Marks in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
