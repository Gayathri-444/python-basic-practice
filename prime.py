
def isprime(n):
    for i in range(2,int(n**(0.5))+1):
        if(n<=1):
            return False
        if(n%i==0):
            return False
    return True

n = int(input("enter a number: "))
p = isprime(n)
print(p)
