# import dependencies
import pandas as pd
import numpy as np
import json
import os
import csv

# raw data file
file_to_load = "Resources/purchase_data.csv"

# read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)

# use the length of list of screen names "SN" for total players.
total_players = len(purchase_data["SN"].value_counts())

# create a data frame with total players named player count
player_count = pd.DataFrame({"Total Players":[total_players]})
player_count

# calculations for unique items, average price, number of purchases, and total revenue
number_of_unique_items = len((purchase_data["Item ID"]).unique())
average_price = (purchase_data["Price"]).mean()
number_of_purchases = (purchase_data["Purchase ID"]).count()
total_revenue = (purchase_data["Price"]).sum()

# create a data frame for analysis named Purchasing Analysis (Total)
summary_df = pd.DataFrame({"Number of Unique Items":[number_of_unique_items],
                           "Average Price":[average_price], 
                           "Number of Purchases": [number_of_purchases], 
                           "Total Revenue": [total_revenue]})

# format in currency style
summary_df.style.format({'Average Price':"${:,.2f}",
                         'Total Revenue': '${:,.2f}'})

# group purchase data by gender
gender_stats = purchase_data.groupby("Gender")

# count total of screen names "SN" by gender
total_count_gender = gender_stats.nunique()["SN"]

# total count by gender and divivde by total players 
percentage_of_players = total_count_gender / total_players * 100

# create data frame with obtained values
gender_demographics = pd.DataFrame({"Percentage of Players": percentage_of_players, "Total Count": total_count_gender})

# format the data frame with no index name in the corner
gender_demographics.index.name = None

# format the values sorted by total count in descending order with two decimal places for the percentage
gender_demographics.sort_values(["Total Count"], ascending = False).style.format({"Percentage of Players":"{:.2f}"})
                                                                                  