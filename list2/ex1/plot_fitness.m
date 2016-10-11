

for i = 1:5

  fitness{i} = load(['fitness_evol' num2str(i)]);
  figure(i)  
  plot(-fitness{i}(:,2),'.r', -fitness{i}(:,1),'.')
  legend('Average distance', 'Smaller distance')
  xlabel('Iteration')
  ylabel('Path distance')
  xlim([0 1500])
  grid
  
  end

