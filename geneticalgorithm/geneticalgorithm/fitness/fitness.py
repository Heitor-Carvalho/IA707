from numpy import *
from copy import copy

class FitnessSharing(object):
    
    def __init__(self, sigma, alpha, betta):
        self.sig = sigma
        self.alpha = alpha
        self.beta = betta

    def shared_fitness(self, population):

        dist_axis = zeros((population.shape[0], population.shape[0]))
        for i in arange(0, population.shape[1]-1):
            pop1_axis, pop2_axis = meshgrid(population[:, i], population[:, i])
            dist_axis += (pop1_axis - pop2_axis)**2

        dist = dist_axis**0.5

        idx = dist < self.sig

        sh = zeros((population.shape[0], population.shape[0]))
        sh[idx] = 1 - (dist[idx]/self.sig)**self.alpha
        
        c = sum(sh, axis = 0)
        
        return (population[:, -1]**self.beta)/c        
