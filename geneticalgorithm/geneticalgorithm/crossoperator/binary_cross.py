from copy import copy
from numpy import *

# To Do: update to new interface and create elitist version
class TwoPointCrossover():
    
    def cross(self, individuals1, individuals2):

        markers = random.permutation(individuals1.shape[1])[0:1]

        marker1 = min(markers)
        marker2 = max(markers)

        sons1 = c_[individuals1[:, :marker1], individuals2[:, marker1:marker2][::-1], individuals1[:, marker2:]]
        sons2 = c_[individuals2[:, :marker1][::-1], individuals1[:, marker1:marker2], individuals2[:, marker2:][::-1]]

        return (sons1, sons2)

class OnePointCrossover():
    
    def cross(self, population):

        individuals = random.permutation(population.shape[0])

        individuals1 = population[individuals[0:population.shape[0]/2], :]
        individuals2 = population[individuals[population.shape[0]/2:], :]
 
        marker = random.permutation(individuals1.shape[1]-1)[0]

        sons1 = c_[individuals1[:, :marker], individuals2[:, marker:]]
        sons2 = c_[individuals2[:, :marker], individuals1[:, marker:]]

        sons1 = zeros(individuals1.shape)
        sons2 = zeros(individuals1.shape)

        sons1[:, :-1] = c_[individuals1[:, :marker], individuals2[:, marker:-1]]
        sons2[:, :-1] = c_[individuals2[:, :marker], individuals1[:, marker:-1]]

        new_population = concatenate([population, sons1, sons2], axis = 0)

        return new_population, population.shape[0]

class ElitistOnePointCrossover():
    
    def cross(self, population):

        best = copy(population[argmax(population[:, -1])])

        individuals = random.permutation(population.shape[0])

        individuals1 = population[individuals[0:population.shape[0]/2], :]
        individuals2 = population[individuals[population.shape[0]/2:], :]
 
        marker = random.permutation(individuals1.shape[1]-1)[0]
        
        sons1 = zeros(individuals1.shape)
        sons2 = zeros(individuals1.shape)

        sons1[:, :-1] = c_[individuals1[:, :marker], individuals2[:, marker:-1]]
        sons2[:, :-1] = c_[individuals2[:, :marker], individuals1[:, marker:-1]]

        new_population = concatenate([population, sons1, sons2], axis = 0)

        new_population[-1, :] = best

        return new_population, population.shape[0]

