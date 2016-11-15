function new_population = mutation(population, max_sig, c, t, min_r, max_r)

  [n, L] = size(population);

  new_population = population + max_sig*randn(n,L).*exp(-c*t);

  new_population(new_population < min_r) = min_r;
  new_population(new_population > max_r) = max_r;
   

end
