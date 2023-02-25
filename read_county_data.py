import pandas as pd
import json
import os
from country_list import un_members

# read the CSV file into a pandas dataframe
df = pd.read_csv('data/all_countries.csv')

# loop through each row in the dataframe
for index, row in df.iterrows():
    # get the country code and continent from the row
    code = row['alpha-3']
    continent = row['region']
    name = row['name']

    # only create JSON files for countries in un_members
    if name not in un_members:
        continue

    # construct the filename for the country's JSON file
    filename = f"{code}.json"
    filepath = os.path.join('Countries', filename)

    # create a dictionary to store the country's data
    data = {
        'name': name,
        'code': code,
        'continent': continent,
        'population': None,
        'area': None,
        'elo': 1500
    }

    # save the data to the JSON file
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)
