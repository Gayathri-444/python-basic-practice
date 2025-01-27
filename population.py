total = int(input("enter the total population: "))
men = int(input("enter the men percentage: "))

rem = (100-men)

women = total*rem//100

print(women)
