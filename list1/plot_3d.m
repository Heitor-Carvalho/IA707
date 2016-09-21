
% Geneting axis
x = linspace(-1, 2, 1e2);
y = linspace(-1, 2, 1e2);

[xgrid, ygrid] = meshgrid(x,y);


f = xgrid.*sin(4*pi*xgrid) - ygrid.*sin(4*pi*ygrid + pi) + 1;

population = zeros(100, 3, 100);
for i = 1:size(population, 3)
    population(:,:,i) = load(['./population', num2str(i-1)]);
end

fitness_adjust = population(:, 1, :).*sin(4*pi*population(:, 1, :)) - population(:, 2, :).*sin(4*pi*population(:, 2, :) + pi) + 1;

for i=1:9:size(population, 3)
    figure(i)
    mesh(xgrid, ygrid, f)
    hold on
    plot3(population(:, 1, i), population(:, 2, i), fitness_adjust(:, :, i), 'd', 'LineWidth', 3)
end
