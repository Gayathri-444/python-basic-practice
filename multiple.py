#problem : You have a number to examine, and your mission is to write a program that checks 
whether this number can be divided evenly by 27. Can you find out if its a multiple of 
27?


def multiple(n):
    if (n%27==0): #checking whether it is multiple of 27
        return "Its a multiple of 27"
    else:
        return "Its not multiple of 27"

n = int(input("enter a number: "))
res = multiple(n)
print(res)
