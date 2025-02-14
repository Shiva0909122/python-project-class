# step1:

import pandas as pd
data1 =pd.read_csv('winequality-red.csv')
df=pd.DataFrame(data1)

print("+=======1=========+")
print("The Df value: \n ",df)
print("+=======2=========+")
print("The Df info value: \n",df.info())  # Column data types and non-null values
print("+========3========+")
print("The Df first 5 value: \n",df.head(5))  # First 5 rows
print("+==========4======+")
print("The Df last 5 value: \n",df.tail(5))  # Last 5 rows
print("+============5====+")
Statistics is a branch of mathematics dealing with the collection, analysis, interpretation, presentation, and organization of data. It provides tools and methods to understand and draw conclusions from data, including measures of central tendency (mean, median, mode), measures of variability (range, variance, standard deviation), and various inferential techniques (hypothesis testing, regression analysis).

In the context of data analysis with Pandas, statistics help summarize and describe the data, identify patterns, and make informed decisions based on the data insights.

Example of statistical summary in Pandas:
```python
print("The Df Description value: \n", df.describe())
```
This command provides summary statistics of the DataFrame, including count, mean, standard deviation, min, max, and quartiles for each numerical column.


print("+===========6=====+")
print("The Df shape value: \n",df.shape)  # Number of rows and columns
print("+==========7======+")
print("The Df column names: \n",df.columns)  # Column names
print("+===========8=====+")
print("The Df datatypes: \n",df.dtypes)  # Data types of columns
print("+============9====+")
print("The Df missing  value: \n",df.isnull().sum())  # Check missing values

------------------------------------------------

# step2 : Cleaning:
import pandas as pd

# Load data
# df = pd.read_csv('winequality-red.csv')
df = pd.read_csv('winequality-red.csv', delimiter=';')

# Check column names
print("The columns are: ",df.columns)

# Check citric acid value range
# print(df['citric acid'].describe())

```python
filtered_df = df[df['citric acid'] > 0.5]
print("The filtered top 10 values:")
print(filtered_df.head(10))  # Print top 10 rows

print("The filtered bottom 10 values:")
print(filtered_df.tail(10))  # Print bottom 10 rows

# Filter rows where citric acid is between 0.5 and 1.0
filtered_df_range = df[(df['citric acid'] > 0.5) & (df['citric acid'] <= 1.0)]
print("The filtered values within range 0.5 to 1.0:")
print(filtered_df_range.head(10))  # Print top 10 rows within range
```

print(filtered_df)

------------------------------------------------

# step3 : Creating New Columns**
# Create a new column based on conditions
import pandas as pd

# Load data correctly
df = pd.read_csv('winequality-red.csv', delimiter=';')

# Check column names
print("The columns are: ", df.columns)

# Check citric acid value range
print(df['citric acid'].describe())  # Uncomment to verify values

# Apply a realistic filter
filtered_df = df[df['citric acid'] > 0.5]
print("The filtered values:")
print(filtered_df.head())  # Print first few rows instead of entire DF

# Create a new column based on acidity level
df['acidity_level'] = df['fixed acidity'].apply(lambda x: 'High' if x > 7 else 'Low')

# Apply a function to transform citric acid data
df['citric_acid_squared'] = df['citric acid'].apply(lambda x: x**2)

# Print sample rows to confirm new columns
print(df[['fixed acidity', 'acidity_level', 'citric acid', 'citric_acid_squared']].head())

 ------------------------------------------------

### step 4. Visualization (Optional, if using Jupyter/Colab)**
<!-- pip install matplotlib seaborn -->
```markdown
import matplotlib.pyplot as plt

# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. 
# It is widely used for plotting graphs and charts, and it integrates well with libraries like NumPy and Pandas.
# The `pyplot` module in Matplotlib provides a MATLAB-like interface for creating plots and figures.

# Example usage:
# Plotting a simple line graph
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.title('Simple Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```
import seaborn as sns

# Histogram of quality with labels
plt.figure(figsize=(8, 6))
df['quality'].hist(bins=10, edgecolor='black')
plt.title('Distribution of Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Frequency')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 6))

plt.show()

 ------------------------

# Pandas operations or analyses? 🚀

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
file_path = "/mnt/data/winequality-white.csv"
df = pd.read_csv(file_path)

# --------------------------------------------
# 1. BASIC DATA EXPLORATION
# --------------------------------------------

print("Dataset Info:")
print(df.info())  # Column types & missing values

