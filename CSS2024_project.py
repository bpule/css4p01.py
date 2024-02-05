# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a movie_dataset script file.
"""
import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt
df = pd.read_csv("movie_dataset.csv", index_col=0)
file = pd.read_csv("movie_dataset.csv")
#print(file.info())
#Filling Nan in revenue (millions) with average revenue
x=df["Revenue (Millions)"].mean()
#print(x)
df["Revenue (Millions)"].fillna(x, inplace=True)
#print(df)
#Filling Nan in Metascore with average metascore

x=df["Metascore"].mean()
df['Metascore'].fillna(int(df['Metascore'].mean()), inplace=True)
#print(df)
"""
Q1:Highest rating_movie= The Dark Knight
"""
rating_sorted_data=df.sort_values(by='Rating',ascending=False)
print(rating_sorted_data)
"""
Q2: Average revenue of all movies=82.952
"""
#total_avg_revenue=df["Revenue (Millions)"].mean()
#print(total_avg_revenue)
"""
Q3:2015-2017 average revenue=68.06402328198025
"""
three_yr_mean=np.mean(df[df["Year"].between(2015,2017)]["Revenue (Millions)"])
#print(three_yr_mean)
"""
Q4: Number of movies released in 2016: 297
"""
df.loc[df["Year"] >= 2016]
Movies_released = df[df['Year'] == '2016']
print(Movies_released)
"""
Q5: Movies directed by Christopher Nolan: 5

Movies by Christopher Nolan=5
"""
movies_by_CN = df.query("Director == 'Christopher Nolan'")
print (movies_by_CN)

"""
Q6:Movies with at least 8 rating: 78
"""
df.loc[df["Rating"] >= 8.0]
"""
Q7:Median range: Christopher Nolan: 8.6
"""
import statistics
CNRating = [8.6, 9, 8.5, 8.8, 8.5]
print("Median of data-set is %s" % (statistics.median(CNRating)))
"""
Q8: Find the year with the highest average rating
"""
total_avg_rating=df["Rating"].mean()
#print(total_avg_rating)
"""
Q9: Percentage increase in movies between 2006 and 2016:575
"""
Movies_in_2006 = df[df['Year'] == 2006].shape[0]
Movies_in_2016 = df[df['Year'] == 2016].shape[0]
Percentage_increase_2006_to_2016 = (Movies_in_2016-Movies_in_2006)/(Movies_in_2006)*100
print(Percentage_increase_2006_to_2016)

"""
Q10: Most common actor in all the movies
"""

"""
Q11: Unique genres
"""
all_genres = df['Genre'].str.split(',').sum
unique_genres = len(set(all_genres))

"""
Q12: Correlation of features
"""
import plotly.express as px
import matplotlib.pyplot as plt
df.loc[df["Year"] >= 2015]
Movies_released_2015 = df[df['Year'] == '2015']
print(Movies_released_2015)
df.loc[df["Year"] >= 2014]
Movies_released_2015 = df[df['Year'] == '2014']
#print(Movies_released_2014)
df.loc[df["Year"] >= 2013]
Movies_released_2015 = df[df['Year'] == '2013']
#print(Movies_released_2013)
#Movies released in 2013=613
#Movies released in 2014=522
#Movies released in 2015=424
#Movies released in 2016=297
x_bar = ["2013","2014", "2015", "2016"]
y_bar = ["613", "522", "424, 297"]
fig = px.bar(x=x_bar, y=y_bar, labels={'x': 'Years of movies released', 'y': 'Number of movies released'}, title='Number of movies released over a 4 year period')
fig.write_html("plot.html")
import webbrowser
webbrowser.open("plot.html")
