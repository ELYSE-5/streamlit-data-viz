import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#import data
path = 'C:/Users/relys/OneDrive/Bureau/efrei_viz_python/st_app/uber-raw-data-apr14.csv'
df = pd.read_csv(path, delimiter = ',')
df.rename( columns = { 'Lat':'latitude' , 'Lon':'longitude'}, inplace=True)

st.set_page_config(layout ='wide')

st.title ("UBER DATA APRIL 2014")


#date transformation
df['Date/Time'] = df['Date/Time'].map(pd.to_datetime)
df.head()

#functions for finding the day, the week, the hour
def get_weekday(dt):
    return dt.weekday()

def get_dom(dt):
    return dt.day

def get_hour(dt):
    return dt.hour

# applying these functions
df['day'] = df['Date/Time'].map(get_dom)
df['weekday']= df['Date/Time'].map(get_weekday)
df['hour'] = df['Date/Time'].map(get_hour)

# show 

col1,col2= st.columns (2)

map_ = col1.checkbox("Map me")
if map_:
    st.map(df)

head_=col2.checkbox("head of my raw dataframe")
if head_:
    df.head()





"""
#show Fréquence de vente
hist = df[["day", "Lat", "Lon"]].plot.hist(bins = 30, rwidth = 0.8, range=(0.5,30.5), figsize = (30,15), title = "Frequency by DoM - Uber - April 2014")


# functions count_rows
def count_rows(rows):
    return len(rows)

by_date = df.groupby('day').apply(count_rows)


#show
plt.plot(by_date)


#Sort data by date and using bar 

fig, ax = plt.subplots(figsize = (30, 15))
ax.plot(range(1, 31), by_date.sort_values())
plt.xticks(range(1, 31), by_date.sort_values().index)
plt.xlabel('Date of the month')
plt.ylabel('Frequency')
plt.title('Frequency by DoM - Uber - April 2014')   
plt.legend()
st.pyplot(fig)

# Visualise the data by hours 
plt.figure(figsize = (30, 15))
plt.hist(df.hour, bins = 24, range = (0.5, 24))
plt.xlabel('Hour of the day')
plt.ylabel('Frequency')
plt.title('Frequency by Hour - Uber - April 2014')

#Visualise the data by weekday
plt.figure(figsize = (30, 15))
plt.hist(df.weekday, bins = 7, rwidth = 0.8, range = (-.5, 6.5))
plt.xlabel('Day of the week')
plt.ylabel('Frequency')
plt.title('Frequency by Hour - Uber - April 2014')

# using xticks
plt.figure(figsize = (30, 15))
plt.hist(df.weekday, bins = 7, rwidth = 0.8, range = (-.5, 6.5))
plt.xlabel('Day of the week')
plt.ylabel('Frequency')
plt.title('Frequency by Hour - Uber - April 2014')
plt.xticks(np.arange(7), 'Mon Tue Wed Thu Fri Sat Sun'.split())
plt.show()

# Grouping data by week and hour 
df2 = df.groupby(['weekday', 'hour']).apply(count_rows).unstack()
df2.head()
sns.heatmap(df2, linewidths = .5)


# Latitude and longitude 
plt.hist(df['Lat'], bins = 100, range = (40.5, 41))
plt.show()

plt.hist(df['Lon'], bins = 100, range = (-74.1, -73.9))
plt.show()


# Merging Lat and Long histograms
plt.hist(df['Lon'], bins = 100, range = (-74.1, -73.9), color = 'g', alpha = 0.5, label = 'Longitude')
plt.legend(loc = 'best')
plt.twiny()
plt.hist(df['Lat'], bins = 100, range = (40.5, 41), color = 'r', label = 'Latitude')
plt.legend(loc = 'upper left')
plt.show()


# lat and long plot

plt.plot(df['Lat'], ms = 10, color = 'r', label = 'latitude')
plt.plot(df['Lon'], ms = 10, color = 'g', label = 'longitude')
plt.xlim(0, 100)
plt.show()



plt.figure(figsize = (20, 20))
plt.scatter(df.Lat, df.Lon)
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()


plt.figure(figsize = (20, 20))
plt.plot(df.Lon, df.Lat, '.', ms = 2, alpha = .5)
plt.xlim(-74.2, -73.7)
plt.ylim(40.7, 41)
plt.grid()

"""