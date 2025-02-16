#Problem :Abhinav and Anjali are playing a game called Rock-Paper-Scissors. It's a hand game usually played between two people. In this game, they both show their hands in one of three ways: Rock, Paper, or Scissors.

ab = input("Enter the shape chosen by Abinav: ")
an = input("Enter the shape chosen by Anjali: ")
if (ab=="Rock" and an=="Scissors") or (ab=="Scissors" and an=="Paper") or (ab=="Paper" and an=="Rock"):
    print("Abhinav Wins")
elif (ab=="Scissors" and an=="Rock") or (ab=="Paper" and an=="Scissors") or (ab=="Rock" and an=="Paper"):
    print("Anjali Wins")
else:
    print("Tie")
