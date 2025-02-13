#problem : A typical car can hold four passengers and one driver, allowing five people to travel around.
#Write a function with the name number_of_cars_needed that takes a number of people (N) and return how cars are needed to seat everyone comfortably.

def number_of_cars_needed(n):
    if (n%5==0):
        return n//5
    else:
        return (n//5)+1
        

n = int(input("Enter a number of people: "))

result = number_of_cars_needed(n)

print(result)
