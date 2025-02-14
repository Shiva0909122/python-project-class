'''The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:
Note that "..." represents the consecutive values in between.'''



if __name__ == '__main__':
    n = int(input("Enter a number: "))
    for i in range(1, n+1):
        print(i, end="")
    print()


'''Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.'''

def is_leap(year):
    leap = False
    

    # Write your logic here
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    return leap

year = int(input("Enter a year: "))
print(is_leap(year))