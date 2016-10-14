from copy import copy
from numpy import *

class DEMutation(object):

    def __init__(self, f):
        self.f = f

    def mutate(self, population, iteraction):

        new_population = zeros(population.shape)

        for i in arange(0, population.shape[0]):
            rrr = random.permutation(population.shape[0])
            idxs = rrr[where(rrr != i)][0:3]
            new_population[i, :-1] = population[idxs[0], :-1] + self.f*(population[idxs[1], :-1] \
                                                          -         population[idxs[2], :-1]) 

        return new_population


class CorrelatedMutation(object):
    # The behaviour espected by sigma does not work well when the best 
    # individual is saved

    def __init__(self, beta, tal1, tal2):
        self.beta = beta # - 0.0873
        self.tal1 = tal1 # - (2*population.shape[0])**(-0.5)
        self.tal2 = tal2 # - ((2*population.shape[0])**(0.5))*(-0.5)

    def mutate(self, population, iteraction, evol_parameters):

        # Calculating rotation matrix
        prod_m = eye(evol_parameters.shape[0])
        for i in arange(0, evol_parameters.shape[0]):
            for j in arange(i+1, evol_parameters.shape[0]):
                rot_m = eye(evol_parameters.shape[0])
                rot_m[i,i] = cos(evol_parameters[i, 1]) 
                rot_m[j,j] = cos(evol_parameters[i, 1])
                rot_m[i,j] = -sin(evol_parameters[i, 1]) 
                rot_m[j,i] = sin(evol_parameters[i, 1]) 
                prod_m = dot(prod_m, rot_m)
        

        # Mutating parameters
        evol_parameters[:, 0:1] = evol_parameters[:, 0:1]*exp(self.tal1*random.randn(1) + self.tal2*random.randn(population.shape[0], 1))
        evol_parameters[:, 1:2] = evol_parameters[:, 1:2] + (evol_parameters[:, 1:2]*self.beta*random.randn(evol_parameters[:, 1].shape[0], 1)) % 2*pi

        sigma_m = eye(evol_parameters.shape[0])*evol_parameters[:, 0]        

        mutation = transpose(array([evol_parameters[:, 0], evol_parameters[:, 0]]))*random.randn(population.shape[0], 2)
        population[:, :-1] = population[:, :-1] + mutation

        return population, evol_parameters
        

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
