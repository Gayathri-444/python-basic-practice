w = input("enter a string: ")

for i in range(0,len(w)):
    for j in range(i+1,len(w)+1):
        print(w[i:j])
