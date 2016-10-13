from numpy import *
from copy import copy

class EEBestSelection(object):
    
    def __init__(self, mu):
        self.mu = mu

    def select(self, population, evol_par):

        best_idx = argsort(population[:, -1])[population.shape[0]-self.mu:population.shape[0]]

        return population[best_idx, :], evol_par[best_idx, :]
        

class PETournamentSelection(object):
    
    def __init__(self, tour_size):
        self.tour_size = tour_size

    def select(self, population):
        
        individuals = random.permutation(population.shape[0])[0:self.tour_size]

        score = zeros((population.shape[0], 1))
        for i in arange(0, population.shape[0]):
            score[i, :] = sum(population[i, -1] > population[individuals, -1])
                
        sort_idx = argsort(score[:, 0])

        survivors = copy(population[sort_idx, :][population.shape[0]/2:])

        return survivors


class EETournamentSelection(object):

    def __init__(self, tournament_percent, mu):
        self.percent = tournament_percent
        self.mu = mu

    def select(self, population, evol_par):

        population_size = population.shape[0]/2
        
        tournament_elem_nb = int(self.percent*population_size)

        survivors = zeros((self.mu, population.shape[1]))
        survivors_par = zeros((self.mu, evol_par.shape[1]))

        for i in arange(self.mu):
            participants = random.permutation(population.shape[0])[0:tournament_elem_nb]
            winner_idx = participants[argmax(population[participants, -1])]
            survivors[i, :] = population[winner_idx, :] 
            survivors_par[i] = evol_par[winner_idx, :]

        return survivors, survivors_par

class EEStocasticUnivSamplingSelection(object):

    def select(self, population, evol_par):

        norm_fitness = population[:, -1] - min(population[:, -1])
        norm_fitness = norm_fitness/sum(norm_fitness)
        
        sort_idx = argsort(norm_fitness)
        roullete = cumsum(sort(norm_fitness))
        
        select_range = 1.0/(population.shape[0]/2)
        points = random.rand(1)*select_range + select_range*arange(0, population.shape[0]/2)

        survivors = zeros((population.shape[0]/2, population.shape[1]))
        survivors_par = zeros((evol_par.shape[0]/2, evol_par.shape[1]))
        for i in arange(population.shape[0]/2):
            idx = sum(points[i] > roullete)
            survivors[i, :] = population[sort_idx[idx], :]
            survivors_par[i, :] = evol_par[sort_idx[idx], :]

        return survivors, survivors_par

class ElitistEEStocasticUnivSamplingSelection(object):

    def select(self, population, evol_par):

        best = copy(population[argmax(population[:, -1])])
        best_par = copy(evol_par[argmax(population[:, -1])])

        norm_fitness = population[:, -1] - min(population[:, -1])
        norm_fitness = norm_fitness/sum(norm_fitness)
        
        sort_idx = argsort(norm_fitness)
        roullete = cumsum(sort(norm_fitness))
        
        select_range = 1.0/(population.shape[0]/2)
        points = random.rand(1)*select_range + select_range*arange(0, population.shape[0]/2)

        survivors = zeros((population.shape[0]/2, population.shape[1]))
        survivors_par = zeros((evol_par.shape[0]/2, evol_par.shape[1]))
        for i in arange(population.shape[0]/2):
            idx = sum(points[i] > roullete)
            survivors[i, :] = population[sort_idx[idx], :]
            survivors_par[i, :] = evol_par[sort_idx[idx], :]

        survivors[-1, :] = best
        survivors_par[-1, :] = best_par

        return survivors, survivors_par

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



