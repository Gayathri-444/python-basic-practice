#problem : write a program to find season for the given month number.

n = int(input("Enter a month number: "))
if n==2 or n==3 :
    print("Spring")
elif n==4 or n==5 or n==6 :
    print("Summer")
elif n==7 or n==8 :
    print("Rainy")
elif n==9 or n==10 :
    print("Autumn")
elif n==1 or n==11 or n==12 :
    print("Winter")
