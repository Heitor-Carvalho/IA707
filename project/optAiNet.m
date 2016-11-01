

clear all

addpath([pwd '/functions'])
addpath([pwd '/operators'])

% Population parameters
N = 5;                                             % Initial population size
L = 2;                                             % Parameters length
MaxN = 200;                                        % Maximun allowed population size

% Population replacement interval
pop_fact = 0.1;                                    % Population percentage that will be replaced

% Fitness function 
fitness_op = @bukin;
fitness_gf = @bukin_graph;

% Mutation operator and parameters
mutator_op = @clone_hypermutate;
beta = 1;
sigma_max = 0.1;
mut_const = 1;
min = -1;
max = 2;

% Affinity threshold
sig_thr = 0.25;

% Stability thershold
stability_trh = 4e-2;

% Clone parameters
clone_factor = 0.5;                               % Number of clones per indivídual = 0.5*N (population size)
Nc = N;

% Creating initial population
population = 3*rand(N, L)-1;

% Figures graph
[gridx, gridy, surf_val] = list_function_graph(-1, 2, fitness_gf); 

itMax = 200;

% Initiating variables
average_fitness = 0;

for it = 1:itMax
  
  % Fitness, average fitness and current population size
  fitness = fitness_op(population);
  average_fitness = mean(fitness);
  N = size(population,1);

  % Cloning and Mutating 
  clones = mutator_op(population, clone_factor, fitness, sigma_max, mut_const, beta, min, max);

  % Finding best clone for each individual
  fitness = fitness_op(clones);
  bests_idx = [];
  for i = 1:N
    idx_blk = i:N:size(fitness,1);  
    [val, idx] = sort(fitness(idx_blk));
    bests_idx(i) = idx_blk(idx(end));
  end
  
  % New population sorted by fitness
  [fitness, idx] = sort(fitness(bests_idx));
  population(1:N, :) = clones(bests_idx(idx), :);
  
  if(abs(average_fitness - mean(fitness)) < stability_trh)
    % Cleaning population
    new_pop = [];
    while(~isempty(population))
      affinit = affitnity(population, size(population,1));
      idx = find(affinit < sig_thr);
      
      % Holding the best individual
      [best_thr, best_thr_idx] = sort(fitness(idx));
      new_pop = [new_pop; population(idx(best_thr_idx(end)), :)];
      
      % Indexing removed individuals
      rm_idx = ones(size(population,1),1);
      rm_idx(idx(best_thr_idx)) = 0;
      
      % Cleaning population
      population = population(rm_idx == 1,:);
    end
    population = new_pop;  

    % Adding new random individuals
    population = [population; 3*rand(ceil(N*pop_fact), L)-1];
  
  end
  

  figure(1)
  clf
  mesh(gridx, gridy, surf_val)
  hold on
  plot3(population(:,1), population(:,2), fitness_op(population),'*')
  drawnow()
  grid;

end    
    
  


