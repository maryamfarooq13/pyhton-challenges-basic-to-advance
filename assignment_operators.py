# Write a program that take input of x and print True if x is even
x = int(input('Enter Value of x: '))
x %= 2
print('x is even:', x == 0)


# Write a program that take input of x and y and print True if x is a multiple of y
n = int(input('Enter Value of x: '))
m = int(input('Enter Value of y: '))
n %= m
print('x is multiple of y: ',(x==0))


# Given two variables a = 10 and b = 5, perform the following operations:
# Addition of a and b and store it in a
# Subtraction of b from a store it in b
# Multiplication of a and b and store it in a
# Division of a by b and store it in b
# Exponentiation (a to the power of b) 
a = 10
b = 5

a += b
print('stored value in a after a += b is:', a)
print('Value of a is: ', a, type(a))
print('Value of a is: ', b, type(b))
b -= a
print('stored value in b after b -= a is:', b)
print('Value of a is: ', a, type(a))
print('Value of a is: ', b, type(b))
a *= b
print('stored value in a after a *= b is:', a)
print('Value of a is: ', a, type(a))
print('Value of a is: ', b, type(b))
b /= a
print('stored value in b after b /= a is:', b)
print('Value of a is: ', a, type(a))
print('Value of a is: ', b, type(b))
a **= b
print('a to the power of b is:', a)
print('Value of a is: ', a, type(a))
print('Value of a is: ', b, type(b))