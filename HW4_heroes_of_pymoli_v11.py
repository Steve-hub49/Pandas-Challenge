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

# PLAYER COUNT
# use the length of list of screen names "SN" for total players.
total_players = len(purchase_data["SN"].value_counts())

# create a data frame with total players named player count
player_count = pd.DataFrame({"Total Players":[total_players]})
player_count

# PURCHASING ANALYSIS (TOTAL)
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

# GENDER DEMOGRAPHICS
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

# PURCHASING ANALYSIS (GENDER)
# count total purchases by gender 
purchase_count = gender_stats["Purchase ID"].count()

# average purchase prices by gender
avg_purchase_price = gender_stats["Price"].mean()

# average purchase total by gender 
avg_purchase_total = gender_stats["Price"].sum()

# average purchase total by gender divivded by purchase count by unique shoppers
avg_purchase_per_person = avg_purchase_total/total_count_gender

# create data frame with obtained values 
gender_demographics = pd.DataFrame({"Purchase Count": purchase_count, 
                                    "Average Purchase Price": avg_purchase_price,
                                    "Average Purchase Value":avg_purchase_total,
                                    "Avg Purchase Total per Person": avg_purchase_per_person})

# provide index in top left as "Gender"
gender_demographics.index.name = "Gender"

# format with currency style
gender_demographics.style.format({"Average Purchase Value":"${:,.2f}",
                                  "Average Purchase Price":"${:,.2f}",
                                  "Avg Purchase Total per Person":"${:,.2f}"})

# AGE DEMOGRAPHICS
# establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

# segment and sort age values into bins established above
purchase_data["Age Group"] = pd.cut(purchase_data["Age"],age_bins, labels=group_names)
purchase_data

# create new data frame with the added "Age Group" and group it
age_grouped = purchase_data.groupby("Age Group")

# count total players by age category
total_count_age = age_grouped["SN"].nunique()

# calculate percentages by age category 
percentage_by_age = (total_count_age/total_players) * 100

# create data frame with obtained values
age_demographics = pd.DataFrame({"Percentage of Players": percentage_by_age, "Total Count": total_count_age})

# format the data frame with no index name in the corner
age_demographics.index.name = None

# format percentage with two decimal places 
age_demographics.style.format({"Percentage of Players":"{:,.2f}"})

# PURCHASING ANALYSIS BY AGE
# Count purchases by age group
purchase_count_age = age_grouped["Purchase ID"].count()

# Obtain average purchase price by age group 
avg_purchase_price_age = age_grouped["Price"].mean()

# Calculate total purchase value by age group 
total_purchase_value = age_grouped["Price"].sum()

# Calculate the average purchase per person in the age group 
avg_purchase_per_person_age = total_purchase_value/total_count_age

# Create data frame with obtained values
age_demographics = pd.DataFrame({"Purchase Count": purchase_count_age,
                                 "Average Purchase Price": avg_purchase_price_age,
                                 "Total Purchase Value":total_purchase_value,
                                 "Average Purchase Total per Person": avg_purchase_per_person_age})

# Format the data frame with no index name in the corner
age_demographics.index.name = None

# Format with currency style
age_demographics.style.format({"Average Purchase Price":"${:,.2f}",
                               "Total Purchase Value":"${:,.2f}",
                               "Average Purchase Total per Person":"${:,.2f}"})

# TOP SPENDERS
# Group purchase data by screen names
spender_stats = purchase_data.groupby("SN")

# Count the total purchases by name
purchase_count_spender = spender_stats["Purchase ID"].count()

# Calculate the average purchase by name 
avg_purchase_price_spender = spender_stats["Price"].mean()

# Calculate purchase total 
purchase_total_spender = spender_stats["Price"].sum()

# Create data frame with obtained values
top_spenders = pd.DataFrame({"Purchase Count": purchase_count_spender,
                             "Average Purchase Price": avg_purchase_price_spender,
                             "Total Purchase Value":purchase_total_spender})

# Sort in descending order to obtain top 5 spender names 
formatted_spenders = top_spenders.sort_values(["Total Purchase Value"], ascending=False).head()

# Format with currency style
formatted_spenders.style.format({"Average Purchase Total":"${:,.2f}",
                                 "Average Purchase Price":"${:,.2f}", 
                                 "Total Purchase Value":"${:,.2f}"})

# MOST POPULAR ITEMS
# Create new data frame with items related information 
items = purchase_data[["Item ID", "Item Name", "Price"]]

# Group the item data by item id and item name 
item_stats = items.groupby(["Item ID","Item Name"])

# Count the number of times an item has been purchased 
purchase_count_item = item_stats["Price"].count()

# Calcualte the purchase value per item 
purchase_value = (item_stats["Price"].sum()) 

# Find individual item price
item_price = purchase_value/purchase_count_item

# Create data frame with obtained values
most_popular_items = pd.DataFrame({"Purchase Count": purchase_count_item, 
                                   "Item Price": item_price,
                                   "Total Purchase Value":purchase_value})

# Sort in descending order to obtain top spender names and provide top 5 item names
popular_formatted = most_popular_items.sort_values(["Purchase Count"], ascending=False).head()

# Format with currency style
popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})
