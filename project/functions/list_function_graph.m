function [gridx, gridy, surf_val] = list_function_graph(min, max, plot_function)

  grid = min:0.04:max;
  [gridx gridy] = meshgrid(grid,grid);
  surf_val = plot_function(gridx, gridy);
  
end