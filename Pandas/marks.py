import pandas as pd

# Load the marksheet data
file_path = "marksheet.csv"  # Update with your actual file path if needed
df_marksheet = pd.read_csv(file_path)

# Display basic information
# print("Dataset Info:\n")
# print(df_marksheet.info())

# print("\nFirst 5 Rows:\n", df_marksheet.head())
# print("\nLast 5 Rows:\n", df_marksheet.tail())

# print("\nStatistical Summary:\n", df_marksheet.describe())

# # Check for missing values
# print("\nMissing Values:\n", df_marksheet.isnull().sum())

# Add new computed columns: Total Marks, Average Marks, and Grade
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

# Display updated dataset
print("\nUpdated DataFrame:\n", df_marksheet.head())

# Save the cleaned dataset
df_marksheet.to_csv("cleanedmarksheet.csv", index=False)
print("\nCleaned dataset saved as 'marksheet_cleaned.csv'")
