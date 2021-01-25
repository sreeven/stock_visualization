// d3.json("static/stock.json").then(function(data) {
//     console.log(data)});

// var test = d3.json("stock.json").then(function(data){
//     for (var i = 0; i < 5; i++){
//         console.log(data.i.Symbol);
//     }
// })



// var data = d3.json("http://localhost:8000");
// console.log(data);

//     var startDate = data.dataset.start_date;
//     var endDate = data.dataset.end_date;
//     var dates = unpack(data.dataset.data, 0);
//     var closingPrices = unpack(data.dataset.data, 4);

//     var trace1 = {
//       type: "scatter",
//       mode: "lines",
//       name: name,
//       x: dates,
//       y: closingPrices,
//       line: {
//         color: "#17BECF"
//       }
//     };

//     var data = [trace1];

//     var layout = {
//       title: ${stock} closing prices,
//       xaxis: {
//         range: [startDate, endDate],
//         type: "date"
//       },
//       yaxis: {
//         autorange: true,
//         type: "linear"
//       }
//     };

//     Plotly.newPlot("plot", data, layout);

//   });
// }

// buildPlot();