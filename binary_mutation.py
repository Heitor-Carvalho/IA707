from numpy import *

class PunctualBinaryMutation():

    def __init__(self, bin_mutation_par):

        self.mut_prob = bin_mutation_par["initial_prob"]
        self.min_prob = bin_mutation_par["min_prob"]

    def reset_probability(self):
    	self.mut_prob = self.mut_parameters["initial_prob"]

    def mutate(self, bits_array, iteraction):

        mutation = random.random((bits_array.shape)) < self.mut_prob
        self.mut_prob = max(self.mut_prob*0.9, self.min_prob)

        return bits_array^mutation

class PunctualExpBinaryMutation():

    def __init__(self, bin_mutation_par):

        self.mut_prob = bin_mutation_par["initial_prob"]
        self.coef = bin_mutation_par['exp_coef']

    def mutate(self, bits_array, iteraction):

        mutation = random.random((bits_array.shape)) < self.mut_prob
        self.mut_prob = max(self.mut_prob*exp(-self.coef*iteraction), 0.1)

        return bits_array ^ mutation

# To do: Binary mutation using steps mod Interval
class PunctualStepBinaryMutation():

    def __init__(self, bin_mutation_par):

        self.mut_prob = bin_mutation_par["initial_prob"]
        self.coef = bin_mutation_par['exp_coef']

    def mutate(self, bits_array, iteraction):
        
        mutation = random.random((bits_array.shape)) < self.mut_prob
        self.mut_prob = max(self.mut_prob*exp(-self.coef*iteraction), 0.1)

        return bits_array ^ mutation


