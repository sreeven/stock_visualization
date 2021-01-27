d3.json("stock.json").then(function(data){
    var marketCaps = {};
    var divYields = {};
    // var communicationServices = {};
    // var consumerDiscretionary = {};
    // var consumerStaples = {};
    // var energy = {};
    // var financials = {};
    // var healthCare = {};
    // var industrials = {};
    // var informationTechnology = {};
    // var materials = {};
    // var realEstate = {};
    // var utilities = {};




    for (var i = 0; i < data.length; i++){
        // var sector  = data[i].Sector;
        // var symbol = data[i].Symbol;
        // var marketCap = data[i].marketCap;

        // if (sector === "Communication Services"){
        //     communicationServices[symbol] = marketCap;
        // }
        // if (sector === "Consumer Discretionary"){
        //     consumerDiscretionary[symbol] = marketCap;
        // }
        // if (sector === "Consumer Staples"){
        //     consumerStaples[symbol] = marketCap;
        // }
        // if (sector === "Energy"){
        //     energy[symbol] = marketCap;
        // }
        // if (sector === "Financials"){
        //     financials[symbol] = marketCap;
        // }
        // if (sector === "Health Care"){
        //     healthCare[symbol] = marketCap;
        // }
        // if (sector === "Industrials"){
        //     industrials[symbol] = marketCap;
        // }
        // if (sector === "Information Technology"){
        //     informationTechnology[symbol] = marketCap;
        // }
        // if (sector === "Materials"){
        //     materials[symbol] = marketCap;
        // }
        // if (sector === "Real Estate"){
        //     realEstate[symbol] = marketCap;
        // }
        // if (sector === "Utilities"){
        //     utilities[symbol] = marketCap;
        // }



        // market cap per sector
        var sector = data[i].Sector;
        var marketCap = data[i].marketCap;
        var divYield = data[i].dividendYield;
        

        if (sector in marketCaps){
            marketCaps[sector] += marketCap;
            divYields[sector] += divYield;

        }
        else {
            marketCaps[sector] = marketCap;
            divYields[sector] = divYield;
        }




        

    }

    // console.log(marketCaps);
    var xTickers = Object.keys(marketCaps);
    var yCaps = Object.values(marketCaps)
    var max = Math.max(yCaps)

    // console.log(yCaps);

    
    // console.log(testCap);
    var trace1 = {
        x: xTickers,
        y: yCaps,
        xaxis: {
            title: "Sector"
        },
        yaxis: {
            title: "Market Cap"
        },

        type: 'bar',

      };
      
      var data = [trace1];
      
      var layout = {
        title: "Market Cap by Sector",
        showlegend: false,
        height: 600,
        width: 600,
        font: {
            family: 'Arial, monospace,',
            size: 14
        },
        yaxis: {range: [0, max]}
      };
      
      Plotly.newPlot('bar', data, layout);





          //   FOR THE PIE CHART

        var pieLabels = Object.keys(divYields);
        var pieValues = Object.values(divYields)

        // new Chart(ctx, {
        //     data: pieValues,
        //     type: 'polarArea',
        //     options: pieLabels
        // });


        var ctx = document.getElementById('myChart');


        data = {
            datasets: [{
                backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#ff6384","#36a2eb","#cc65fe","#ffce56","#f7fcb9", "#addd8e"],
                data: pieValues
            }],

            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: pieLabels,
            // options: {
            //     legend:false,
            //     maintainAspectRatio: false,

            // }

        };

        var myPieChart = new Chart(ctx, {
            type: "polarArea",
            // ctx.canvas.width = 60;
            // ctx.canvas.height = 60;
            data: data,
            options: {
                title: {
                display: true, 
                fontSize: 18,
                padding: 40,
                text: "Dividend Yield per Sector"},

                maintainAspectRatio: false,
                responsive: true,
                legend: {
                    display: true
                },
                
            }
        });


    });

