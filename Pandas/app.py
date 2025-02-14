# Section 1

# DataFrame is a two-dimensional table-like data structure with labeled rows and columns, where each column can have a different data type (e.g., integers, strings, floats).
# It can be created from Python data structures like lists, dictionaries, or a list of dictionaries.

import pandas as pd

# Create a DataFrame from a dictionary
data1 = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Location': ['New York', 'Paris', 'Berlin', 'London'],
    'Age': [24, 13, 53, 33]
}
df = pd.DataFrame(data1) # Create a DataFrame from a dictionary  
print(df) # Print the DataFrame


# Section 2

# Series in Pandas is 1-dimensional labeled array capable of holding any data type (integers, strings, floats, etc.). 
# Each element is associated with an index, either default (0, 1, 2…) or custom labels. 

# creating a series
age = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])
print(age)  


# Section 3

# Reading a csv file
df = pd.read_csv('people_data.csv') # Read a CSV file
print(df) # Print the DataFrame


#Section 4

# Understanding and Analyzing the Data Frame
# After creating or loading a DataFrame, inspecting and summarizing the data is an important step in understanding dataset. Pandas provides various functions to help you view and analyze the data.
# head(): View the first n rows of the DataFrame (default is 5 rows).
# tail(): View the last n rows of the DataFrame (default is 5 rows).
# info(): This method provides a concise summary of the DataFrame, including the number of non-null entries, column names, and data types.

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [24, 27, 22, 32, 29],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}

df = pd.DataFrame(data)

print("First 3 rows using head():") # Print the first 3 rows of the DataFrame
print(df.head(3)) 


print("\nLast 2 rows using tail():") # Print the last 2 rows of the DataFrame
print(df.tail(2)) 

# Get a concise summary of the DataFrame
print("\nDataFrame summary using info():")
df.info()

#============DONE==============================#

#Section 5: Indexing in Pandas
# Indexing in Pandas refers to process of accessing and selecting data from a Pandas DataFrame or Series.
#  There are multiple ways to do this. We will cover how to to basic indexing, select specific columns , apply slicing, and use Boolean indexing to filter data efficiently.

# Select a single column
age_column = df['Name'] # Select the 'Name' column
print(age_column)

# When it comes to selecting rows:
#  we can use .loc[] to select rows by label, meaning we refer to the row index or label directly. 
# Alternatively, .iloc[] allows for position-based indexing,
#  where we select rows by their integer positions.

# Using .loc[] to select rows by label
row_by_label = df.loc[3]  # Selects the row with index label 1 (Bob's data)

# Using .iloc[] to select rows by position
row_by_position = df.iloc[2]  # Selects the second row (Bob's data)

print("Row by label:\n", row_by_label)
print("Row by position:\n", row_by_position)

