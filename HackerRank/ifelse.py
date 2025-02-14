#!/bin/python3
'''Question: Given an integer, n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird'''

# Solution:

if __name__ == '__main__':
    n = int(input("Enter a positive integer: ").strip())

    if n % 2 == 1:  # Check if n is odd
        print("Weird")
    elif 2 <= n <= 5:  # Even and in range 2 to 5
        print("Not Weird")
    elif 6 <= n <= 20:  # Even and in range 6 to 20
        print("Weird")
    else:  # Even and greater than 20
        print("Not Weird")

# Output: Enter a positive integer: 24
# Not Weird
'''Explanation:
If n is odd, print "Weird".
If n is even and in the range [2, 5], print "Not Weird".
If n is even and in the range [6, 20], print "Weird".
If n is even and greater than 20, print "Not Weird". '''