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
purchasing_analysis = pd.DataFrame({"Purchasing Analysis (Total)":[unique_items][average_price][number_of_purchases][total_revenue]})
purchasing_analysis_(total)

# format in currency style
summary_df.style.format({'Average Price':"${:,.2f}",'Total Revenue': '${:,.2f}'})

