import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the data
data = pd.read_csv('processedAccidentData.csv')

# Select the relevant columns for the model
#'Time', 'Day_of_week', 'Age_band_of_driver', 'Sex_of_driver', 'Educational_level', 'Vehicle_driver_relation', 'Driving_experience', 'Type_of_vehicle', 'Owner_of_vehicle', 'Service_year_of_vehicle', 'Defect_of_vehicle', 'Area_accident_occured', 'Lanes_or_Medians', 'Road_allignment', 'Types_of_junction', 'Road_surface_type', 'Road_surface_conditions', 'Light_conditions', 'Weather_conditions', 'Type_of_collision', 'Number_of_vehicles_involved', 'Vehicle_movement', 'Pedestrian_movement', 
# X = data[['Driving_experience']]

X = data[['Weather_conditions']]
y = data['Accident_severity']

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.34, random_state=42)

# Create the random forest classifier
clf = RandomForestClassifier()

# Train the model on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Print the accuracy of the model
print("Accuracy:", accuracy_score(y_test, y_pred))

# Create a confusion matrix to visualize the model's performance
conf_mat = confusion_matrix(y_test, y_pred)

# Plot the confusion matrix
plt.figure(figsize=(10,10))
plt.imshow(conf_mat, cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.colorbar()
plt.xticks(range(2), ["Predicted Low", "Predicted High"])
plt.yticks(range(2), ["Actual Low", "Actual High"])
plt.xlabel("Predicted Severity")
plt.ylabel("Actual Severity")
for i in range(2):
    for j in range(2):
        # pass
        plt.text(j, i, conf_mat[i, j], ha="center", va="center", color="red")
plt.show()
