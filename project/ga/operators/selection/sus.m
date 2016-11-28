function new_population = sus(population, fitness)

  [N, L] = size(population);
  [fitness_sort, idx] = sort(fitness);
  
  % Calculating probability of choose an individual
  norm_fitness =  (fitness_sort - min(fitness_sort));
  norm_fitness = norm_fitness/sum(norm_fitness);
  
  % Normalizing this probability
  roulette = cumsum(norm_fitness);
  dist_selec = 1/(N/2);
  points_selec = rand(1)*dist_selec;

  points = 0:(1/(N/2)):(N/2-1)*(1/(N/2));
  points = 1 - (points_selec + points);

  new_population = zeros(N/2, L);
  for i=1:N/2
    survivor = sum(roulette < points(i)) + 1;
    new_population(i,:) = population(idx(survivor), :);
  end
  

end