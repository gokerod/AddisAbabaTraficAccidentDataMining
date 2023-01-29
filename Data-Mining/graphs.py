import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

attribs = ["Time",
"Day_of_week",
"Age_band_of_driver",
"Sex_of_driver",
"Driving_experience",
"Types_of_Junction",
"Light_conditions",
"Weather_conditions",
"Type_of_collision",
"Vehicle_movement",
"Cause_of_accident",
"Accident_severity"]

df = pd.read_csv('processedAccidentData.csv')
print(len(df['Time'].unique()))

def graph(line: str):
    y = df[line].value_counts()
    x = df[line].unique()
    
    plt.figure(figsize=(50, 10)) if len(x) > 8 else plt.figure(figsize=(15, 10))  
    plt.bar(x, y, color="lightblue")
    for i in range(len(x)):
        plt.text(x=i, y=y[i], s=y[i], ha='center')
    plt.xlabel(line, labelpad=5)
    plt.ylabel("count")
    plt.title(f"{line} graph")

    # plt.show()
    plt.savefig(f"graphs/test/{line}.png", bbox_inches="tight")
    plt.clf()

for line in attribs:
    # graph(line)
    # print("================================ DONE ================================")
    pass

def corretlation_grapher():
    y = df.query(" Time == ['Afternoon Rush'] ")['Accident_severity'].value_counts()
    x = df["Accident_severity"].unique()
    plt.bar(x, y)
    for i in range(len(x)):
        plt.text(x=i, y=y[i], s=y[i], ha='center')
    plt.xlabel('Accident_severity', labelpad=5)
    plt.ylabel("count")
    plt.title("Accident_severity vs Time graph")
    plt.show()
    # print(y)
    
corretlation_grapher()