print("\nFirst 5 Rows:")
print(df.head())  # First 5 rows

print("\nSummary Statistics:")
print(df.describe())  # Statistical summary

print("\nShape of Dataset:", df.shape)  # Rows and columns

print("\nColumn Names:", df.columns)  # Column headers

print("\nChecking for Missing Values:")
print(df.isnull().sum())  # Count missing values per column

# --------------------------------------------
# 2. DATA CLEANING
# --------------------------------------------

# Fill missing values with column mean
df.fillna(df.mean(), inplace=True)

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# --------------------------------------------
# 3. DATA SELECTION & FILTERING
# --------------------------------------------

# Select specific columns
df_subset = df[['fixed acidity', 'volatile acidity', 'citric acid']]

# Filter rows where quality is greater than 6
df_high_quality = df[df['quality'] > 6]

# Apply multiple conditions
df_filtered = df[(df['fixed acidity'] > 7) & (df['quality'] >= 6)]

# --------------------------------------------
# 4. SORTING DATA
# --------------------------------------------

# Sort by 'quality' in descending order
df_sorted = df.sort_values(by='quality', ascending=False)

# --------------------------------------------
# 5. AGGREGATION & GROUPING
# --------------------------------------------

# Group by 'quality' and get mean values
df_grouped = df.groupby('quality').mean()

# Count number of entries per quality level
df_counts = df['quality'].value_counts()

print("\nMean Values Grouped by Quality:")
print(df_grouped)

print("\nCount of Wines per Quality Score:")
print(df_counts)

# --------------------------------------------
# 6. FEATURE ENGINEERING (Creating New Columns)
# --------------------------------------------

# Creating a new column based on acidity level
df['acidity_level'] = ['High' if x > 7 else 'Low' for x in df['fixed acidity']]

# Creating a transformed column (square of citric acid)
df['citric_acid_squared'] = df['citric acid'].apply(lambda x: x**2)

# --------------------------------------------
# 7. DATA VISUALIZATION
# --------------------------------------------

# Histogram of quality
plt.figure(figsize=(8,5))
df['quality'].hist(bins=10, color='skyblue', edgecolor='black')
plt.xlabel("Quality")
plt.ylabel("Count")
plt.title("Wine Quality Distribution")
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

# Boxplot for alcohol content
plt.figure(figsize=(8,5))
sns.boxplot(x='quality', y='alcohol', data=df, palette='coolwarm')
plt.title("Alcohol Content by Wine Quality")
plt.show()

# --------------------------------------------
# 8. MERGING & JOINING (Example)
# --------------------------------------------

# Create a dummy dataframe to merge
df_extra = pd.DataFrame({
    'quality': df['quality'].unique(),
    'category': ['Low' if x < 5 else 'Medium' if x < 7 else 'High' for x in df['quality'].unique()]
})

# Merge with original dataset
df_merged = df.merge(df_extra, on='quality', how='left')

print("\nMerged DataFrame:")
print(df_merged.head())

# --------------------------------------------
# 9. PIVOT TABLES & CROSSTABS
# --------------------------------------------

# Create a pivot table to see mean alcohol content for each quality level
pivot_table = df.pivot_table(values='alcohol', index='quality', aggfunc='mean')

print("\nPivot Table (Mean Alcohol by Quality):")
print(pivot_table)

# Crosstab to count acidity levels per quality
crosstab_result = pd.crosstab(df['quality'], df['acidity_level'])
print("\nCrosstab Result:")
print(crosstab_result)

# --------------------------------------------
# 10. EXPORTING DATA
# --------------------------------------------

# Save cleaned data to CSV
df.to_csv("/mnt/data/cleaned_winequality-white.csv", index=False)

# Save as Excel file
df.to_excel("/mnt/data/cleaned_winequality-white.xlsx", index=False)

print("\nCleaned data saved successfully!")

# Explaintaion

Explanation of Features Included in the Code:
✔ Basic Exploration: Understanding dataset structure
✔ Data Cleaning: Handling missing values and duplicates
✔ Filtering & Selection: Extracting relevant data
✔ Sorting: Ordering values
✔ Grouping & Aggregation: Summarizing data
✔ Feature Engineering: Creating new columns
✔ Visualization: Histograms, box plots, heatmaps
✔ Merging & Joining: Combining datasets
✔ Pivot Tables & Crosstabs: Summarizing relationships
✔ Saving Data: Exporting to CSV & Excel

