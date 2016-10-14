import numpy.matlib as matlib
from copy import copy
from numpy import *

class DECrossover(object):

    def __init__(self, cr):
        self.cr = cr

    def cross(self, population, mut_population):
        
        new_population = zeros(population.shape)
        for i in arange(0, population.shape[0]):
            variables = random.rand(population.shape[1]-1) < self.cr
            if(sum(variables) == 0):
                variables[random.permutation(population.shape[1]-1)] = True
        
            new_population[i, :-1] = concatenate([population[i, :-1][variables == False], mut_population[i, :-1][variables == True]], axis = 0)

        return new_population, population.shape[0]


class EEAndArithmeticCrossover(object):

    def __init__(self, mu, _lambda):
        self.mu = mu
        self._lambda = _lambda

    def cross(self, population, evol_parameters):

        if(population.shape[0] == 1):
            sons = matlib.repmat(population, self._lambda, 1)
            sons_par = matlib.repmat(evol_parameters, self._lambda, 1)
       
            return sons, sons_par, self._lambda + self.mu

        sons = zeros((self._lambda, population.shape[1]))
        sons_par = zeros((self._lambda, evol_parameters.shape[1]))
        for i in arange(0, self._lambda):
            idx = random.permutation(self.mu)[0:2]
            alpha = random.rand(1)
            sons[:, :-1] = alpha*population[idx[0], :-1] + (1 - alpha)*population[idx[1], :-1]
            sons_par[:, 0] = (evol_parameters[idx[0], 0] + evol_parameters[idx[1], 0])/2
            sons_par[:, 1] = (evol_parameters[idx[0], 1] + evol_parameters[idx[1], 1])/2

        return sons, sons_par, self._lambda

class EEPlusArithmeticCrossover(object):

    def __init__(self, mu, _lambda):
        self.mu = mu
        self._lambda = _lambda

    def cross(self, population, evol_parameters):

        if(population.shape[0] == 1):
            sons = matlib.repmat(population, self._lambda, 1)
            sons_par = matlib.repmat(evol_parameters, self._lambda, 1)
            new_population = concatenate([population, sons], axis = 0)
            new_evol_parameters = concatenate([evol_parameters, sons_par], axis = 0) 
       
            return new_population, new_evol_parameters, self._lambda + self.mu

        sons = zeros((self._lambda, population.shape[1]))
        sons_par = zeros((self._lambda, evol_parameters.shape[1]))
        for i in arange(0, self._lambda):
            idx = random.permutation(self.mu)[0:2]
            alpha = random.rand(1)
            sons[:, :-1] = alpha*population[idx[0], :-1] + (1 - alpha)*population[idx[1], :-1]
            sons_par[:, 0] = (evol_parameters[idx[0], 0] + evol_parameters[idx[1], 0])/2
            sons_par[:, 1] = (evol_parameters[idx[0], 1] + evol_parameters[idx[1], 1])/2

        new_population = concatenate([population, sons], axis = 0)
        new_evol_parameters = concatenate([evol_parameters, sons_par], axis = 0) 

        return new_population, new_evol_parameters, self._lambda + self.mu


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
