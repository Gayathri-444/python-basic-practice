#problem : Given a number N, find whether the number is common or uncommon. A number is considered uncommon if it is not divisible by any of the single-digit primes.

def uncommon(n):
    if(n%2==0 or n%3==0 or n%5==0 or n%7==0):  #checking for it a common or uncommon number
        return False
    else:
        return True

n = int(input("enter a number: "))
result = uncommon(n)
print(result)
