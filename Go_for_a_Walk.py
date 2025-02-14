#problem : Write a program that reads a temperature and checks if the given temperature is between 15 and 40.
#Print Can go for a walk if the given temperature is between 15 and 40, otherwise print cannot go for a walk.

temp = int(input("Enter the temperature: "))
if temp>15 and temp<40:
    print("Can go for a walk")
else:
    print("Cannot go for a walk")
