from numpy import *
from copy import copy

# To Do: update to new interface and create elitist version
class PunctualBinaryMutation():

    def __init__(self, bin_mutation_par):

        self.mut_prob = bin_mutation_par["initial_prob"]
        self.min_prob = bin_mutation_par["min_prob"]

    def reset_probability(self):
    	self.mut_prob = self.mut_parameters["initial_prob"]

    def mutate(self, population, iteraction):

        mutation = random.random((population.shape)) < self.mut_prob
        self.mut_prob = max(self.mut_prob*0.9, self.min_prob)

        return population^mutation

# To Do: update to new interface and create elitist version
class PunctualExpBinaryMutation():

    def __init__(self, bin_mutation_par):

        self.mut_prob = bin_mutation_par["initial_prob"]
        self.coef = bin_mutation_par['exp_coef']
        self.min_prob = bin_mutation_par['min_prob']

    def mutate(self, population, iteraction):
        mutation = random.random((population.shape[0], population.shape[1]-1)) < self.mut_prob
        self.mut_prob = max(self.mut_prob*exp(-self.coef*iteraction), self.min_prob)
        population[:,:-1] =  population[:, :-1].astype('bool') ^ mutation.astype('bool')
        return population

class PunctualStepBinaryMutation():

    def __init__(self, bin_mutation_par):

        self.steps = bin_mutation_par['steps']
        self.probs = bin_mutation_par['probs']

    def mutate(self, population, iteraction):
        
        idx = sum(self.steps < iteraction)
        mutation = random.random((population.shape)) < self.probs[idx]

        new_generation = zeros(population.shape)
        new_generation[:, :-1] = population[:, :-1].astype('bool') ^ mutation[:, :-1].astype('bool')

        return new_generation


class ElitistPunctualStepBinaryMutation():

    def __init__(self, bin_mutation_par):

        self.steps = bin_mutation_par['steps']
        self.probs = bin_mutation_par['probs']

    def mutate(self, population, iteraction):
        
        best = copy(population[argmax(population[:, -1])])

        idx = sum(self.steps < iteraction)
        mutation = random.random((population.shape)) < self.probs[idx]
        
        new_generation = zeros(population.shape)
        new_generation[:, :-1] = population[:, :-1].astype('bool') ^ mutation[:, :-1].astype('bool')

        new_generation[-1, :] = best
        
        return new_generation


