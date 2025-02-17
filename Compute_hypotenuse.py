#problem : Write a program that reads two sides A and B of a right-angled triangle and prints the hypotenuse H of the right-angled triangle.

A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
a = (((A**2)+(B**2))**0.5)
type = int(a)
print(type)
