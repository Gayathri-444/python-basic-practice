#problem : You have two numbers, and your challenge is to write a program that performs both 
addition and subtraction with them. However, if any subtraction results in a negative 
number, display it as a positive value. How will you tackle this and show the final 
results?

def addsub(a,b):
    add = a+b
    sub = abs(a-b)#abs function is used to provide all the value in positive values.
    return add,sub

a = int(input())
b = int(input())
res = addsub(a,b)
print(res)
