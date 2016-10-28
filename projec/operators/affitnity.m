function dist = affinity(population, idx)

  dist = zeros(size(population, 1), 1);
  for i = 1:size(population, 2)
    dist = dist + (population(idx, i) - population(:, i)).^2;
  end
  dist = sqrt(dist);

end