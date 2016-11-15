function new_population = tournament_selection(population, fitness, percent)
  [N, L] = size(population);
  tourn_size = floor(N*percent);

  new_population = zeros(N/2, L);
  for i = 1:N/2
    idx = randperm(N, tourn_size);
    [val, best_idx] = max(fitness(idx));
    new_population(i, :) = population(idx(best_idx), :);
  end
 
end