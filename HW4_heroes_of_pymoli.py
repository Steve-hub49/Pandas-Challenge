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

