function fitness = drop_wave(p)

% Normal range from [-2, 2]
  fitness = (1+cos(12*sqrt(p(:,1).^2 + p(:,2).^2)))./(0.5*(p(:,1).^2 + p(:,2).^2) + 2);  

end