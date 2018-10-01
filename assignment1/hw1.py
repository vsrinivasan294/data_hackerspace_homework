#
# Vishnu Srinivasan 
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due October 1st, 2018
#

import json
import csv
import numpy as np
import pandas as pd

def histogram_times(filename):

    flight_data = pd.read_csv(filename)
    flight_data1 = flight_data.dropna(subset = ['Time'])
    flight_data1['Time'] = flight_data1['Time'].str.split(':').str[0]

    #Removing the bad values
    flight_data1 = flight_data1.drop(flight_data1.index[flight_data1.Time == 'c'])
    flight_data1 = flight_data1.drop(flight_data1.index[flight_data1.Time == 'c16'])
    flight_data1 = flight_data1.drop(flight_data1.index[flight_data1.Time == 'c14'])
    flight_data1 = flight_data1.drop(flight_data1.index[flight_data1.Time == '114'])
    flight_data1 = flight_data1.drop(flight_data1.index[flight_data1.Time == '0943'])
    flight_data1 = flight_data1.drop(flight_data1.index[flight_data1.Time == '18.40'])
    flight_data1 = flight_data1.drop(flight_data1.index[flight_data1.Time == '22\'08'])
    flight_data1 = flight_data1.drop(flight_data1.index[flight_data1.Time == '12\'20'])

    #Convert into a series and also into ints
    flight_data2 = pd.Series(flight_data1['Time'])
    flight_data2.sort_values(ascending = True)
    flight_data2 = pd.to_numeric(flight_data2, errors='coerce')

    #Counter for the value 
    flight_data3 = flight_data2.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)
    flight_data3.sort_values(ascending = True)

    output = flight_data3.tolist()

    out = [flight_data3[0]]
    out.append(flight_data3[1])
    out.append(flight_data3[2])
    out.append(flight_data3[3])
    out.append(flight_data3[4])
    out.append(flight_data3[5])
    out.append(flight_data3[6])
    out.append(flight_data3[7])
    out.append(flight_data3[8])
    out.append(flight_data3[9])
    out.append(flight_data3[10])
    out.append(flight_data3[11])
    out.append(flight_data3[12])
    out.append(flight_data3[13])
    out.append(flight_data3[14])
    out.append(flight_data3[15])
    out.append(flight_data3[16])
    out.append(flight_data3[17])
    out.append(flight_data3[18])
    out.append(flight_data3[19])
    out.append(flight_data3[20])
    out.append(flight_data3[21])
    out.append(flight_data3[22])
    out.append(flight_data3[23])
    return out


def weigh_pokemons(filename, weight):
  
    out = []
    with open(filename) as f:
        data = json.load(f)
        for pkmn in data["pokemon"]:
            if (float(pkmn["weight"].split(" ")[0]) == weight):
                out.append(pkmn["name"])
    return out

def single_type_candy_count(filename):
  
    out = 0

    with open(filename) as f:
        data = json.load(f)
        for pkmn in data["pokemon"]:
            if (len(pkmn["type"]) == 1):
                if ('candy_count' in pkmn):
                    out = out + pkmn["candy_count"]
    return out

###### -- Do this later too

def reflections_and_projections(points):
    pass

def normalize(image):
    pass

def sigmoid_normalize(image): #Extra credit
    pass
