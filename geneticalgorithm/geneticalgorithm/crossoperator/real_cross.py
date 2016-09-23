from copy import copy
from numpy import *

class ArithmeticCrossover(object):

    def cross(self, population):

        individuals = random.permutation(population.shape[0])

        individuals1 = population[individuals[0:population.shape[0]/2], :]
        individuals2 = population[individuals[population.shape[0]/2:], :]

        alpha = random.rand(1)

        sons1 = zeros(individuals1.shape)
        sons2 = zeros(individuals1.shape)

        sons1[:, :-1] = alpha*individuals1[:, :-1] + (1 - alpha)*individuals2[:, :-1]
        sons2[:, :-1] = (1 - alpha)*individuals1[:, :-1] + alpha*individuals2[:, :-1]

        new_population = concatenate([population, sons1, sons2], axis = 0)

        return new_population, population.shape[0]

class ElitistArithmeticCrossover(object):

    def cross(self, population):

        best = copy(population[argmax(population[:, -1])])

        individuals = random.permutation(population.shape[0])

        individuals1 = population[individuals[0:population.shape[0]/2], :]
        individuals2 = population[individuals[population.shape[0]/2:], :]

        alpha = random.rand(1)

        sons1 = zeros(individuals1.shape)
        sons2 = zeros(individuals1.shape)

        sons1[:, :-1] = alpha*individuals1[:, :-1] + (1 - alpha)*individuals2[:, :-1]
        sons2[:, :-1] = (1 - alpha)*individuals1[:, :-1] + alpha*individuals2[:, :-1]

        new_population = concatenate([population, sons1, sons2], axis = 0)

        new_population[-1, :] = best

        return new_population, population.shape[0]

class SpeciationCrossover(object):
    
    def __init__(self, sigmate):
        self.sigmate = sigmate

    def cross(self, population):

        alpha = random.rand(1)

        sons1 = zeros((population.shape[0]/2, population.shape[1]))
        sons2 = zeros((population.shape[0]/2, population.shape[1]))
        
        for i in arange(population.shape[0]/2):
            dist = abs(population[i, -1] - concatenate([population[0:i, -1], population[i+1:, -1]], axis = 0))
            mates = where(dist < self.sigmate)[0]

            if size(mates) == 0:
                mate_idx = random.permutation(population.shape[0])[0]
            else:
                mate_idx = mates[random.permutation(mates.shape[0])[0]]

            sons1[i, :-1] = alpha*population[i, :-1] + (1 - alpha)*population[mate_idx, :-1]
            sons2[i, :-1] = (1 - alpha)*population[i, :-1] + alpha*population[mate_idx, :-1]

        new_population = concatenate([population, sons1, sons2], axis = 0)

        return new_population, population.shape[0]


class ElitistSpeciationCrossover(object):
    
    def __init__(self, sigmate):
        self.sigmate = sigmate

    def cross(self, population):

        best = copy(population[argmax(population[:, -1])])

        alpha = random.rand(1)

        sons1 = zeros((population.shape[0]/2, population.shape[1]))
        sons2 = zeros((population.shape[0]/2, population.shape[1]))
        
        for i in arange(population.shape[0]/2):
            dist = abs(population[i, -1] - concatenate([population[0:i, -1], population[i+1:, -1]], axis = 0))
            mates = where(dist < self.sigmate)[0]

            if size(mates) == 0:
                mate_idx = random.permutation(population.shape[0])[0]
            else:
                mate_idx = mates[random.permutation(mates.shape[0])[0]]

            sons1[i, :-1] = alpha*population[i, :-1] + (1 - alpha)*population[mate_idx, :-1]
            sons2[i, :-1] = (1 - alpha)*population[i, :-1] + alpha*population[mate_idx, :-1]

        new_population = concatenate([population, sons1, sons2], axis = 0)

        new_population[-1, :] = best

        return new_population, population.shape[0]
