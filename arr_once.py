'''''problem :Given a non-empty array of integers nums, every element appears twice except for one. Find 
that single one.''' 

def once(arr):
    once = []   #creating an empty list to add items
    for i in arr:
        if arr.count(i) == 1: #count() counts the number of times a number appears
            once.append(i)  #adding to the empty list
    return once  

arr = list(map(int, input("Enter numbers: ").split(',')))
res = once(arr)
print(res)

            
