% clear all

addpath([pwd '/../'])
addpath([pwd '/../functions'])
addpath([pwd '/operators/crossover'])
addpath([pwd '/operators/mutation'])
addpath([pwd '/operators/selection'])
addpath([pwd '/operators/niching'])

% Algorithm parameters
N = 100;                                        % Population size                                         
L = 2;                                          % Parameters length

max_sig = 0.05;                                 % Max sigma constant
mut_const = 0.25;                                % Mutation decay constant

d = 0.25;                                       % Affinity threshold

itMax = 600;                                    % Maximum number of iterations
maxEval = 4e4;                                  % Maximum number of evaluations

min_r = -1;                                     % Minimum limit
max_r = 2;                                      % Maximum limit

% Fitness function 
fitness_op = @list_function;
fitness_gf = @list_function_graph;

% ---------------------------------------------------------------------------------------------------%
% ---------------------------------------------------------------------------------------------------%
% ---------------------------------------------------------------------------------------------------%

% Figures graph
[gridx, gridy, surf_val] = generate_graph(min_r, max_r, fitness_gf); 

% Creating initial population
new_population = (max_r-min_r)*rand(2*N, L) + min_r;

% Parameters history
fitness_avg_hist = zeros(1, itMax);
fitness_min_hist = zeros(1, itMax);
fitness_max_hist = zeros(1, itMax);

% Evaluation parameters
load('list_fitness_min');
eps = 0.05;
np = zeros(itMax, 1);
total_fit = zeros(itMax, 1);

% Initiating variables
it = 0;
eval = 0;

while(it < itMax && eval <= maxEval)

  % Fitness, average fitness
  fitness = fitness_op(new_population);

  % Counting number of iterations used
  it = it + 1;
  eval = eval + size(new_population, 1);

  % Filling history
  fitness_avg_hist(it) = mean(fitness);
  fitness_min_hist(it) = min(fitness);
  fitness_max_hist(it) = max(fitness);
  [np(it), total_fit(it)] = minimum_metrics(population, min_locals, min_fitness, eps); 

  fitness = clearing(new_population, fitness, d);  

  population = sus(new_population, fitness);

  % Ploting
  figure(1)
  clf
  mesh(gridx, gridy, surf_val)
  hold on
  plot3(population(:,1), population(:,2), fitness_op(population(:,:)),'*')
  drawnow()
  grid;


  new_population = crossover(population);
  new_population = mutation(new_population, max_sig, mut_const, it, min_r, max_r);

end 