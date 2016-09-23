from numpy import *
from copy import copy

class StocasticUnivSamplingSelection(object):

    def select(self, population):

        norm_fitness = population[:, -1] - min(population[:, -1])
        norm_fitness = norm_fitness/sum(norm_fitness)
        
        sort_idx = argsort(norm_fitness)
        roullete = cumsum(sort(norm_fitness))
        
        select_range = 1.0/(population.shape[0]/2)
        points = random.rand(1)*select_range + select_range*arange(0, population.shape[0]/2)

        survivors = zeros((population.shape[0]/2, population.shape[1]))
        for i in arange(population.shape[0]/2):
            idx = sum(points[i] > roullete)
            survivors[i, :] = population[sort_idx[idx], :]

        return survivors

class ElitistStocasticUnivSamplingSelection(object):

    def select(self, population):

        best = copy(population[argmax(population[:, -1])])

        norm_fitness = population[:, -1] - min(population[:, -1])
        norm_fitness = norm_fitness/sum(norm_fitness)
        
        sort_idx = argsort(norm_fitness)
        roullete = cumsum(sort(norm_fitness))
        
        select_range = 1.0/(population.shape[0]/2)
        points = random.rand(1)*select_range + select_range*arange(0, population.shape[0]/2)

        survivors = zeros((population.shape[0]/2, population.shape[1]))
        for i in arange(population.shape[0]/2):
            idx = sum(points[i] > roullete)
            survivors[i, :] = population[sort_idx[idx], :]

        survivors[-1, :] = best

        return survivors

class TournamentSelection(object):

    def __init__(self, tournament_percent):
        self.percent = tournament_percent

    def select(self, population):

        population_size = population.shape[0]/2
        
        tournament_elem_nb = int(self.percent*population_size)

        survivors = zeros((population_size, ))

        for i in arange(population_size):
            participants = random.permutation(population.shape[0])[0:tournament_elem_nb]
            survivors[i] = participants[argmax(population[participants, -1])]

        return population[survivors.astype('int'), :]

class ElitistTournamentSelection(object):

    def __init__(self, tournament_percent):
        self.percent = tournament_percent

    def select(self, population):

        best = population[argmax(population[:, -1])]

        population_size = population.shape[0]/2
        
        tournament_elem_nb = int(self.percent*population_size)

        survivors = zeros((population_size, ))

        for i in arange(population_size):
            participants = random.permutation(population.shape[0])[0:tournament_elem_nb]
            survivors[i] = participants[argmax(population[participants, -1])]

        population = population[survivors.astype('int'), :]
        population[-1, :] = best

        return population



