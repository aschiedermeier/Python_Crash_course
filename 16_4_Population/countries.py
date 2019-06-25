###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 16: Downloading Data
###########################################

###########################################
# population



###########################################
# list all country codes in dict 
# get country code using dictionaries COUNTRIES from
# module pygal_maps_world
from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])

