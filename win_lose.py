def compare(team_a_points, team_b_points):
    if (team_a_points > team_b_points):
        print("Win")
    elif (team_a_points == team_b_points):
        print("Draw")
    else :
        print("Lose")
   
    

team_a_points = int(input("Enter team_A point: "))
team_b_points = int(input("Enter team_B point: "))

compare_result = compare(team_a_points, team_b_points)
