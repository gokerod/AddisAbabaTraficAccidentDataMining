import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('processedAccidentData.csv')
df.squeeze(axis=0)
print(type(df))
# ne = df['Accident_severity'].squeeze()
# print(type(ne))

attribs = ["Time", "Age_band_of_driver", "Types_of_Junction", "Light_conditions", "Weather_conditions", "Accident_severity"]


# def mapper():
#     Time = {'Afternoon Rush': 0, 'Night Time': 1, 'Day Time': 2, 'Morning Rush': 3}
#     Age_band_of_driver = {'18-30': 0, '31-50': 1, 'Under 18': 2, 'Over 51': 3, 'Unknown': 4}
#     Types_of_Junction = {'No junction':0, 'Y Shape': 1, 'Crossing':2, 'O Shape': 3, 'Unknown': 4, 'T Shape': 5, 'X Shape': 6}
#     Light_conditions = {'Daylight': 0, 'Darkness - lights lit': 1, 'Darkness - no lighting': 2, 'Darkness - lights unlit': 3}
#     Weather_conditions = {'Normal': 0, 'Raining': 1, 'Raining and Windy': 2, 'Cloudy': 3, 'Unknown': 4, 'Windy': 5, 'Snow': 6, 'Fog or mist': 7}
#     Accident_severity = {'Slight Injury': 0, 'Serious Injury': 1}
    
#     df['Time'] = df['Time'].map(Time)
#     df['Age_band_of_driver'] = df['Age_band_of_driver'].map(Age_band_of_driver)
#     df['Types_of_Junction'] = df['Types_of_Junction'].map(Types_of_Junction)
#     df['Light_conditions'] = df['Light_conditions'].map(Light_conditions)
#     df['Weather_conditions'] = df['Weather_conditions'].map(Weather_conditions)
#     df['Accident_severity'] = df['Accident_severity'].map(Accident_severity)
#     return df

# df = mapper()
# print(df.to_string())

x = df[attribs]
y = df['Accident_severity']

print(x)
print(y)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(x, y)

tree.plot_tree(dtree, feature_names=attribs)
# plt.savefig('graphs/decision_trees/decision_tree.png')
plt.show()