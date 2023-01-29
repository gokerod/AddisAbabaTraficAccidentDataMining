const csvtojson = require("csvtojson");
const json2csv = require("json2csv").parse;
const fs = require("fs");
const accidentData = require("./generalization");

const csv = json2csv(accidentData);
fs.writeFileSync("./data/processedAccidentData.csv", csv);

module.exports = json2csv;
