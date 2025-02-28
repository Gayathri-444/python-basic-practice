#problem : write a program that replaces the last number of each tuple in the list with a given number (N).

num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]

n = int(input())
new_list = []
for tuple_a in num_list :
    update_tuple = tuple_a[:-1] + (n,)
    new_list.append(update_tuple)
    
print(new_list)
