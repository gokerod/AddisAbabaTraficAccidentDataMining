const getEntropy = (a, b, totalInstance) => {
  total = a + b;
  a = a / total;
  b = b / total;
  if (a === 0 || b === 0) return (total / totalInstance) * 1;
  return (total / totalInstance) * (-(a / total) * Math.log2(a) - b * Math.log2(b));
};

const getHighestEntropyAttribute = (accidentData, classAttribute) => {
  totalInstance = accidentData.length;
  var highestEntropy = ["", 0];
  var attributes = Object.keys(accidentData[0]); // Get all attributes of dataset
  attributes = attributes.filter((attribute) => attribute != classAttribute); // Remove the class attribute
  // Get possible types of class attribute
  var classAttributeValues = Array.from(
    new Set(accidentData.map((accident) => accident[classAttribute]))
  );

  // Iterate on each attribute
  attributes.forEach((attribute) => {
    attributeEntropy = 0;
    let types = new Set(accidentData.map((accident) => accident[attribute])); // Get possible types of current attribute

    // Iterate on each type
    types.forEach((type) => {
      // Get all instances whose attribute and type are the current attribute and type
      subset = accidentData.filter((accident) => accident[attribute] === type);

      // Get count of lists whose value is positive form the above subset
      positive = subset.filter(
        (accident) => accident[classAttribute] === classAttributeValues[0]
      ).length;
      // Get count of lists whose value is negative
      negative = subset.length - positive;
      total = subset.length;

      // Get entropy of current type
      entropy = getEntropy(positive, negative, totalInstance);
      console.log(entropy);
      // Add the entropy of the type to its parent attribute entropy
      attributeEntropy += entropy;
    });
    // If the current attribute as larger entropy than the previous, Update the highest entropy
    if (highestEntropy[1] < attributeEntropy) highestEntropy = [attribute, attributeEntropy];
  });

  return highestEntropy;
};
module.exports = getHighestEntropyAttribute;
