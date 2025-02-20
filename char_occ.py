#problem : Write a python program to count the number of occurences of the given character in the String.

s = input("Enter a String: ")
n = input("Enter a character: ")

count = 0

for i in s:
    if i==n:
        count += 1
print("count of "+n+": "+str(count))
