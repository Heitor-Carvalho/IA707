
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
    max_iteration = 140

    # Population parameters
    N = 2
    M = 50

    max_mut_it = max_iteration

    # Instantiating genetic operators
    mutation_op = realmut.CorrelatedMutation(0.083, 0.21, 0.24) # beta, sqrt(2*par_len)^-1, sqrt(2*sqrt(par_len))^-1
    cross_op =  realcross.EEAndArithmeticCrossover(N, M)
    selection_op = selec.EEBestSelection(N)

    # Generating population
    init_solutions = 2*random.rand(N, 2)-1;
    population = concatenate([init_solutions, zeros((init_solutions.shape[0], 1))], axis = 1)
    
    # Generating evolution parameters
    evol_par = zeros((population.shape[0], 2))

    evol_par[:, 0:1] = 0.5
    evol_par[:, 1:2] = random.randn(N,1)

    new_population = zeros((population.shape[0]*2, population.shape[1]))

    # Creating fitness tracking
    fitness_tracking = zeros((max_iteration, 3))

    for i in arange(max_iteration):

        # Population crossover
        new_population, new_evol_par, idx_sons = cross_op.cross(population, evol_par)

        # Population mutation
        new_population, new_evol_par = mutation_op.mutate(new_population, i, new_evol_par)

        # Fitness evaluation
        new_population[:, -1] = objective_fun(new_population,i)
        
        # Selecting individuals                
        population, evol_par = selection_op.select(new_population, new_evol_par)   
        
        fitness_tracking[i, 0] = max(population[:, -1])
        fitness_tracking[i, 1] = min(population[:, -1])
        fitness_tracking[i, 2] = mean(population[:, -1])
        
        print 'Max %s, Min %s, Mean %s, It %s' % (max(population[:, -1]), min(population[:, -1]), mean(population[:, -1]), i)

        
    savetxt('fitness_evol', fitness_tracking, fmt='%1.4f')
    savetxt('best_sol', population[argmax(population[:, -1])], fmt='%1.4f')

if __name__ == '__main__':
    main()