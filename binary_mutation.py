import numpy as np

bin_mutation_par = {"initial_prob": 0.6, "min_prob": 0.01}


class BinaryMutation():

    def __init__(self, bin_mutation_par):

        self.mut_parameters = bin_mutation_par

	def puctual_mutation(bits, iteraction):
        
        if(iteraction == 0):
        	self.mut_prob = self.mut_parameters["initial_prob"]
        
        self.mut_prob = min(self.mut_prob**2, self.mut_parameters["min_prob"])
        
        mutation = np.random.randn(len(bits)) > self.mut_prob

        return bits + mutation




