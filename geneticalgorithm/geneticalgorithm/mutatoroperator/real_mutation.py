
from numpy import *

class NonUniformMutation(object):
    
    def __init__(self, a, b, p, T):
        self.a = float(a)
        self.b = float(b)
        self.p = float(p)
        self.T = float(T)

    def mutate(self, number_array, iteraction):
        
        # Particular case for two cromossomo
        crom_idx = int(round(random.rand(1)))

        rrr = random.rand(number_array.shape[0])
        if(random.rand(1) > 0.5):
            delta = (self.b - number_array[:, crom_idx])
        else:
            delta = -(number_array[:, crom_idx] - self.a)

        number_array[:, crom_idx] = number_array[:, crom_idx] + delta*(1 - rrr**(1 - min(iteraction, self.T)/self.T)**self.p)

        return number_array
