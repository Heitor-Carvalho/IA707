from numpy import *

class RouletteWheelSelection(object):
    """docstring for RouletteWheel"""

    def select(self, population):

        roulette = cumsum(population[-1:, :])

        survivors = zeros((1, survivors_size))
        for i in arange(survivors_size):
            survivors[i] = np.where(roulette > 0.3)[0][0]
        
        return population[:, survivors]


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


class LinearRankSelection(object):

    def selec(self, population):
         
        sorted_population = population[:, population[-1, :].argsort()]

        # Notes: needs check in how the population size is controlled
        survivors = zeros((1, tournament_number))
        j = 0
        for i in arange(tournament_number):
            prob = (self.alpha + (i/(population.shape[1] - 1))*(self.beta - self.alpha))/population.shape[1]
            if(random.rand(1) > prob):
                survivors[j] = i
                j += 1

        return population[:, survivors]

class NonLinearRankSelection(object):
    """docstring for NonLinearRankSelection"""
        
    def selec(self, population):
         
        sorted_population = population[:, population[-1, :].argsort()]
        # Notes: needs check in how the population size is controlled
        survivors = zeros((1, tournament_number))
        j = 0
        for i in arange(tournament_number):
            prob = (self.alpha)*(1 - self.alpha)**(population.shape[1]-1-i)
            if(random.rand(1) > prob):
                survivors[j] = i
                j += 1

        return population[:, survivors]
    

