// defines a user-defined function (UDF) that transforms a CSV line (a single row of text) into a JSON object.
function transform(line) {
    // Splits the input string (line) into an array of values
    var values = line.split(',');

    // This object will be populated with key-value pairs derived from the CSV data.
    var obj = new Object();

    // Populates the obj object with properties
    obj.rank = values[0];
    obj.name = values[1];
    obj.country = values[2];

    // Converts the JavaScript object (obj) into a JSON-formatted string.
    var jsonString = JSON.stringify(obj);

    return jsonString;
   }