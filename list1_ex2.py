
from numpy import *

import binary_mutation as binmut
import permutation_cross as permcross
import selection as selec

def objective_fun(objects, max_capacity, population):
    
    for i in arange(population.shape[0]):
        idx = population[i, :-1] > 0.5
        total_wigth = sum(objects[:, 0][idx])
        total_val = sum(objects[:, 1][idx])

        if(total_wigth > max_capacity):
            total_val = -(total_val - max_capacity)
#            total_val = 0
        population[i, -1] = total_val

    return population[:, -1]


def main():
        
    objects = loadtxt('knapsack.txt')
    max_capacity = 6404180
    max_iteration = 100

    bin_mutation_par = {}
    bin_mutation_par['initial_prob'] = 0 
    bin_mutation_par['exp_coef'] = 0.001	

    cross_op = permcross.OxCrossover()    
    binmut_op = binmut.PunctualExpBinaryMutation(bin_mutation_par)
    selection_op = selec.TournamentSelection(0.25)

    
    N = 100

    init_sol = random.rand(N, objects.shape[0]) > 0.5
    population = concatenate([init_sol, zeros((init_sol.shape[0], 1))], axis = 1)

    sons1 = zeros((population.shape[0]/2, population.shape[1]))
    sons2 = zeros((population.shape[0]/2, population.shape[1]))
    
    for i in arange(max_iteration):

        population[:, :-1] = binmut_op.mutate(population[:, :-1].astype('bool'), i)

        individuals = random.permutation(population.shape[0])


        sons1[:, 0:-1], sons2[:, 0:-1] = cross_op.cross(population[individuals[0:N/2], :-1], population[individuals[N/2:], :-1])

        new_population = concatenate([population, sons1, sons2], axis = 0)
        new_population[:, -1] = objective_fun(objects, max_capacity, new_population)

        population = selection_op.select(new_population)   

        print 'Max %s, Min %s, Mean %s' % (max(population[:, -1]), min(population[:, -1]), mean(population[:, -1]))

    import pdb; pdb.set_trace()






if __name__ == '__main__':
    main()