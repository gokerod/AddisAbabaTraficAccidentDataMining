const csvtojson = require("csvtojson");
const fs = require("fs");

csvtojson()
  .fromFile("./data/DM project data.csv")
  .then((data) => {
    accidentData = JSON.stringify(data);
    fs.writeFile("data/accidentData.json", accidentData, (err) => {
      if (err) throw err;
      console.log("File write successful");
    });
  });
