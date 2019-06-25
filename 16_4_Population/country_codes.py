###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 16: Downloading Data
###########################################

###########################################
# population

###########################################
# list all country codes in dict 
# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code,COUNTRIES[country_code])
###########################################
# get country code using dictionaries COUNTRIES from
# module pygal_maps_world
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return None

# print (get_country_code("Andorra"))
# print (get_country_code("United Arab Emirates"))
# print (get_country_code("Afghanistan"))



###########################################
# world population

import json

# Load the data into a list.
filename = "population_data.json"
with open (filename) as f:
    pop_data = json.load(f)

# Print the 2010 population for each country.
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        # if code:
        #     print (code + ": " + str(population))
        # else:
        #     print("ERROR - " + country_name)

