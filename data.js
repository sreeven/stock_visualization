
    
function buildStockData(stock) {
    d3.json("stock.json").then((data) => {
        var stockData = data.stockData;
        var resultArray = stockData.filter(stockObj => stockObj,id == sample);
        var result = resultArray[0];
        var PANEl = d3.select("#stock-data");

        PANEl.html("");

        Object.entries(result).forEach(([key, value]) => {
            PANEL.append("h6").text(`${key.toUpperCase()}: ${value}`);
        });    
})

buildStockData();
      
function buildCharts(sample) {
    d3.json("stock.json").then((data) => {
        var sectors = data.Sector;
        var resultArray = sectors.filter(stockObj => stockObj.id == stock);
        var result = resultArray[0];
        var marketcap = result.marketCap;
        var sector = result.Sector;
        // var otu_ids = result.otu_ids;
        // var otu_labels = result.otu_labels;
        // var sample_values = result.sample_values;   
buildCharts(data);
         
// bubble chart 
var bubbleLayout = {
    title: "Bacteria Cultures Per Sample",
    margin: { t: 0 },
    hovermode: "closest",
    xaxis: { title: "Sector" },
    margin: { t: 30}
  };
  var bubbleData = [
    {
      x: sector,
      y: marketcap,
      //text: otu_labels,
      mode: "markers",
      marker: {
        size: sample_values,
        color: sector,
        colorscale: "Earth"
      }
    }
  ];

Plotly.newPlot("bubble", bubbleData, bubbleLayout);



// print("===========================")
    })}