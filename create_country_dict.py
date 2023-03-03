import os
import json

# reference set of keys that should be present in each JSON file
reference_keys = {"name", "code", "continent", "population", "area"}

# directory containing the JSON files
directory = "countries"

# list to store the names of countries with missing data
country_dict = {}

# loop through each file in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        data = json.load(f)
    #add to country_dict name:code
    country_dict[data["name"]] = data["code"]

# print the list of countries with missing data
print(country_dict)
