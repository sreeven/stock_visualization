var sp500data = []
var symbols = []
var marketcaps = []
var opens = []
var closes = []

d3.json("stock.json").then(function(data){
  for (var i = 0; i < data.length; i++){
    sp500data.push(data[i])

    symbols.push(data[i].Symbol)
    marketcaps.push(data[i].Marketcap)
    opens.push(data[i].Open)
    closes.push(data[i].Close)

  }

  })

  console.log(opens)
  console.log(closes)
  
var trace1 = {
  // x: [1, 2, 3, 4],
  // y: [10, 11, 12, 13],
  x: opens,
  y: closes,
  mode: 'markers',
  // marker: {
  //   size: [40, 60, 80, 100]
  // }
};

var data = [trace1];

var layout = {
  title: 'Marker Size',
  showlegend: false,
  height: 600,
  width: 600,
  xaxis: {range: [0 ,500]},
  yaxis: {range: [0, 200]}
};

Plotly.newPlot('bubble', data, layout);