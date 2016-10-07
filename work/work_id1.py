from numpy import *
import copy

import geneticalgorithm.crossoperator.binary_cross as bincross
import geneticalgorithm.mutatoroperator.binary_mutation as binmut
import geneticalgorithm.selectionoperator.selection as selec


def objective_fun(costs, population):

    for i in arange(population.shape[0]):
        idx = where((population[i, :-1] == 1))[0]
        if(idx.shape[0] == 0):
            population[i, -1] = -100000
            continue
        
        population[i, -1] = - costs[0, idx[0]]
        j = 0
        while(j < idx.shape[0]-1):
            population[i, -1] = population[i, -1] - costs[idx[j], idx[j+1]]
            j += 1
        population[i, -1] = population[i, -1] - costs[idx[j], costs.shape[0]-1]


    return population[:, -1]


def main():
        
    costs = loadtxt('costs.txt')

    max_iteration = 1000

    bin_mutation_par = {}
    bin_mutation_par['steps'] = array([0.1, 0.2, 0.3, 0.4, 0.8])*max_iteration
    bin_mutation_par['steps'] = bin_mutation_par['steps'].astype('int')
    bin_mutation_par['probs'] = [0.03, 0.02, 0.01, 0.008, 0.005, 0.004]

    # Instantiating genetic operators
    binmut_op = binmut.ElitistPunctualStepBinaryMutation(bin_mutation_par)
    cross_op = bincross.ElitistTwoPointCrossover()    
    selection_op = selec.ElitistTournamentSelection(0.8)

    N = 200

    # Generating population
    init_sol = random.rand(N, costs.shape[0]) > 0.996

    population = concatenate([init_sol, zeros((init_sol.shape[0], 1))], axis = 1)
    new_population = zeros((population.shape[0]*2, population.shape[1]))

    # Creating fitness tracking
    fitness_tracking = zeros((max_iteration, 3))
    import pdb; pdb.set_trace()
    
    for i in arange(max_iteration):

        # Population fitness evaluation
        population[:, -1] = objective_fun(costs, population)

        # Population mutation
        population = binmut_op.mutate(population, i)

        # Population crossover
        new_population, idx_sons = cross_op.cross(population)

        # Fitness evaluation
        new_population[:, -1] = objective_fun(costs, new_population)

        # Selecting individuals                
        population = selection_op.select(new_population)   

        fitness_tracking[i, 0] = max(population[:, -1])
        fitness_tracking[i, 1] = min(population[:, -1])
        fitness_tracking[i, 2] = mean(population[:, -1])
        
        print 'Max %s, Min %s, Mean %s, It %s' % (max(population[:, -1]), min(population[:, -1]), mean(population[:, -1]), i)

    savetxt('fitness_evol', fitness_tracking, fmt='%1.4f')
    savetxt('best_sol', population[argmax(population[:, -1])], fmt='%1.4f')







if __name__ == '__main__':
    main()