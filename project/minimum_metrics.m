function [np, total_fitness] = minimum_metrics(population, min_locals, min_fit, eps)
  np = 0;
  total_fitness = 0;

  for i = 1:size(min_locals, 1)
      dist = 0;
      for j = 1:size(min_locals, 2)
         dist = dist + (min_locals(i, j) - population(:, j)).^2;
      end
      
      dist = sqrt(dist);
      if(any(dist < eps))
          np = np + 1;
          total_fitness = total_fitness + min_fit(i);
      end
  end
  
end