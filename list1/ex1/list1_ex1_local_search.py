
from numpy import *
import copy
    
import geneticalgorithm.crossoperator.binary_cross as bincross
import geneticalgorithm.mutatoroperator.binary_mutation as binmut
import geneticalgorithm.selectionoperator.selection as selec


objects = loadtxt('sum_diff_order.txt')

def local_seach(best):
    best.shape = (1, size(best))
    changes = eye(size(best)-1)
    for change in changes:
        best_candidate = copy.copy(best)
        best_candidate[0, :-1] = best_candidate[0, :-1].astype('bool')^change.astype('bool')
        
        best_candidate[0, -1] = objective_fun(objects, best_candidate)
        if(best_candidate[0,-1] > best[0, -1]):
            best = best_candidate
    
    return best

def objective_fun(objects, population):
    
    for i in arange(population.shape[0]):
        idx = population[i, :-1] > 0.5
        population[i, -1] = -abs(sum(objects[idx]) - sum(objects[~idx]))
    
    return population[:, -1]


def main():
        
    max_iteration = 400

    bin_mutation_par = {}
    bin_mutation_par['steps'] = array([0.1, 0.2, 0.3, 0.4, 0.8])*max_iteration
    bin_mutation_par['steps'] = bin_mutation_par['steps'].astype('int')
    bin_mutation_par['probs'] = [0.3, 0.2, 0.08, 0.025, 0.015, 0.01]

    binmut_op = binmut.PunctualStepBinaryMutation(bin_mutation_par)

    cross_op = bincross.OnePointCrossover()    
    selection_op = selec.ElitistTournamentSelection(0.6)

    N = 200

    init_sol = zeros((N, objects.shape[0]))
    i = 0
    while i < N:
        init_sol[i] = random.rand(1, objects.shape[0]) > 0.5
        if(sum(init_sol[i])/objects.shape[0] > 0.6 or sum(init_sol[i])/objects.shape[0] < 0.4):
            continue
        else:
            i += 1

    population = concatenate([init_sol, zeros((init_sol.shape[0], 1))], axis = 1)

    sons1 = zeros((population.shape[0]/2, population.shape[1]))
    sons2 = zeros((population.shape[0]/2, population.shape[1]))

    fitness_tracking = zeros((max_iteration, 3))

    for i in arange(max_iteration):

        population[:, -1] = objective_fun(objects, population)
        best = copy.copy(population[argmax(population[:, -1]), :])
        population[:, :-1] = binmut_op.mutate(population[:, :-1].astype('bool'), i)
        population[0] = best

        individuals = random.permutation(population.shape[0])

        sons1[:, 0:-1], sons2[:, 0:-1] = cross_op.cross(population[individuals[0:N/2], :-1], population[individuals[N/2:], :-1])

        new_population = concatenate([population, sons1, sons2], axis = 0)
        new_population[:, -1] = objective_fun(objects, new_population)
        
        new_population[0] = best
        
        best = copy.copy(new_population[argmax(new_population[:, -1]), :])
        population = selection_op.select(new_population)   
        population[0] = best
        
        fitness_tracking[i, 0] = max(population[:, -1])
        fitness_tracking[i, 1] = min(population[:, -1])
        fitness_tracking[i, 2] = mean(population[:, -1])

        if(i % 80 == 0):
            best = local_seach(best)
        
#        print 'Max %s, Min %s, Mean %s, It %s' % (max(population[:, -1]), min(population[:, -1]), mean(population[:, -1]), i)

    savetxt('fitness_evol', fitness_tracking, fmt='%1.4f')
    savetxt('best_sol', best, fmt='%1.4f')





if __name__ == '__main__':
    main()