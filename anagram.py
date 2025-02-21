#problem : An Anagram Program checks whether two words or phrases contain the same characters in a different order.

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

if sorted(s1)==sorted(s2):
    print("The words are anagram")
else:
    print("The words are not a anagram")
