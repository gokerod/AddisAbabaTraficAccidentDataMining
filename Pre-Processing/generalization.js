const accidentData = require("./preProcessing");

attributes = Object.keys(accidentData[0]);

attributes.forEach((attribute) => {
  accidentData.forEach((accident) => {
    switch (accident[attribute]) {
      // Education level
      case "Above high school":
      case "Junior high school":
      case "High school":
        accident[attribute] = "High school";
        break;
      // Driving_experience
      case "1-2yr":
      case "2-5yr":
        accident[attribute] = "1-5 yr";
        break;
      // Type_of_vehicle
      case "Automobile":
      case "Stationwagen":
        accident[attribute] = "Auto";
        break;
      case "Taxi":
      case "Public (12 seats)":
        accident[attribute] = "Public 1";
        break;
      case "Pick up upto 10Q":
      case "Lorry (11?40Q)":
        accident[attribute] = "Dry 1";
        break;
      case "Lorry (41?100Q)":
      case "Long lorry":
      case "Turbo":
        accident[attribute] = "Dry 2";
        break;
      case "Bicycle":
      case "Ridden horse":
        accident[attribute] = "unlicensed";
      // Lanes_or_Medians
      case "Undivided Two way":
      case "Double carriageway (median)":
      case "Two-way (divided with broken lines road marking)Two-way (divided with broken lines road marking)":
      case "Two-way (divided with solid lines road marking)":
        accident[attribute] = "Two way";
        break;
      //  Road_surface_type
      case "Asphalt roads":
      case "Asphalt roads with some distress":
        accident[attribute] = "Asphalt";
        break;
      case "Earth roads":
      case "Gravel roads":
        accident[accident] = "Non-Asphalt";
        break;
      // Weather_conditions
      case "Raining and Windy":
        accident[attribute] = "Raining";
        break;
      //  Pedestrian_movement
      case "Crossing from driver's nearside":
      case "In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing)":
      case "In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing) - masked by parked or statioNot a Pedestrianry vehicle":
      case "Crossing from nearside - masked by parked or statioNot a Pedestrianry vehicle":
      case "Crossing from offside - masked by  parked or statioNot a Pedestrianry vehicle":
      case "Walking along in carriageway, back to traffic":
      case "Walking along in carriageway, facing traffic":
        accident[attribute] = "Pedestrian";
        break;
      case "Unknown or other":
        accident[attribute] = "Unknown";
        break;
      // Cause_of_accident
      case "Changing lane to the left":
      case "Changing lane to the right":
        accident[attribute] = "Changing lane";
        break;
      case "Overspeed":
      case "Driving at high speed":
        accident[attribute] = "Driving at high speed";
        break;
    }
  });
});

// Enumeration

var map = new Map();
var obj = {};
attributes.forEach((attribute) => {
  types = Array.from(new Set(accidentData.map((accident) => accident[attribute])));
  types.forEach((type, index) => {
    map.set(type, index);
  });
  obj[attribute] = Object.fromEntries(map);
});

console.log(obj["Age_band_of_driver"]);
attributes = attributes.filter((attribute) => attribute == "Age_band_of_driver");
attributes.forEach((attribute) => {
  accidentData.forEach((accident) => {
    accident[attribute] = map.get(accident[attribute]);
  });
});

module.exports = accidentData;
