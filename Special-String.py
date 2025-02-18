#problem : Write a program that reads a String S and checks if all the given conditions are satisfied.
#The first three characters of S is NXT. The remaining characters of S contain a Number. Number is divisible by 2 or 7.
#Print Special String if all the given conditions are satisfied. Otherwise, print Not a Special String.

S = input("Enter the input: ")
a = S[0:3]=="NXT"
s = int(S[3: ])
b = s%2==0 or s%7==0
if a and b:
    print("Special String")
else:
    print("Not a Special String")
