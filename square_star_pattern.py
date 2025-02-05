#program : Write a program to print rectangle/square star pattern.

n = int(input("enter a number: "))

for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
