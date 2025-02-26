#problem : write a python program get a 3 digit number input and print the unit digit and the 100th place digit.

num = int(input("Enter a three-digit number: "))
unit_digit = num % 10
hundredth_digit = num // 100


print("Unit digit:", unit_digit)
print("Hundredth digit:", hundredth_digit)
