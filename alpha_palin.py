'''problem : A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers. 
Given a string s, return true if it is a palindrome, or false otherwise.''' 

def palin(s):
    new = ""
    for i in s:
        if i.isalpha():
            new += i.lower()
    return new

s = input()
res = palin(s)
print(res)

if res == res[::-1]:
    print("it is a palindrom")
else:
    print("it is not a palindrome")



