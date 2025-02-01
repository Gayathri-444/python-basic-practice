#problem : A number is called Special Eleven, if it is a multiple of 11 or if it is one more than a multiple of 11. Write a program to check if the given number is special Eleven Number.

def special(n):
    if (n%11==0 or n%11==1):
        print("Special Number")
    else:
        print("Normal Number")


n = int(input("Enter a number: "))
special(n)

