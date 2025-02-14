print("shivarth")

#Variables in Python 
a = 10
A = 20
print(a)
print(A)

#Expressions in Python

b= 10
c= 20
d= 30
e= b+c+d
print("The value of e is", e)


#Conditions in Python
f = 3
g = 9
if f>g:
    print("f is greater than g")
else:
    print("g is greater than f")

# Conditions in Python
if g % f == 0:
    print("f is divisible by g")
elif b +1 == 10:
    print("Increment in b produces 10")
else:
    print("You are in else block")

#Artithmetic Operations in Python
expr = 10 + 20 * 30
print("The value of expr:",expr)

name= "shivarth"
age= 20

if((name == "shivarth" or name == "False") and (age >= 2)):
    print("Welcome to the world of Python")
else:
    print("Good Bye!!")

# difference between # == and is operator # [] is an empty list
list1 = []
list2 = []
list3=list1

print(id(list1))
print(id(list2))
if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if (list1 is list3):
    print("True")
else:    
    print("False")

list3 = list3 + list2

if (list1 is list3):
    print("True")
else:    
    print("False")