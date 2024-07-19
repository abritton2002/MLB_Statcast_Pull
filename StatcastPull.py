# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 12:17:52 2023

@author: rfrey
"""
#pip install pandas
import pandas as pd
#pip install numpy
import numpy as np
#pip install datetime
import datetime
#pip install sqlite3
import sqlite3
#pip install baseball-scraper
from baseball_scraper import statcast

# Today's Date
today = datetime.date.today()

# Set the start date to July 14th
start_date = '2024-07-14'

# Calculate the previous day
prev_day = today - datetime.timedelta(days=1)
prev_day_str = prev_day.strftime('%Y-%m-%d')

# Acquire data from July 14th to the previous day
data = statcast(start_dt=start_date, end_dt=prev_day_str)

# Show the columns
print(list(data.columns.values))

# Write data to a CSV file
csv_file_path = 'statcast_data_test.csv'
data.to_csv(csv_file_path, index=False)

# Connect to DB and write to table
conn = sqlite3.connect('statcast_test.db')

table_name = 'statcast_data_test'

data.to_sql(table_name, conn, if_exists='append', index=False)

conn.close()

# Test to see data is there
# conn = sqlite3.connect('statcast_2023.db')

# cur = conn.cursor()

# df = cur.execute("SELECT * FROM statcast_data_2023 LIMIT 10")

# print(df.fetchone())

# conn = sqlite3.connect('statcast_2023.db')

# cur = conn.cursor()

# cur.execute("DELETE FROM statcast_data_2023")

# conn.commit()

# conn.close()