from numpy import *
from copy import copy

class ElitistPercentScrambleMutation():

    def __init__(self, percent):
        self.percent = percent
    
    def mutate(self, population, iteraction):

        best = copy(population[argmax(population[:, -1])])

        size = int(population.shape[0]*self.percent)
        idxs = random.permutation(size)
        
        for i in arange(0, size):
            markers = random.permutation(population.shape[1]-1)[0:2]

            marker1 = min(markers)
            marker2 = max(markers)

            population[idxs[i], marker1:marker2] = random.permutation(population[idxs[i], marker1:marker2]) 

        population[-1, :] = best

        return population


class PercentScrambleMutation():

    def __init__(self, percent):
        self.percent = percent
    
    def mutate(self, population, iteraction):

        size = int(population.shape[0]*self.percent)
        idxs = random.permutation(size)
        
        for i in arange(0, size):
            markers = random.permutation(population.shape[1]-1)[0:2]

            marker1 = min(markers)
            marker2 = max(markers)

            population[idxs[i], marker1:marker2] = random.permutation(population[idxs[i], marker1:marker2]) 

        return population


class ElitistPercentReverseMutation():

    def __init__(self, percent):
        self.percent = percent
    
    def mutate(self, population, iteraction):

        best = copy(population[argmax(population[:, -1])])

        size = int(population.shape[0]*self.percent)
        idxs = random.permutation(size)
        
        for i in arange(0, size):
            markers = random.permutation(population.shape[1]-1)[0:2]

            marker1 = min(markers)
            marker2 = max(markers)

            population[idxs[i], marker1:marker2] = population[idxs[i], marker1:marker2][::-1]

        population[-1, :] = best

        return population

class PercentReverseMutation():

    def __init__(self, percent):
        self.percent = percent
    
    def mutate(self, population, iteraction):

        size = int(population.shape[0]*self.percent)
        idxs = random.permutation(size)
        
        for i in arange(0, size):
            markers = random.permutation(population.shape[1]-1)[0:2]

            marker1 = min(markers)
            marker2 = max(markers)

            population[idxs[i], marker1:marker2] = population[idxs[i], marker1:marker2][::-1]

        return population


class ElitistPercentKReverseMutation():

    def __init__(self, percent, k):
        self.percent = percent
        self.k = k
    
    def mutate(self, population, iteraction):

        best = copy(population[argmax(population[:, -1])])

        size = int(population.shape[0]*self.percent)
        idxs = random.permutation(size)
        
        for i in arange(0, size):
            markers = random.permutation(population.shape[1]-1)[0:self.k]

            markers = sort(markers)
            
            for j in arange(0, markers.shape[0]-1):
                if(j % 2 == 0):
                    population[idxs[i], markers[j]:markers[j+1]] = population[idxs[i], markers[j]:markers[j+1]][::-1]
                else:
                    population[idxs[i], markers[j]:markers[j+1]] = population[idxs[i], markers[j]:markers[j+1]]

        population[-1, :] = best

        return population

class PercentKReverseMutation():

    def __init__(self, percent, k):
        self.percent = percent
        self.k = k
    
    def mutate(self, population, iteraction):

        size = int(population.shape[0]*self.percent)
        idxs = random.permutation(size)
        
        for i in arange(0, size):
            markers = random.permutation(population.shape[1]-1)[0:self.k]

            markers = sort(markers)
            
            for j in arange(0, markers.shape[0]-1):
                if(j % 2 == 0):
                    population[idxs[i], markers[j]:markers[j+1]] = population[idxs[i], markers[j]:markers[j+1]][::-1]
                else:
                    population[idxs[i], markers[j]:markers[j+1]] = population[idxs[i], markers[j]:markers[j+1]]

        return population

