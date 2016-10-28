function fitness = drop_wave_graph(x, y)

  fitness = (1+cos(12*sqrt(x.^2 + y.^2)))./(0.5*(x.^2 + y.^2) + 2);  

end