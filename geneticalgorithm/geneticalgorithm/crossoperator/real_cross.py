from numpy import *

class ArithmeticCrossover(object):

    def cross(self, individuals1, individuals2):
        alpha = random.rand(1)
        return (alpha*individuals1 + (1 - alpha)*individuals2, (1 - alpha)*individuals1 + alpha*individuals2)


class SpeciationCrossover(object):
    
    def __init__(self, sigmate):
        self.sigmate = sigmate

    def cross(self, population):

        alpha = random.rand(1)

        sons1 = zeros((population.shape[0]/2, population.shape[1]-1))
        sons2 = zeros((population.shape[0]/2, population.shape[1]-1))

        for i in arange(population.shape[0]/2):
            dist = abs(population[i, -1] - concatenate([population[0:i, -1], population[i+1:, -1]], axis = 0))
            mates = where(dist < self.sigmate)[0]

            if size(mates) == 0:
                mate_idx = random.permutation(population.shape[0])[0]
            else:
                mate_idx = mates[random.permutation(mates.shape[0])[0]]

            sons1[i, :] = alpha*population[i, :-1] + (1 - alpha)*population[mate_idx, :-1]
            sons2[i, :] = (1 - alpha)*population[i, :-1] + alpha*population[mate_idx, :-1]

        return (sons1, sons2)
