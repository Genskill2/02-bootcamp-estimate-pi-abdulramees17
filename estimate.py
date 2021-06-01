def wallis(n):
    p = 1
    for i in range(1,n+1):
        x=(4*(i**2))
        y=(4*(i**2) - 1)
        z=x/y
        p=p*z
    p=p*2
    return(p)
    
    
import random
def monte_carlo(n):
    circle_points= 0
    square_points= 0
    for i in range(n):
        x= random.uniform(0, 1)
        y= random.uniform(0, 1)
        z= x**2 + y**2
        if z<= 1:
            circle_points+= 1
        square_points+= 1
    pi = 4*circle_points/square_points
    return(pi)
