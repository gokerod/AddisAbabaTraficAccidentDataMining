const fs = require("fs");

// Read the json from file
try {
  var accidentData = fs.readFileSync("./data/accidentData.json", "utf-8");
  accidentData = JSON.parse(accidentData);
} catch (err) {
  throw err;
}

//   Check of Duplicates (There are none)
accidentValues = Object.values(accidentData);
accidentDataSet = new Set(accidentValues);

accidentData.map((accident, index) => {
  for (let key in accident) {
    //    Replace missed values with Unknown
    if (
      accident[key] == "" ||
      accident[key] == "other" ||
      accident[key] == "Other" ||
      accident[key] == "unknown"
    )
      accident[key] = "Unknown";

    // Replace Fatal Injury with Serious Injury for generalization
    if (key == "Accident_severity" && accident[key] == "Fatal injury") {
      accident[key] = "Serious Injury";
    }
  }

  //   Remove rows if Accident_Severity is Unknown (There are none)
  if (accident.Accident_Severity == "Unknown") accidentData.splice(index, 1);

  //   Discretization for Time
  var time = accident.Time;
  if (time.length < 8) time = 0 + time;
  if (time >= "06:00:00" && time <= "09:00:00") accident.Time = "Morning Rush";
  else if (time > "09:00:00" && time < "17:00:00") accident.Time = "Day Time";
  else if (time >= "17:00:00" && time <= "19:00:00") accident.Time = "Afternoon Rush";
  else accident.Time = "Night Time";

  // Delete casualties as they are not relevant
  delete accident.Casualty_class;
  delete accident.Sex_of_casualty;
  delete accident.Age_band_of_casualty;
  delete accident.Casualty_severity;
  delete accident.Number_of_casualties;
  delete accident.Age_band_of_casualty;

  // Remove attributes with more than 20% Unknown count
  delete accident.Service_year_of_vehicle;
  delete accident.Defect_of_vehicle;
  delete accident.Area_accident_occured;
  delete accident.Work_of_casuality;
  delete accident.Fitness_of_casuality;
});

// Get unknown count per attribute
attributes = Object.keys(accidentData[0]);
map = new Map();
attributes.forEach((attribute) => {
  unknownCount = accidentData.filter((accident) => accident[attribute] == "Unknown").length;
  map.set(attribute, unknownCount);
});
attributeUnknownCount = Array.from(map);
attributeUnknownCount.sort((a, b) => b[1] - a[1]);

// Get unknown count per instance
instanceUnknownCount = [];
accidentData.forEach((accident, index) => {
  var count = 0;
  attributes.forEach((attribute) => {
    if (accident[attribute] === "Unknown") count++;
  });
  instanceUnknownCount.push([index, count]);
});

// Get indexes of instance whose unknown count is greater than 2
instanceUnknownCount = instanceUnknownCount.filter((instance) => instance[1] > 2);
indexOfInstancesToDelete = instanceUnknownCount.map((instance) => instance[0]);

// delete instances whose unknown count is greater or equal to 5
indexOfInstancesToDelete.forEach((index) => accidentData.splice(index, 1));

// console.log(new Set(accidentData.map((accident) => accident["Educational_level"])));
module.exports = accidentData;
