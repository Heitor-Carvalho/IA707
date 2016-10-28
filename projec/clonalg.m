clear all

% Population parameters
N = 80;                                            % Population size
L = 2;                                             % Parameters length

% Population replacement interval
pop_fact = 0.05;                                   % Population percentage that will be replaced
iterval = 40;                                      % Interval used to add new random individuals

% Fitness function 
fitness_op = @drop_wave;
fitness_gf = @drop_wave_graph;

% Mutation operator and parameters
mutator_op = @clone_hypermutate;
beta = 1;
sigma_max = 0.1;
mut_const = 0.5;
min = -2;
max = 2;

% Clone parameters
clone_factor = 0.4;                               % Number of clones per indivídual = 0.5*N (population size)

% Creating initial population
population = (max-min)*rand(N, L) + min;

% Figures graph
[gridx, gridy, surf_val] = list_function_graph(min, max, fitness_gf); 

itMax = 200;

% Initiating variables 
bests_idx = zeros(N, 1);

for it = 1:itMax
    
  fitness = fitness_op(population);
  
  % Cloning and Mutating 
  clones = mutator_op(population, clone_factor, fitness, sigma_max, mut_const, beta, min, max);
  
  % Finding best clone for each individual
  fitness = fitness_op(clones);
  for i = 1:N
    idx_blk = i:N:size(fitness,1);  
    [val, idx] = sort(fitness(idx_blk));
    bests_idx(i) = idx_blk(idx(end));
  end
  
  % New population with the best clones
  population = clones(bests_idx, :);
  
  % Adding new random individuals
  if(mod(it, iterval) == 0)
    [val, idx] = sort(fitness(bests_idx));
    population(idx(1:ceil(N*pop_fact)), :) = (max-min)*rand(ceil(N*pop_fact), L) + min;
  end
  
  % Ploting
  figure(1)
  clf
  mesh(gridx, gridy, surf_val)
  hold on
  plot3(population(:,1), population(:,2), fitness_op(population),'*')
  drawnow()
  grid;

end  
  
    
  


