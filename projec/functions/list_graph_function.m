function fitness = list_graph_function(x, y)

  fitness = x.*sin(4*pi*x) - y.*sin(4*pi*y + pi) + 1;

end
