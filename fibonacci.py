n = int(input("enter a number: "))

n1=0
n2=1

for i in range(2,n):
    n3 = n1+n2
    print(" "+str(n3))
    n1=n2
    n2=n3
