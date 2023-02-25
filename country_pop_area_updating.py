import pandas as pd
import json
import os

# read the population data into a pandas dataframe
pop_df = pd.read_excel('data/pop_2022.xls')

# read the area data into a pandas dataframe
area_df = pd.read_excel('data/area_2022.xls')

# loop through each country JSON file
for filename in os.listdir('countries'):
    filepath = os.path.join('countries', filename)

    # check if the file is a JSON file
    if filename.endswith('.json'):
        # load the JSON data for the country
        with open(filepath, 'r') as f:
            data = json.load(f)

        # get the country code
        code = data['code']

        # update the land area from the area dataframe
        land_area = area_df.loc[area_df['Country Code'] == code, '2020'].values[0]
        data['area'] = land_area

        # update the population from the population dataframe
        population = pop_df.loc[pop_df['Country Code'] == code, '2020'].values[0]
        data['population'] = population

        # save the updated JSON data back to the file
        with open(filepath, 'w') as f:
            json.dump(data, f)
