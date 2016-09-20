
from numpy import *
import copy

import geneticalgorithm.mutatoroperator.real_mutation as realmut
import geneticalgorithm.crossoperator.real_cross as realcross
import geneticalgorithm.selectionoperator.selection as selec
import geneticalgorithm.fitness.fitness_sharing as fitsh


def objective_fun(value):
    x = value[:, 0]
    y = value[:, 1]
    return x*sin(4*pi*x) - y*sin(4*pi*y + pi) + 1

def main():
    # Population size
    N = 100
    max_mut_it = 100
    max_iteration = 100

    # Instantiating mutator operator
    mutation_op = realmut.NonUniformMutation(-1, 2, 1.4, max_mut_it)
    cross_op =  realcross.SpeciationCrossover()
    selection_op = selec.TournamentSelection(0.15)
    fitsh_op = fitsh.FitnessSharing(0.7, 1)

    # Random population in the interval [-1, 2] 
    init_solutions = 3*random.rand(N, 2) - 1;
    population = concatenate([init_solutions, zeros((init_solutions.shape[0], 1))], axis = 1)

    # Initializing sons
    sons1 = zeros((population.shape[0]/2, population.shape[1]))
    sons2 = zeros((population.shape[0]/2, population.shape[1]))
    
    fitness_tracking = zeros((max_iteration, 3))

    for i in arange(max_iteration):
    
        # Generate mutation
        population[:, 0:-1] = mutation_op.mutate(population[:, 0:-1], i)

        # Crossing individuals (double the population)
        population[:, -1] = objective_fun(population)
        sons1[:, 0:-1], sons2[:, 0:-1] = cross_op.cross(population)
       
        # New population with double size
        new_population = concatenate([population, sons1, sons2], axis = 0)

        # Calculating population fitness
        new_population[:, -1] = objective_fun(new_population[:, 0:-1])
        
        fitness_tracking[i, 0] = max(new_population[:, -1])
        fitness_tracking[i, 1] = min(new_population[:, -1])
        fitness_tracking[i, 2] = mean(new_population[:, -1])
       # Calculating fitness sharing
        new_population[:, -1] = fitsh_op.shared_fitness(new_population)

        # Selecting individuals
        population = selection_op.select(new_population)   

        savetxt('population' + str(i), population, fmt='%1.4f')

 
        print 'Max %s, Min %s, Mean %s' % (max(population[:, -1]), min(population[:, -1]), mean(population[:, -1]))
        
    savetxt('fitness_evol', fitness_tracking, fmt='%1.4f')
#    savetxt('best_sol', best, fmt='%1.4f')

if __name__ == '__main__':
    main()