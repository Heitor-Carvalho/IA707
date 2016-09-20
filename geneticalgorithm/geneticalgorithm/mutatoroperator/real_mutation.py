
from numpy import *

class NonUniformMutation(object):
    
    def __init__(self, a, b, p, T):
        self.a = float(a)
        self.b = float(b)
        self.p = float(p)
        self.T = float(T)

    def mutate(self, number_array, iteraction):
        
        # Particular case for two cromossomo
        rrr = random.rand(number_array.shape[0], number_array.shape[1])
        if(random.rand(1) > 0.5):
            delta = (self.b - number_array[:, :])
        else:
            delta = -(number_array[:, :] - self.a)

        number_array[:, :] = number_array[:, :] + delta*(1 - rrr**(1 - min(iteraction, self.T)/self.T)**self.p)

        return number_array
