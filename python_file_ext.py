#problem : Given a file name with the file extension, write a program that checks if the given file is a python file.

s = input()
length=s[-3: ]     #checking using indexing method.
if length==".py":  
    print("True")
else:
    print("False")
