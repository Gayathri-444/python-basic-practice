#problem : Given the coordinates of two trucks, A (Ax, Ay) and B (Bx, By), determine which truck is closer to the office at (0,0). Compare the square of their distances and return the smaller value. If both are equal, return either.

def Distance(Ax, Ay, Bx, By):
    distanceA = (Ax ** 2) + (Ay ** 2)
    distanceB = (Bx ** 2) + (By ** 2)
    
    return min(distanceA, distanceB)


Ax, Ay, Bx, By = map(int, input().split())
print(Distance(Ax, Ay, Bx, By))
