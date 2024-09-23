tiledlayout('flow')
dt=[0.01,0.03];
for i=1:2
    for j=1:2
        nexttile;
        resultshow(dt(j),0.02,i-1);
    end
end