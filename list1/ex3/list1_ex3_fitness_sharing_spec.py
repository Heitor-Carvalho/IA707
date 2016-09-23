
from numpy import *
import copy

import geneticalgorithm.mutatoroperator.real_mutation as realmut
import geneticalgorithm.crossoperator.real_cross as realcross
import geneticalgorithm.selectionoperator.selection as selec
import geneticalgorithm.fitness.fitness as fitsh

def objective_fun(value):
    x = value[:, 0]
    y = value[:, 1]
    return x*sin(4*pi*x) - y*sin(4*pi*y + pi) + 1

def main():
    # Population size
    N = 100
    max_mut_it = 90
    max_iteration = 100 

    # Instantiating mutator operator
    mutation_op = realmut.ElitistPercentNonUniformMutation(-1, 2, 3, max_mut_it, 0.6)
    cross_op =  realcross.ElitistSpeciationCrossover(0.6)
    selection_op = selec.ElitistStocasticUnivSamplingSelection()
    fitsh_op = fitsh.FitnessSharing(0.5, 1, 2)

    # Random population in the interval [-1, 2] 
    init_solutions = 3*random.rand(N, 2) - 1;
    population = concatenate([init_solutions, zeros((init_solutions.shape[0], 1))], axis = 1)
    new_population = zeros((population.shape[0]*2, population.shape[1]))

    # Creating fitness tracking
    fitness_tracking = zeros((max_iteration, 3))

    for i in arange(max_iteration):
    
    
        # Population fitness evaluation
        population[:, -1] = objective_fun(population)

        fitness_tracking[i, 0] = max(population[:, -1])
        fitness_tracking[i, 1] = min(population[:, -1])
        fitness_tracking[i, 2] = mean(population[:, -1])

        # Population mutation
        population = mutation_op.mutate(population, i)

        # Population crossover
        new_population, idx_sons = cross_op.cross(population)

        # Fitness evaluation
        new_population[:, -1] = objective_fun(new_population)

        # Getting shared fitness
        new_population[:, -1] = fitsh_op.shared_fitness(new_population)
   
        # Selecting individuals                
        population = selection_op.select(new_population)   

        savetxt('population' + str(i), population, fmt='%1.4f')
        
        print 'Max %s, Min %s, Mean %s, It %s' % (max(population[:, -1]), min(population[:, -1]), mean(population[:, -1]), i)
        
    savetxt('fitness_evol', fitness_tracking, fmt='%1.4f')
    savetxt('best_sol', population[argmax(population[:, -1])], fmt='%1.4f')

if __name__ == '__main__':
    main()