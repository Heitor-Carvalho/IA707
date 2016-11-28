% clear all

addpath([pwd '/..'])
addpath([pwd '/../functions'])
addpath([pwd '/operators'])

% Algorithm parameters
N = 10;                                            % Initial population size
L = 1;                                             % Parameters length
pop_fact = 0.2;                                    % Population percentage that will be replaced

clone_factor = 0.6;                                % Number of clones per indivídual = 0.5*N (population size)

beta = 1;                                          % Mutation constant
sigma_max = 1;                                     % Max sigma constant
mut_const = 2;                                     % Mutation decay constant

sig_thr = 3;                                       % Affinity threshold
stability_trh = 0.01*4;                            % Stability thershold

itMax = 600;                                       % Maximum number of iterations
maxEval = 5e3;                                     % Maximum number of evaluations

min_r = 0;                                         % Minimum limit
max_r = 100;                                       % Maximum limit

% Mutation operator and parameters
mutator_op = @clone_hypermutate;

% Fitness function 
fitness_op = @hump;
fitness_gf = @hump;

% ---------------------------------------------------------------------------------------------------%
% ---------------------------------------------------------------------------------------------------%
% ---------------------------------------------------------------------------------------------------%

% Figures graph
load('hump_parameters');
xaxis = 0:1e-2:100;
surf_val = fitness_gf(xaxis, peaks, radios, shapes, amps); 

% Creating initial population
population = (max_r-min_r)*rand(N, L) + min_r;

% Parameters history
population_hist = zeros(itMax, 1);
fitness_avg_hist = zeros(itMax, 1);
fitness_min_hist = zeros(itMax, 1);
fitness_max_hist = zeros(itMax, 1);

% Evaluation parameters
load('list_fitness_min');
eps = 0.05;
np = zeros(itMax, 1);
total_fit = zeros(itMax, 1);

% Initiating variables
average_fitness = 0;
it = 0;
eval = 0;

while(it < itMax && eval <= maxEval)
  
  % Fitness, average fitness and current population size
  fitness = fitness_op(population, peaks, radios, shapes, amps);
  average_fitness = mean(fitness);
  
  N = size(population,1);

  % Counting number of iterations used
  it = it + 1;
  
  % Filling history
  population_hist(it) = size(population, 1); 
  fitness_avg_hist(it) = mean(fitness);
  fitness_min_hist(it) = min(fitness);
  fitness_max_hist(it) = max(fitness);
  [np(it), total_fit(it)] = minimum_metrics(population, peaks, amps, eps); 
  
  % Cloning and Mutating 
  clones = mutator_op(population, clone_factor, fitness, sigma_max, mut_const, beta, min_r, max_r);

  % Finding best clone for each individual
  fitness = fitness_op(clones, peaks, radios, shapes, amps);

  % Counting number of evaluations used
  eval = eval + size(clones, 1);

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
    population = [population; (max_r-min_r)*rand(ceil(N*pop_fact), L) + min_r];

  end

%   Ploting
  figure(1)
  clf
  plot(xaxis, surf_val)
  grid on;
  hold on
  plot(population, fitness_op(population, peaks, radios, shapes, amps),'*')
  drawnow()

  
end    
    
  


