%This plots the data given as x and y, as the first column vs seccond
%column
function mygraph = plotXY(File)
    %asks for axis labels
    Xaxisname = input('What do you want to name x axis: ','s');
    Yaxisname = input('What do you want to name y axis: ','s');
    graphtitle = input('What is your title: ','s');

    %creates and plots the graph
    mygraph = plot(File(:,1),File(:,2));
    xlabel(Xaxisname);
    ylabel(Yaxisname);
    title(graphtitle);
    
end