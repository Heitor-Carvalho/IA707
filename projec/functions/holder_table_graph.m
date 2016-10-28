function fitness = holder_table_graph(x, y)
  % Normal range from [-6, 6]
  fitness = abs(sin(x).*cos(y).*exp(abs(1 - sqrt(x.^2 + y.^2)/pi)));  

end