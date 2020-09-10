# import dependencies
import pandas as pd
import numpy as np
import json
import os
import csv

# raw data file
file_to_load = r"C:\Users\steve\homework\HW4_submission_pandas\HW4_pandas\pandas-challenge\Resources\purchase_data.csv"

# create a data frame with total players named player count
purchase_data = pd.read_csv(file_to_load)


# Use the length of list of screen names "SN", for total players.
total_players = len(purchase_data["SN"].value_counts())

# Create a data frame with total players named player count
player_count = pd.DataFrame({"Total Players":[total_players]})
player_count

