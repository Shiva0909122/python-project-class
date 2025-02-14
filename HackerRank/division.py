'''The provided code stub reads two integers,  and , from STDIN. 
Add logic to print two lines. The first line should contain the result of integer division,  
. The second line should contain the result of float division,   .

No rounding or formatting is necessary.'''

# Solution:
if __name__ == '__main__':
    a = int(input("Enter A value: "))
    b = int(input("Enter B value: "))
    print("Result of integer division: ",a // b)
    print("Result of float division: ",a / b)

# Output: Enter A value: 3
# Enter B value: 5
# Result of integer division: 0
# Result of float division: 0.6
'''Explanation
The result of the integer division 3//5 is 0.
The result of the float division is 3/5 is 0.6.'''
