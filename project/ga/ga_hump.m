% clear all

addpath([pwd '/../'])
addpath([pwd '/../functions'])
addpath([pwd '/operators/crossover'])
addpath([pwd '/operators/mutation'])
addpath([pwd '/operators/selection'])
addpath([pwd '/operators/niching'])

% Algorithm parameters
N = 20;                                        % Population size                                         
L = 1;                                         % Parameters length

max_sig = 15;                                  % Max sigma constant
mut_const = 0.25;                              % Mutation decay constant

d = 3;                                         % Affinity threshold

itMax = 600;                                   % Maximum number of iterations
maxEval = 5e3;                                 % Maximum number of evaluations

min_r = 0;                                     % Minimum limit
max_r = 100;                                   % Maximum limit

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
new_population = (max_r-min_r)*rand(2*N, L) + min_r;

% Parameters history
fitness_avg_hist = zeros(1, itMax);
fitness_min_hist = zeros(1, itMax);
fitness_max_hist = zeros(1, itMax);

% Evaluation parameters
eps = 0.05;
np = zeros(itMax, 1);
total_fit = zeros(itMax, 1);

% Initiating variables
it = 0;
eval = 0;

while(it < itMax && eval <= maxEval)

  % Fitness, average fitness
  fitness = fitness_op(new_population, peaks, radios, shapes, amps);
  [best_val, best_idx] = sort(fitness);
  best = new_population(best_idx(end), :);
  
  % Counting number of iterations used
  it = it + 1;
  eval = eval + size(new_population, 1);

  % Filling history
  fitness_avg_hist(it) = mean(fitness);
  fitness_min_hist(it) = min(fitness);
  fitness_max_hist(it) = max(fitness);

  fitness = clearing(new_population, fitness, d);  

  population = sus(new_population, fitness);

  [np(it), total_fit(it)] = minimum_metrics(population, peaks, amps, eps); 

  % Ploting
  figure(1)
  clf
  plot(xaxis, surf_val)
  grid on;
  hold on
  plot(population, fitness_op(population, peaks, radios, shapes, amps),'*')
  drawnow()

  new_population = crossover(population);
  new_population = mutation(new_population, max_sig, mut_const, it, min_r, max_r);

  new_population(1:1, :) = best;

end 