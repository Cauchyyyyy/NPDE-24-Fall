m=[20,160];
N=[10,100];

tiledlayout('flow');
for i=1:2
    for j=1:2
        nexttile;
        resultshow(m(i),N(j));
    end
end