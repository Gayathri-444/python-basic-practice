#problem: Write a program that reads an operator O, and two numbers A and B.Print the result by doing arithmetic operations on A and B based on the operator O


operator = input("Enter the operator : ")
first_number = int(input("Enter the value of num1 : "))
second_number = int(input("Enter the value of num2 : "))

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    print(first_number / second_number)
else:
    print(first_number % second_number)
