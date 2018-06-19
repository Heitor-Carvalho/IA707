
from numpy import *
import copy

import geneticalgorithm.crossoperator.binary_cross as bincross
import geneticalgorithm.mutatoroperator.binary_mutation as binmut
import geneticalgorithm.selectionoperator.selection as selec

# Matriz grid size
GRID_SIZE = 5;

C = ones((GRID_SIZE, GRID_SIZE))
D = zeros((GRID_SIZE, GRID_SIZE))
A = (random.rand(GRID_SIZE, GRID_SIZE) > 0.5).astype('int')

def frobeus_dist(A, B):
  return sqrt(trace((A-B)*(A-B).T));

def objective_fun(population):
  s_max = frobeus_dist(C,D)
  fitness = zeros((population.shape[0], ))
  for i, individual in enumerate(population):
    B = reshape(individual[0:-1], (GRID_SIZE, GRID_SIZE))
    fitness[i] =  -sum(abs(A-B))

  return fitness

def main():

    max_iteration = 100

    bin_mutation_par = {}
    bin_mutation_par['steps'] = array([0.1, 0.2, 0.3, 0.7])*max_iteration
    bin_mutation_par['steps'] = bin_mutation_par['steps'].astype('int')
    bin_mutation_par['probs'] = [0.5, 0.2, 0.01, 0.005, 0.001]

    # Instantiating genetic operators
    binmut_op = binmut.PunctualStepBinaryMutation(bin_mutation_par)
    cross_op = bincross.OnePointCrossover()
    selection_op = selec.ElitistTournamentSelection(0.6)

    # Population size
    N = 30

    # Generating population
    init_sol = random.rand(N, GRID_SIZE**2) > 0.5

    population = concatenate([init_sol, zeros((init_sol.shape[0], 1))], axis = 1)
    new_population = zeros((population.shape[0]*2, population.shape[1]))

    # Creating fitness tracking
    fitness_tracking = zeros((max_iteration, 3))
    for i in arange(max_iteration):

        # Population fitness evaluation
        population[:, -1] = objective_fun(population)

        # Population mutation
        population = binmut_op.mutate(population, i)

        # Population crossover
        new_population, idx_sons = cross_op.cross(population)

        # Fitness evaluation
        new_population[:, -1] = objective_fun(new_population)

        # Selecting individuals
        population = selection_op.select(new_population)

        fitness_tracking[i, 0] = max(population[:, -1])
        fitness_tracking[i, 1] = min(population[:, -1])
        fitness_tracking[i, 2] = mean(population[:, -1])

        print 'Max %s, Min %s, Mean %s, It %s' % (max(population[:, -1]), min(population[:, -1]), mean(population[:, -1]), i)

    idx_sort_fitness = argmax(population[:, -1])
    best_one = population[idx_sort_fitness, :-1]
    print float(sum(A == reshape(best_one, (GRID_SIZE, GRID_SIZE))))/GRID_SIZE**2
    savetxt('fitness_evol', fitness_tracking, fmt='%1.4f')
    savetxt('best_sol', population[argmax(population[:, -1])], fmt='%1.4f')

if __name__ == '__main__':
    main()
