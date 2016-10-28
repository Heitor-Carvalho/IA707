function fitness = bukin(p)

  fitness = 100*sqrt(abs(p(:, 2) - 0.001*p(:, 1).^2)) + 0.01*abs(p(:, 1)+10);
  
end