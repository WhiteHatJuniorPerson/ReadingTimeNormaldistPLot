import pandas as pd 
import random as rd 
import statistics as stats 
import plotly.figure_factory as pf 

df = pd.read_csv("medium_data.csv")
ReadingTime = df["reading_time"].tolist()


finallist  = []
def getOneSample():
    sample = []
    for i in range(0,100):
        rp = rd.randint(0,len(ReadingTime)-1)
        sample.append(float(ReadingTime[rp]))
    samplemean = stats.mean(sample)
    finallist.append(samplemean)
for i in range(0,1000):
    getOneSample()
graph  = pf.create_distplot([finallist],["Reading Time Normal"],show_hist=False)
graph.show()