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
import math

def histogram_times(filename):

    out = []
    
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
    
    for x in range (len(flight_data3)):
        out.append(flight_data3[x])
   
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
    
    arrYOne = np.matmul(points,[[1, 0], [0, -1]]) 
    arrPi = np.matmul(arrYOne, [[0, -1], [1, 0]])
    arrLine = np.matmul(arrPi, [[1, 3], [3, 9]])
    arrLine = arrLine*.1
    
    return arrLine

####### -- Wtf is this unholy piece of code above ^^


def normalize(image):
    maximum = image.max()
    minimum = image.min()
    
    for x in range(len(image)):
        for y in range(len(image[0])):
            p = image[x,y]
            image[x,y] = (float(p - minimum) * 255.0)/float(maximum-minimum)
    
    return image

def sigmoid_normalize(image, a):
    
    for x in range(len(image)):
        for y in range(len(image[0])):
            p = image[x,y]
            image[x,y] = 255 * ((255 * (1 + math.exp( (p-128) * ((-a) ** (-1)) )))**(-1)) 
    return image



