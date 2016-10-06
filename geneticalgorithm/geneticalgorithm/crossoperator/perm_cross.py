from copy import copy
from numpy import *

class ElitistPMXCrossover(object):

    def cross(self, population):
    
        best = copy(population[argmax(population[:, -1])])

        individuals = random.permutation(population.shape[0])

        individuals1 = population[individuals[0:population.shape[0]/2], :]
        individuals2 = population[individuals[population.shape[0]/2:], :]

        markers = random.permutation(individuals1.shape[1]-1)[0:2]

        marker1 = min(markers)
        marker2 = max(markers)

        sons1 = -1*ones(individuals1.shape)
        sons2 = -1*ones(individuals1.shape)
 
        for j in arange(0, sons1.shape[0]):
            sons1[j, marker1:marker2] = individuals1[j, marker1:marker2]
            for i in arange(marker1, marker2):
                if(individuals2[j, i] in sons1[j, marker1:marker2]):
                    continue
                else:
                    sons1[j, self.find_position(individuals2[j, i], individuals1[j, :-1], \
                                                individuals2[j, :-1], marker1, marker2)]  \
                    = individuals2[j, i] 

            idx1 = sons1[j, :-1] == -1 
            sons1[j, :-1][idx1] = individuals2[j, :-1][idx1]

        for j in arange(0, sons1.shape[0]):
            sons2[j, marker1:marker2] = individuals2[j, marker1:marker2]
            for i in arange(marker1, marker2):
                if(individuals1[j, i] in sons2[j, marker1:marker2]):
                    continue
                else:
                    sons2[j, self.find_position(individuals1[j, i], individuals2[j, :-1], \
                                                individuals1[j, :-1], marker1, marker2)]  \
                    = individuals1[j, i]         
            idx2 = sons2[j, :-1] == -1 
            sons2[j, :-1][idx2] = individuals1[j, :-1][idx2]

        new_population = concatenate([population, sons1, sons2], axis = 0)

        new_population[-1, :] = best

        return new_population, population.shape[0]

    def find_position(self, val, parents1, parents2, marker1, marker2):

        if(val in parents2[marker1:marker2]):
            idx = where(val == parents2)
            val = parents1[idx]
            return self.find_position(val, parents1, parents2, marker1, marker2)
        else:
            return where(val == parents2)


class PMXCrossover(object):

    def cross(self, population):
    
        individuals = random.permutation(population.shape[0])

        individuals1 = population[individuals[0:population.shape[0]/2], :]
        individuals2 = population[individuals[population.shape[0]/2:], :]

        markers = random.permutation(individuals1.shape[1]-1)[0:2]

        marker1 = min(markers)
        marker2 = max(markers)

        sons1 = -1*ones(individuals1.shape)
        sons2 = -1*ones(individuals1.shape)
 
        for j in arange(0, sons1.shape[0]):
            sons1[j, marker1:marker2] = individuals1[j, marker1:marker2]
            for i in arange(marker1, marker2):
                if(individuals2[j, i] in sons1[j, marker1:marker2]):
                    continue
                else:
                    sons1[j, self.find_position(individuals2[j, i], individuals1[j, :-1], \
                                                individuals2[j, :-1], marker1, marker2)]  \
                    = individuals2[j, i]
            idx1 = sons1[j, :-1] == -1 
            sons1[j, :-1][idx1] = individuals2[j, :-1][idx1]

        for j in arange(0, sons1.shape[0]):
            sons2[j, marker1:marker2] = individuals2[j, marker1:marker2]
            for i in arange(marker1, marker2):
                if(individuals1[j, i] in sons2[j, marker1:marker2]):
                    continue
                else:
                    sons2[j, self.find_position(individuals1[j, i], individuals2[j, :-1], \
                                                individuals1[j, :-1], marker1, marker2)]  \
                    = individuals1[j, i]         
            idx2 = sons2[j, :-1] == -1 
            sons2[j, :-1][idx2] = individuals1[j, :-1][idx2]

        new_population = concatenate([population, sons1, sons2], axis = 0)

        return new_population, population.shape[0]

    def find_position(self, val, parents1, parents2, marker1, marker2):

        if(val in parents2[marker1:marker2]):
            idx = where(val == parents2)
            val = parents1[idx]
            return self.find_position(val, parents1, parents2, marker1, marker2)
        else:
            return where(val == parents2)

