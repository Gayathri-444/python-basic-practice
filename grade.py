#problem : grading scheme program.


def grade(n):
    if(n>=90):
        return "A"
    elif(80<=n<=89):
        return "B"
    elif(70<=n<=79):
        return "C"
    elif(60<=n<=69):
        return "D"
    else:
        return "F"

n = int(input("enter the marks: "))
res = grade(n)
print(res)
