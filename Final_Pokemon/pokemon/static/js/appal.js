var defaultURL = "/catchbytotal";
d3.json(defaultURL).then(function(data) 
{
  var data = [data];
  var layout = 
    { 
        title: "Pokemon Catch Rate Vs. Total Points",
        xaxis: {title: "Catch Rate"},
        yaxis: {title: "Total"}  
    };
 
  Plotly.plot("scatter", data, layout);
});

  Plotly.newPlot('myDiv', data, layout);