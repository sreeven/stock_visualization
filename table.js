d3.json("stock.json").then(function(data){
    // var data = []
    // var sp500 = {}


    // for (var i = 0; i < data.length; i++){
    //     var symbol = data[i].Symbol;
    //     var open = data[i].Open;
    //     var close = data[i].Close;
    //     var high = data[i].High;
    //     var low = data[i].Low;

    //     var stock = {
    //         // "Symbol": symbol,
    //         "Open": open,
    //         "Close": close,
    //         "High": high,
    //         "Low": low
    //     }
    //     sp500[symbol] = stock
    // }


    var entry = Object.entries(data)
    
        // // get table references
    const tbody = d3.select("tbody");

    function buildTable(entry) {
    // First, clear out any existing data
    tbody.html("");

    // Next, loop through each object in the data
    // and append a row and cells for each value in the row
    entry.forEach((dataRow) => {
        // Append a row to the table body
        const row = tbody.append("tr");

        // Loop through each field in the dataRow and add
        // each value as a table cell (td)
        Object.values(dataRow).forEach((val) => {
        let cell = row.append("td");
            cell.text(val);
        }
        );
    });
    }

    buildTable(data);

}
)











