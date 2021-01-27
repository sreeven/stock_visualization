d3.json("stock.json").then(function(data){


    var entry = Object.entries(data)
    
    const tbody = d3.select("tbody");

    function buildTable(entry) {
    tbody.html("");


    entry.forEach((dataRow) => {
        const row = tbody.append("tr");

        Object.values(dataRow).forEach((val) => {
        let cell = row.append("td");
            cell.text(val);
        }
        );
    });
    }

    buildTable(data);
    function handleClick() {

        const ticker = d3.select("#stock-to-filter").property("value");
        let filteredData = tableData;
      
    
        if (ticker) {
    
          filteredData = filteredData.filter(stock => stock.Symbol === ticker);
        }
    
        buildTable(filteredData);
      }
      d3.selectAll("#filter-btn").on("click", handleClick);



})
