function fitness = list_function(p)

  fitness = p(:,1).*sin(4*pi*p(:,1)) - p(:,2).*sin(4*pi*p(:,2) + pi) + 1;
  
end
