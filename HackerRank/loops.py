'''The provided code stub reads an integer, n , from STDIN. For all non-negative integers i<n, print i ** 2 .'''

# Solution:
if __name__ == '__main__':
    n = int(input("Enter a positive integer: ").strip())
    for i in range(n):
        print(i ** 2)



# Output: Enter a positive integer: 5
# 0# 1# 4# 9# 16
'''Explanation :
The square of the integer 0 is 0.The square of the integer 1 is 1.
The square of the integer 2 is 4.
The square of the integer 3 is 9.The square of the integer 4 is 16.'''
