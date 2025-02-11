#problem : Write a program that reads a number N and checks if the last digit of N is equal to the last digit of the square of N. Print Equal if the last digit of N is equal to the last digit of the square of N. Otherwise, print Not Equal.

N = int(input("Enter a number:"))
a = N**2
type1 = str(N)  #type casting of int to str.
type2 = str(a)
if type1[-1]==type2[-1]:  #checking last digit is equal or not.
    print("Equal")
else:
    print("Not Equal")
