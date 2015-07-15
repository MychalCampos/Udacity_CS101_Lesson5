# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 17:51:44 2015
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5
@author: Mychal
"""


population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0,
              'Mumbai': 12.5}

# alternatively
population = {}
population['Shanghai'] = 17.8
population['Istanbul'] = 13.3
population['Karachi'] = 13.0
population['Mumbai'] = 12.5

print population['Mumbai']
