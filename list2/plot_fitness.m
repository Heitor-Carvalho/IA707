

for i = 1:20

  fitness{i} = load(['fitness_evol' num2str(i)]);
  figure(i)
  plot(0:1:size(fitness{i}(:,1))-1, fitness{i}(:,1),'.r', ... 
       0:1:size(fitness{i}(:,1))-1, fitness{i}(:,2),'.g', ...
       0:1:size(fitness{i}(:,1))-1, fitness{i}(:,3),'.k')

  xlabel('Iteration')
  ylabel('Fitness')
  xlim([0 size(fitness{i}, 1)])
  legend('Best fitness', 'Worst fitness', 'Average fitness', 'location', 'best')
  grid
 
end

