function fitness = hump(population, peaks, radios, shapes, amps)
 
 fitness = zeros(size(population, 1), 1);
 for i=1:numel(population)
    dist = abs(population(i) - peaks);
    idx = dist < radios;
    if(any(idx))
        fitness(i) = amps(idx)*(1 - (dist(idx)/radios(idx))^shapes(idx));
    else
        fitness(i) = 0;
    end
  end

end