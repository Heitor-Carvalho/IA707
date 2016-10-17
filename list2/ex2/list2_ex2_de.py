
from numpy import *
import copy

import geneticalgorithm.mutatoroperator.real_mutation as realmut
import geneticalgorithm.crossoperator.real_cross as realcross
import geneticalgorithm.selectionoperator.selection as selec

# sphere test function
def objective_fun(value, it):

    x = value[:, 0]
    y = value[:, 1]
    
    fitness = -(x*x + y*y)     

    if(it > 50):
        fitness = -((x-1)*(x-1) + (y-1)*(y-1))
    if(it > 100):
        fitness = -((x-2)*(x-2) + (y-2)*(y-2))
    if(it > 150):
        fitness = -((x-3)*(x-3) + (y-3)*(y-3))

    return fitness

def objective_fun(value, it):
    x = value[:, 0]
    y = value[:, 1]
    
    fitness = x*sin(4*pi*x) - y*sin(4*pi*y + pi) + 1
    fitness[x > 2] = -10
    fitness[x < -1] = -10
    fitness[y > 2] = -10
    fitness[y < -1] = -10
     
    return fitness

def main():
    max_iteration = 80

    # Population parameters
    N = 25

    max_mut_it = max_iteration

    # Instantiating genetic operators
    mutation_op = realmut.DEMutation(0.3) 
    cross_op =  realcross.DECrossover(0.5)
    selection_op = selec.DESelection()

    # Generating population
    init_solutions = 2*random.rand(N, 2)-1;
    population = concatenate([init_solutions, zeros((init_solutions.shape[0], 1))], axis = 1)
    mut_population = zeros((population.shape[0], population.shape[1]))

    # Creating fitness tracking
    fitness_tracking = zeros((max_iteration, 3))

    for i in arange(max_iteration):

        # Population mutation
        mut_population = mutation_op.mutate(population, i)

        # Population crossover
        new_population, idx_sons = cross_op.cross(population, mut_population)

        # Fitness evaluation
        population[:, -1] = objective_fun(population, i)
        new_population[:, -1] = objective_fun(new_population, i)
        
        # Selecting individuals                
        population = selection_op.select(population, new_population)   
        
        fitness_tracking[i, 0] = max(population[:, -1])
        fitness_tracking[i, 1] = min(population[:, -1])
        fitness_tracking[i, 2] = mean(population[:, -1])
        
        print 'Max %s, Min %s, Mean %s, It %s' % (max(population[:, -1]), min(population[:, -1]), mean(population[:, -1]), i)

        
    savetxt('fitness_evol', fitness_tracking, fmt='%1.4f')
    savetxt('best_sol', population[argmax(population[:, -1])], fmt='%1.4f')

if __name__ == '__main__':
    main()