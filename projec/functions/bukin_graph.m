function fitness = bukin_graph(x, y)

  % Normal range from [-15, 5]x[-3, 3]
  fitness = 100*sqrt(abs(y - 0.001*x.^2)) + 0.01*abs(x+10);
  
end