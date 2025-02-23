#problem : a program that reads two numbers, A and B, and checks if both A and B are less than or equal to 1000 or B is greater than 500. The program should print "Pair" if the conditions are met, and "Not a Pair" otherwise.

A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
if ((A<=1000 and B<=1000)or(B>500)):
    print("Pair")
else:
    print("Not a Pair")
