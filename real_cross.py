
from numpy import *


class ArithmeticCrossover(object):

    def cross(self, individuals1, individuals2):
    	alpha = random.rand(1)
        return (alpha*individuals1 + (1 - alpha)*individuals2, (1 - alpha)*individuals1 + alpha*individuals2)