class ElitistMPXCrossover(object):

    def cross(self, population):
    
        best = copy(population[argmax(population[:, -1])])

        individuals = random.permutation(population.shape[0])

        individuals1 = population[individuals[0:population.shape[0]/2], :]
        individuals2 = population[individuals[population.shape[0]/2:], :]

        markers = random.permutation(individuals1.shape[1]-1)[0:1]

        marker1 = min(markers)
        marker2 = max(markers)

        sons1 = -1*ones(individuals1.shape)
        sons2 = -1*ones(individuals1.shape)
 
        for j in arange(0, sons1.shape[0]):
            sons1[j, 0:marker2-marker1] = individuals1[j, marker1:marker2]
            sons1[j, marker2-marker1:-1] = setdiff1d(individuals2[j, :-1], sons1[j, :-1])
            sons2[j, 0:marker2-marker1] = individuals2[j, marker1:marker2]
            sons2[j, marker2-marker1:-1] = setdiff1d(individuals1[j, :-1], sons2[j, :-1])
    
        new_population = concatenate([population, sons1, sons2], axis = 0)

        new_population[-1, :] = best

        return new_population, population.shape[0]


class MPXCrossover(object):

    def cross(self, population):
    
        individuals = random.permutation(population.shape[0])

        individuals1 = population[individuals[0:population.shape[0]/2], :]
        individuals2 = population[individuals[population.shape[0]/2:], :]

        markers = random.permutation(individuals1.shape[1]-1)[0:1]

        marker1 = min(markers)
        marker2 = max(markers)

        sons1 = -1*ones(individuals1.shape)
        sons2 = -1*ones(individuals1.shape)
 
        for j in arange(0, sons1.shape[0]):
            sons1[j, 0:marker2-marker1] = individuals1[j, marker1:marker2]
            sons1[j, marker2-marker1:-1] = setdiff1d(individuals2[j, :-1], sons1[j, :-1])
            sons2[j, 0:marker2-marker1] = individuals2[j, marker1:marker2]
            sons2[j, marker2-marker1:-1] = setdiff1d(individuals1[j, :-1], sons2[j, :-1])
    
        new_population = concatenate([population, sons1, sons2], axis = 0)

        return new_population, population.shape[0]


class OXCrossover(object):

    def cross(self, population):
    
        individuals = random.permutation(population.shape[0])

        individuals1 = population[individuals[0:population.shape[0]/2], :]
        individuals2 = population[individuals[population.shape[0]/2:], :]

        markers = random.permutation(individuals1.shape[1]-1)[0:1]

        marker1 = min(markers)
        marker2 = max(markers)

        sons1 = zeros(individuals1.shape)
        sons2 = zeros(individuals1.shape)

        sons1[:, :-1] = c_[individuals1[:, :marker1], individuals2[:, marker1:marker2][::], individuals1[:, marker2:-1]]
        sons2[:, :-1] = c_[individuals2[:, :marker1][::-1], individuals1[:, marker1:marker2], individuals2[:, marker2:-1][::-1]]

        new_population = concatenate([population, sons1, sons2], axis = 0)

        return new_population, population.shape[0]

class ElitistOXCrossover(object):

    def cross(self, population):
    
        best = copy(population[argmax(population[:, -1])])

        individuals = random.permutation(population.shape[0])

        individuals1 = population[individuals[0:population.shape[0]/2], :]
        individuals2 = population[individuals[population.shape[0]/2:], :]

        markers = random.permutation(individuals1.shape[1]-1)[0:1]

        marker1 = min(markers)
        marker2 = max(markers)

        sons1 = zeros(individuals1.shape)
        sons2 = zeros(individuals1.shape)

        sons1[:, :-1] = c_[individuals1[:, :marker1], individuals2[:, marker1:marker2][::-1], individuals1[:, marker2:-1]]
        sons2[:, :-1] = c_[individuals2[:, :marker1][::-1], individuals1[:, marker1:marker2], individuals2[:, marker2:-1][::-1]]

        new_population = concatenate([population, sons1, sons2], axis = 0)

        new_population[-1, :] = best

        return new_population, population.shape[0]
        
