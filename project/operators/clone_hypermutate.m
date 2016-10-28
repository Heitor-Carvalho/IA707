function clones = clone_hypermutate(population, clone_factor, fitness, sig_max, beta, mut_const, min_r, max_r)
   
   % Normalizing fitness
   fitness_norm = (fitness - min(fitness))/(max(fitness) - min(fitness)); 
   
   % Creating clones
   clones = repmat(population, ceil(size(population, 1)*clone_factor), 1);
   
   % Generating inverse fitness mutation
   mutation = sig_max*randn(size(clones,1), size(clones,2));
   mutation = repmat((1/beta)*exp(-mut_const*fitness_norm), size(clones,1)/size(fitness_norm,1), size(clones,2)).*mutation;
   
   % Saturating mutation values
   clones = clones + mutation;
   clones(clones < min_r) = min_r;
   clones(clones > max_r) = max_r;
   
   % Adding a copy of the original population
   clones(1:size(population, 1), :) = population(1:size(population, 1),:);

  
end