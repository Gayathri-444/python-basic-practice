'''problem :A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding 
the number itself. A divisor of an integer x is an integer that can divide x evenly. 
Given an integer n, return true if n is a perfect number, otherwise return false. '''

def perfect(n):
    if n<=1:
        return False

    total = 0

    for i in range(1,n-1):
        if (n%i==0):         #if the given number is divisible exactly, then it is factor
            total += i    #the extracted factors are added

    return total==n      

n = int(input("enter a number: "))
result = perfect(n)
print(result)
