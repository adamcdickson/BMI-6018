# -*- coding: utf-8 -*-

#%% Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%% Importing Data
flights_data = pd.read_csv('flights.csv')
flights_data.head(10)
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()
#%% Pandas Data Filtering/Sorting Question Answering
#use flights_data

#Question 1 How many flights were there from JFK to SLC? Int
q_1 = flights_data[
    (flights_data["origin"] == "JFK") &
    (flights_data["dest"] == "SLC")
].shape[0]

print(q_1)

#Question 2 How many airlines fly to SLC? Should be int
q_2 = flights_data.loc[
    flights_data["dest"] == "SLC", "carrier"
].nunique()

print(q_2)

#Question 3 What is the average arrival delay for flights to RDU? float
q_3 = flights_data.loc[
    flights_data["dest"] == "RDU", "arr_delay"
].mean()

print(q_3)

#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
q_4 = flights_data.loc[
    flights_data["dest"] == "SEA", "origin"
].isin(["LGA", "JFK"]).mean()

print(q_4)

#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
flights_data["date"] = (
    flights_data["year"].astype(str) + "/" +
    flights_data["month"].astype(str) + "/" +
    flights_data["day"].astype(str)
)
average_dep_delay = flights_data.groupby(
    "date", as_index=False
)["dep_delay"].mean()

q_5 = average_dep_delay.loc[
    [average_dep_delay["dep_delay"].idxmax()]
].reset_index(drop=True)

print(q_5)

#Question 6 Which date has the largest average arrival delay? pd slice with date and float
average_arr_delay = flights_data.groupby(
    "date", as_index=False
)["arr_delay"].mean()

q_6 = average_arr_delay.loc[
    [average_arr_delay["arr_delay"].idxmax()]
].reset_index(drop=True)

print(q_6)

#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
nyc_flights = flights_data[
    (flights_data["origin"].isin(["LGA", "JFK"])) &
    (flights_data["year"] == 2013)
].copy()

nyc_flights["speed"] = (
    nyc_flights["distance"] / nyc_flights["air_time"]
)

q_7 = nyc_flights.loc[
    [nyc_flights["speed"].idxmax()],
    ["tailnum", "speed"]
].reset_index(drop=True)

print(q_7)

#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
q_8 = weather_data_pd.fillna(0)

weather_data_np = q_8.to_numpy()

#%% Numpy Data Filtering/Sorting Question Answering
#Use weather_data_np
#Question 9 How many observations were made in Feburary? Int
february_weather = weather_data_np[
    weather_data_np[:, 3] == 2
]

q_9 = len(february_weather)

print(q_9)

#Question 10 What was the mean for humidity in February? Float
q_10 = np.mean(
    february_weather[:, 8].astype(float)
)

print(q_10)

#Question 11 What was the std for humidity in February? Float
q_11 = np.std(
    february_weather[:, 8].astype(float)
)

print(q_11)
