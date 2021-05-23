import random ,statistics 
import plotly.express as ps
import plotly.figure_factory as ff
import pandas as pd
import statistics as s

df=pd.read_csv("109data.csv")
data=df["reading"].tolist()

rList=[]
for i in range(0,100):
    r=random.randint(0,len(data)-1)
    reading =data[r]
     
    rList.append(reading)


mean=sum(rList)/len(rList)
sdev=s.stdev(rList)
median=s.median(rList)
mode=s.mode(rList)
#percentage=s.percentage(rList)
print(mean,sdev,median,mode)
#in a data set if mean median and mode are all equal that means it follows normal distribution 
f=ff.create_distplot([rList],['reading'],show_hist=False)
f.show()

