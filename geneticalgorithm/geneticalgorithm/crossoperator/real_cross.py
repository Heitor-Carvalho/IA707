from numpy import *

class ArithmeticCrossover(object):

    def cross(self, individuals1, individuals2):
        alpha = random.rand(1)
        return (alpha*individuals1 + (1 - alpha)*individuals2, (1 - alpha)*individuals1 + alpha*individuals2)


class SpeciationCrossover(object):
    
    def __init__(self, sigmate)
        self.sigmate = sigmate

    def cross(self, population):
        import pdb; pdb.set_trace()

        for i in arrange(population.shape[0]):
            dist = abs(individual[-1] - concatenate([population[0:i, :], population[i+1:, :]], axis = 0))
            idx = argmin(dist) + 1
        pop1, pop2 = meshgrid(population[:, -1], population[:, -1])
        dist = abs(pop2-pop1) + 9.0*eye(pop1.shape[0], pop1.shape[1])
        idx = dist < self.sigmate
        



        alpha = random.rand(1)
        return (alpha*individuals1 + (1 - alpha)*individuals2, (1 - alpha)*individuals1 + alpha*individuals2)
