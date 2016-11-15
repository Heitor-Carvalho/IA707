function fitness = holder_table(p)
  
  fitness = -abs(sin(p(:, 1)).*cos(p(:, 2)).*exp(abs(1 - sqrt(p(:,1).^2 + p(:,2).^2)/pi)));  

end