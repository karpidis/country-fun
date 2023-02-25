import os
import json

# reference set of keys that should be present in each JSON file
reference_keys = {"name", "code", "continent", "population", "area"}

# directory containing the JSON files
directory = "countries"

# list to store the names of countries with missing data
missing_data = []

# loop through each file in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        data = json.load(f)
        # check if all reference keys are present in the file
        if not reference_keys.issubset(set(data.keys())):
            # if not, add the country name to the missing_data list
            missing_data.append(data["name"])

# print the list of countries with missing data
print(missing_data)
