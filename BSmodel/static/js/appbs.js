// Plot the default route once the page loads
var defaultURL = "/type_total";
d3.json(defaultURL).then(function(data) {
  var data = [data];
  var layout = { margin: { t: 30, b: 100 } 
    // title: "title_label",
    // xaxis: {title: "x_label"},
    // yaxis: {title: "y_label"}
  };
  Plotly.plot("bar", data, layout);
});

// Update the plot with new data
function updatePlotly(newdata) {
  Plotly.restyle("x", [newdata.x]);
  Plotly.restyle( "y", [newdata.y]);
}

// Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  d3.json(`/${route}`).then(function(data) {
    console.log("newdata", data);
    updatePlotly(data);
  });
}


