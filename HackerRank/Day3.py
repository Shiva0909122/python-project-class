# List
my_list = [1, 2, 3, 4, 5] # List of integers 
print("List:", my_list) # Output: List: [1, 2, 3, 4, 5]
my_list.append(6)  # Adds an element to the end
my_list.remove(2)  # Removes the first occurrence of 2
print(my_list[1])  # Accesses the second element
print(len(my_list))  # Returns the length of the list

# String
my_string = "Hello, World!" # String of characters
print("String:", my_string) # Output: String: Hello, World!
print(my_string.lower())  # Converts to lowercase
print(my_string.upper())  # Converts to uppercase
print(my_string.replace("World", "Python"))  # Replace a substring
print(len(my_string))  # Length of the string


# Integer
my_int = 12345 # Integer
print("Integer:", my_int) # Output: Integer: 12345
print(my_int + 5)  # Addition
print(my_int - 2)  # Subtraction
print(my_int * 3)  # Multiplication
print(my_int // 2)  # Integer division


# Float      
my_float = 3.14 # Floating point number
print("Float:       ", my_float) # Output: Float: 3.14
print(round(my_float, 1))  # Rounds the number to 1 decimal place
print(my_float * 2)  # Multiplication

# Boolean
my_bool = True # Boolean value
print("Boolean:", my_bool) # Output: Boolean: True
print(5 > 3)  # True
print(5 == 5)  # True
print(5 < 2)  # False


# Complex
my_complex = 1 + 2j # Complex number
print("Complex:", my_complex) # Output: Complex: (1+2j)
print(my_complex.real)  # Real part
print(my_complex.imag)  # Imaginary part

# Tuple
my_tuple = (1, 2, 3, 4, 5) # Tuple of integers
print("Tuple:", my_tuple) # Output: Tuple: (1, 2, 3, 4, 5)
print(my_tuple[0])  # Accessing an element
print(len(my_tuple))  # Length of tuple

# Set
my_set = {1, 2, 3, 4, 5} # Set of integers
print("Set:", my_set) # Output: Set: {1, 2, 3, 4, 5}
my_set.add(6)  # Adds an element
my_set.remove(3)  # Removes an element
print(my_set)

# Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3} # Dictionary
print("Dictionary:", my_dict) # Output: Dictionary: {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = 4  # Adds a new key-value pair
print(my_dict['a'])  # Accessing a value by key
print(my_dict.keys())  # Getting all keys
print(my_dict.values())  # Getting all values

# NoneType
my_none = None # NoneType
print("NoneType:", my_none) # Output: NoneType: None

x = 1 
y = 2 
z = x   
x = y 
y = z 
print(x, y)

