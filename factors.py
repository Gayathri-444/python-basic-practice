#problem : write a program to print the factors of the given number.

def factors(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i)

n = int(input())
factors(n)
