% clear all

addpath([pwd '/..'])
addpath([pwd '/../functions'])
addpath([pwd '/operators'])

% Algorithm parameters
N = 20;                                           % Population size
L = 1;                                            % Parameters length
pop_fact = 0.05;                                  % Population percentage that will be replaced
iterval = 1;                                      % Interval used to add new random individuals

clone_factor = 4/N;                               % Number of clones per indivídual = clone_factor*N (population size)

beta = 1;                                         % Mutation constant
sigma_max = 0.5;                                    % Max sigma constant
mut_const = 5;                                    % Mutation decay constant

itMax = 1000;                                     % Maximum number of iterations
maxEval = 5e3;                                    % Maximum number of evaluations

min_r = 0;                                        % Minimum limit
max_r = 100;                                      % Maximum limit

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
bests_idx = zeros(N, 1);

% Parameters history
fitness_avg_hist = zeros(itMax, 1);
fitness_min_hist = zeros(itMax, 1);
fitness_max_hist = zeros(itMax, 1);

% Evaluation parameters
eps = 0.05;
np = zeros(itMax, 1);
total_fit = zeros(itMax, 1);

% Initiating variables
it = 0;
eval = 0;

while(it < itMax && eval <= maxEval)
    
  fitness = fitness_op(population, peaks, radios, shapes, amps);
  
  % Counting number of iterations used
  it = it + 1;

  % Filling history
  fitness_avg_hist(it) = mean(fitness);
  fitness_min_hist(it) = min(fitness);
  fitness_max_hist(it) = max(fitness);
  [np(it), total_fit(it)] = minimum_metrics(population, peaks, amps, eps); 


  % Cloning and Mutating 
  clones = mutator_op(population, clone_factor, fitness, sigma_max, mut_const, beta, min_r, max_r);
  
  % Finding best clone for each individual
  fitness = fitness_op(clones, peaks, radios, shapes, amps);
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
%   figure(1)
%   clf
%   plot(xaxis, surf_val)
%   grid on;
%   hold on
%   plot(population, fitness_op(population, peaks, radios, shapes, amps),'*')
%   drawnow()
  
end  
  
    
  


