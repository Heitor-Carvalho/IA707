from copy import copy
from numpy import *

class NonUniformMutation(object):
    
    def __init__(self, a, b, p, T):
        self.a = float(a)
        self.b = float(b)
        self.p = float(p)
        self.T = float(T)

    def mutate(self, population, iteraction):
        
        # Particular case for two cromossomo
        rrr = random.rand(population.shape[0], population.shape[1]-1)
        if(random.rand(1) > 0.5):
            delta = (self.b - population[:, :-1])
        else:
            delta = -(population[:, :-1] - self.a)

        population[:, :-1] = population[:, :-1] + delta*(1 - rrr**(1 - min(iteraction, self.T)/self.T)**self.p)

        return population

class ElitistNonUniformMutation(object):
    
    def __init__(self, a, b, p, T):
        self.a = float(a)
        self.b = float(b)
        self.p = float(p)
        self.T = float(T)

    def mutate(self, population, iteraction):
        
        best = copy(population[argmax(population[:, -1])])

        # Particular case for two cromossomo
        rrr = random.rand(population.shape[0], population.shape[1]-1)
        if(random.rand(1) > 0.5):
            delta = (self.b - population[:, :-1])
        else:
            delta = -(population[:, :-1] - self.a)

        population[:, :-1] = population[:, :-1] + delta*(1 - rrr**(1 - min(iteraction, self.T)/self.T)**self.p)

        population[-1, :] = best
        
        return population

class PercentNonUniformMutation(object):
    
    def __init__(self, a, b, p, T, percent):
        self.a = float(a)
        self.b = float(b)
        self.p = float(p)
        self.T = float(T)
        self.percent = percent

    def mutate(self, population, iteraction):

        size = int(population.shape[0]*self.percent)
        idxs = random.permutation(size)

        rrr = random.rand(idxs.shape[0], population.shape[1]-1)
        if(random.rand(1) > 0.5):
            delta = (self.b - population[idxs, :-1])
        else:
            delta = -(population[idxs, :-1] - self.a)

        population[idxs, :-1] = population[idxs, :-1] + delta*(1 - rrr**(1 - min(iteraction, self.T)/self.T)**self.p)

        return population

class ElitistPercentNonUniformMutation(object):
    
    def __init__(self, a, b, p, T, percent):
        self.a = float(a)
        self.b = float(b)
        self.p = float(p)
        self.T = float(T)
        self.percent = percent

    def mutate(self, population, iteraction):

        best = copy(population[argmax(population[:, -1])])

        size = int(population.shape[0]*self.percent)
        idxs = random.permutation(size)

        rrr = random.rand(idxs.shape[0], population.shape[1]-1)
        if(random.rand(1) > 0.5):
            delta = (self.b - population[idxs, :-1])
        else:
            delta = -(population[idxs, :-1] - self.a)

        population[idxs, :-1] = population[idxs, :-1] + delta*(1 - rrr**(1 - min(iteraction, self.T)/self.T)**self.p)

        population[-1, :] = best
        
        return population
