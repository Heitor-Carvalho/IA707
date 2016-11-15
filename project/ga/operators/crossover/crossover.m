function new_population = crossover_common(population)
    
    n = size(population, 1);
    
    idx = reshape(randperm(n), n/2, 2);
    sons = zeros(n, 2);
    
    for i=1:n/2
        alpha = rand(1);
        sons(2*i-1, :) = alpha*population(idx(1),:) + (1-alpha)*population(idx(2),:);
        sons(2*i, :) = alpha*population(idx(2),:) + (1-alpha)*population(idx(1),:);
    end
    
    new_population = [population; sons];
    
end

