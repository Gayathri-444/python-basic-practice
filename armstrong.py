#problem : write a program to check whether the given number is armstrong number or not.


n = int(input())
sum = 0
temp = n
while(temp>0):
    a = temp%10 # extracts the digits
    sum += a**3  #cubes the each digit
    temp //= 10 # then gives the digits

if n==sum:
    print("armstrong number")
else:
    print("not an armstrong number")
