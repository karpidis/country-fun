#this was created to find which countries had different name from un members in all_countries data
import os
import json
from country_list import un_members

checked_un_members = []

# loop through each JSON file in the "countries" directory
for filename in os.listdir('countries'):
    with open(os.path.join('countries', filename), 'r') as f:
        # load the JSON data for the country
        data = json.load(f)
        name = data['name']
        # check if the country is in the UN members list
        if name in un_members:
            checked_un_members.append(name)

# compare the UN members list and the checked list
missing_countries = list(set(un_members) - set(checked_un_members))
print(f"Missing countries: {missing_countries}")
