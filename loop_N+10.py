#problem : Write a program that reads a number N and prints 10 numbers after N.

n = int(input("Enter a number:"))
start = n + 1 
end = start + 10
for i in range(start,end):  #loop runs till the end value.
    print(i)
