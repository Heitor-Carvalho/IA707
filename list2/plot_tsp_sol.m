coor = load('cities.txt')
sol = load('best_sol')

plot([coor(sol(1:end-1)+1, 1); coor(sol(1)+1, 1)], 
     [coor(sol(1:end-1)+1, 2); coor(sol(1)+1, 2)])
