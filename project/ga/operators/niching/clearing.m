function fitness = clearing(population, fitness, dist_lim)
  
  [N, L] = size(population);
  
  [fitness_ord, sort_idx] = sort(fitness, 'descend');
  search_idx = sort_idx;
  while(~isempty(search_idx))
    pop_dist = 0;
    for i = 1:L
      pop_dist = pop_dist + (population(search_idx(1), i) - population(search_idx, i)).^ 2; 
    end
    pop_dist = sqrt(pop_dist);
    sharing_idx = pop_dist <= dist_lim;
    sharing_idx(1) = 0;

    fitness(search_idx(sharing_idx)) = -99;

    sharing_idx(1) = 1;
    search_idx(sharing_idx) = []; 
  end
  
end 