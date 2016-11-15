% clear all

addpath([pwd '/..'])
addpath([pwd '/../functions'])
addpath([pwd '/operators'])

% Algorithm parameters
N = 120;                                           % Population size
L = 2;                                             % Parameters length
pop_fact = 0.1;                                    % Population percentage that will be replaced
iterval = 30;                                      % Interval used to add new random individuals

clone_factor = 4/N;                                % Number of clones per indivídual = clone_factor*N (population size)

beta = 1;                                          % Mutation constant
sigma_max = 0.05;                                  % Max sigma constant
mut_const = 0.5;                                   % Mutation decay constant

itMax = 600;                                       % Maximum number of iterations
maxEval = 4e4;                                     % Maximum number of evaluations

min_r = -1;                                        % Minimum limit
max_r = 2;                                         % Maximum limit

% Mutation operator and parameters
mutator_op = @clone_hypermutate;

% Fitness function 
fitness_op = @list_function;
fitness_gf = @list_function_graph;

% ---------------------------------------------------------------------------------------------------%
% ---------------------------------------------------------------------------------------------------%
% ---------------------------------------------------------------------------------------------------%

% Figures graph
[gridx, gridy, surf_val] = generate_graph(min_r, max_r, fitness_gf); 

% Creating initial population
population = (max_r-min_r)*rand(N, L) + min_r;
bests_idx = zeros(N, 1);

% Parameters history
fitness_avg_hist = zeros(itMax, 1);
fitness_min_hist = zeros(itMax, 1);
fitness_max_hist = zeros(itMax, 1);

% Evaluation parameters
load('list_fitness_min');
eps = 0.05;
np = zeros(itMax, 1);
total_fit = zeros(itMax, 1);

% Initiating variables
it = 0;
eval = 0;

while(it < itMax && eval <= maxEval)
    
  fitness = fitness_op(population);
  
  % Counting number of iterations used
  it = it + 1;

  % Filling history
  fitness_avg_hist(it) = mean(fitness);
  fitness_min_hist(it) = min(fitness);
  fitness_max_hist(it) = max(fitness);
  [np(it), total_fit(it)] = minimum_metrics(population, min_locals, min_fitness, eps); 


  % Cloning and Mutating 
  clones = mutator_op(population, clone_factor, fitness, sigma_max, mut_const, beta, min_r, max_r);
  
  % Finding best clone for each individual
  fitness = fitness_op(clones);
  eval = eval + size(clones, 1);

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
    population(idx(1:ceil(N*pop_fact)), :) = (max_r-min_r)*rand(ceil(N*pop_fact), L) + min_r;
    eval = eval + ceil(N*pop_fact);
  end
  
  % Ploting
  figure(1)
  clf
  mesh(gridx, gridy, surf_val)
  hold on
  plot3(population(:,1), population(:,2), fitness_op(population),'*')
  drawnow()
  grid on;  
  

end  
  
    
  


