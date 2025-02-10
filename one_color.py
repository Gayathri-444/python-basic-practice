#problem : Given a string of length N, made up of only uppercase characters 'R' and 'G', where 'R' stands for Red and 'G' stands for Green. Find out the minimum number of characters you need to change to make the whole string of the same colour.

s = input("Enter the string: ")
count_r = 0 
count_g = 0
for i in s:    
    if i=="R":    #if the character is R, then count is added.
        count_r = count_r + 1 
    else:
        count_g = count_g + 1 

if count_r>count_g:    #if the R is greater , then count of G displays.
    print("G:"+str(count_g))
else:
    print("R:"+str(count_r))
