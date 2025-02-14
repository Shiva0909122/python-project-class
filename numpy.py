
# **NumPy (Numerical Python)**
# NumPy is a powerful Python library used for numerical computing. 
# It provides support for large multi-dimensional arrays and matrices,
#  along with mathematical functions to operate on these arrays.


# **1. Importing NumPy**
 
## **2. Creating NumPy Arrays**
# NumPy provides an `ndarray` object which is more efficient than 
# Python lists.

### **Creating Arrays**
#### **1D Array**
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print("\n") 
#### **2D Array**
 
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print("\n")
#### **3D Array**
 
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3)
print("\n") 

## **3. Checking Array Properties**
 
print(arr1.ndim)  # Number of dimensions
print(arr2.shape)  # Shape (rows, columns)
print(arr1.size)   # Number of elements
print(arr1.dtype)  # Data type
print("\n") 
## **4. Creating Special Arrays**
### **Zeros Array**
 
zeros = np.zeros((3, 3))
print(zeros)
print("\n") 
### **Ones Array**
 
ones = np.ones((2, 4))
print(ones)
print("\n") 
### **Identity Matrix**
 
identity = np.eye(4)
print(identity)
print("\n") 
### **Array with Random Values**
 
rand_array = np.random.rand(3, 3)
print(rand_array)
print("\n") 
### **Array with Range of Numbers**
 
arr_range = np.arange(1, 10, 2)  # (start, stop, step)
print(arr_range)
print("\n") 
### **Array with Evenly Spaced Values**
 
lin_space = np.linspace(1, 10, 5)  # (start, stop, number of points)
print(lin_space)
print("\n")

## **5. Array Indexing and Slicing**
### **Indexing**
 
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])  # First element
print(arr[-1]) # Last element
print("\n") 
### **Slicing**
 
print(arr[1:4])   # Elements from index 1 to 3
print(arr[:3])    # First three elements
print(arr[::2])   # Every second element
print("\n") 
### **Indexing in 2D Arrays**
 
arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2D[1, 1])  # Element at row 1, col 1
print(arr2D[:, 1])  # All rows, second column
 
print("\n")
 

## **6. Mathematical Operations**
### **Basic Operations**
 
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # Element-wise addition
print(a - b)  # Element-wise subtraction
print(a * b)  # Element-wise multiplication
print(a / b)  # Element-wise division
print("\n")

### **Broadcasting**
 
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 2, 3])
print(a + b)  # Broadcasts `b` to match `a`
print("\n") 

### **Matrix Multiplication**
 
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.dot(A, B))  # Matrix multiplication
print("\n") 

## **7. Statistical Functions**
 
arr = np.array([1, 2, 3, 4, 5])

print(np.min(arr))  # Minimum value
print(np.max(arr))  # Maximum value
print(np.sum(arr))  # Sum of all elements
print(np.mean(arr)) # Mean
print(np.median(arr)) # Median
print(np.std(arr)) # Standard deviation
print("\n") 
## **8. Reshaping and Transposing**
### **Reshape**
 
arr = np.arange(1, 10)
reshaped = arr.reshape(3, 3)
print(reshaped)
print("\n") 
### **Transpose**
 
print(reshaped.T)  # Transpose of a matrix
print("\n") 

## **9. Stacking and Splitting**
### **Stacking**
 
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack((a, b)))  # Vertical stack
print(np.hstack((a, b)))  # Horizontal stack
print("\n") 
### **Splitting**
 
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.split(arr, 2))  # Split into 2 equal parts
print("\n") 
## **10. Copying and Views**
 
arr = np.array([1, 2, 3])
b = arr.copy()  # Creates a new independent array
b[0] = 100
print(arr)  # Original remains unchanged
print("\n") 
 

## **11. Boolean Indexing**
 
arr = np.array([10, 20, 30, 40, 50])
print(arr[arr > 25])  # Elements greater than 25
print("\n") 
