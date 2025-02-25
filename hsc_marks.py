#problem: find the percentage of HSC marks, for 5 subjects as input.

subject1 = int(input("Enter marks for Subject 1: "))
subject2 = int(input("Enter marks for Subject 2: "))
subject3 = int(input("Enter marks for Subject 3: "))
subject4 = int(input("Enter marks for Subject 4: "))
subject5 = int(input("Enter marks for Subject 5: "))

total_marks = 5 * 100
obtained_marks = subject1 + subject2 + subject3 + subject4 + subject5

percentage = (obtained_marks / total_marks) * 100

print("Total Marks Obtained: ", obtained_marks, "/ 500")
print("Percentage: ", round(percentage, 2), "%")
