import math
import unittest

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if _name_ == "_main_":
    unittest.main()

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
        z=math.sqrt(z)
        if z<= 1:
            circle_points+= 1
        square_points+= 1
    pi = 4*circle_points/square_points
    return(pi)
