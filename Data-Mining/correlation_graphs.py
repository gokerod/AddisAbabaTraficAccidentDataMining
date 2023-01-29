import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
# import decisionTree as dt

df = pd.read_csv('processedAccidentData.csv')

# attributes enumeration
attribs = {"Time": {
                'Afternoon Rush': 0, 'Morning Rush': 3
                },
           "Age_band_of_driver": {
               'Under 18': 2, 'Over 51': 3
               },
           "Types_of_Junction": {
               'No junction': 0, 'Y Shape': 1, 'Crossing':2, 'O Shape': 3
               }, 
           "Light_conditions": {
               'Daylight': 0, 'Darkness - lights lit': 1
               }, 
           "Weather_conditions": {
               'Normal': 0, 'Raining': 1
               }
           }

# attribute labels 
atrib_labels = ["Time"
,"Age_band_of_driver"
,"Types_of_Junction"
,"Light_conditions"
,"Weather_conditions"
,"Accident_severity"]

features = ['Time', 'Day_of_week', 'Age_band_of_driver', 'Sex_of_driver',
       'Educational_level', 'Vehicle_driver_relation', 'Driving_experience',
       'Type_of_vehicle', 'Owner_of_vehicle', 'Lanes_or_Medians',
       'Road_allignment', 'Types_of_Junction', 'Road_surface_type',
       'Road_surface_conditions', 'Light_conditions', 'Weather_conditions',
       'Type_of_collision', 'Number_of_vehicles_involved', 'Vehicle_movement',
       'Pedestrian_movement', 'Cause_of_accident', 'Accident_severity']

def atrib_instance_grabber(attrib):
    # print(attribs[attrib])
    return attribs[attrib]

#correlation to selected features shown by bargraphs
#features chossen for reporting purposes
def corretlation_grapher(att):
    instance = atrib_instance_grabber(att)
    print("##", instance)
    
    for j in instance:
        print(">>", instance[j])
        try:
            y = df.query(f" {att} == [{instance[j]}] ")['Accident_severity'].value_counts()
        except Exception:
            y = 0    
        print(">>>", y)
        x = df["Accident_severity"].unique()
        plt.bar(x, y, color="lightblue")
        for i in range(len(x)):
            plt.text(x=i, y=y[i], s=y[i], ha='center')
        plt.xlabel('Accident_severity', labelpad=5)
        plt.ylabel("count")
        plt.title(f"Accident_severity against {j} graph")
        # plt.show()
        plt.savefig(f"graphs/correlation/bargraphs/Accident_severity against {j}.png", bbox_inches="tight")
        plt.clf()

# scatter plot of data
def scatter_plotter(atrib: str):
    # basically useless, all scatter plots are on the same line
    plt.figure(figsize=(10, 10))
    scatter = sns.scatterplot(x=atrib, y='Accident_severity', data=df)
    scatter.set_title(f"Accident_severity vs {atrib}")
    scatter.set_xlabel(atrib)
    
    # plt.show()
    plt.savefig(f"graphs/scatterplot/Accident_severity against {atrib}.png", bbox_inches="tight")
    plt.clf()


#correlation between features by heatmap
def correlation_heatmap(atrib: str):
    corr = df.corr('pearson')
    print(corr)
    plt.figure(figsize=(20, 10))
    heat = sns.heatmap(corr, xticklabels=atrib,
                yticklabels=atrib)
    heat.set_title(f"Accident_severity correlation matrix")
    
    # plt.show()
    plt.savefig("graphs/correlation/heatmap/Accident_severity heatmap.png", bbox_inches="tight")
    plt.clf()

# easy_correlation()

# runner
for feat in atrib_labels:
    # enumerate features
    # df = dt.mapper()
    
    # corretlation_grapher(feat)
    
    # scatter_plotter(feat)
    
    # correlate(feat)
    pass

# heatmap uses all columns to represent correlation
# df = dt.mapper()
correlation_heatmap(features)

# print(df.columns)