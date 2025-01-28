def Fuzzy(n):
    if n < 0:
        print("INVALID INPUT")
        return None
    elif n > 7000:
        print("OVERLOADED")
        return None
    elif 0 < n <= 2000:
        return 25
    elif 2001 <= n <= 4000:
        return 35
    elif 4001 <= n <= 7000:
        return 45


g = int(input("Enter the weight: "))
f = Fuzzy(g)

if f is not None:  # this condition executes when there is a value given
    print("Time estimated: " + str(f) + " minutes")






