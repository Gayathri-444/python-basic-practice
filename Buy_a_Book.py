#Problem : Write a program that reads the size S and page count C of a book and check if S is equal to large or C is greater than or equal to 300.
#print Buy a Book if S is equal to larger or C is greater than or equal to 300.Otherwise, print Do Not Buy a Book.

S = input("Enter a size: ")
C = int(input("Enter a page count: "))
if S=="large" or C>=300:
    print("Buy a Book")
else:
    print("Do Not Buy a Book")
