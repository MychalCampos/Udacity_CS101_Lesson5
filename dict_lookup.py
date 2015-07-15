# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:18:13 2015
# Change the lookup procedure
# to now work with dictionaries.
@author: Mychal
"""


def lookup(index, keyword):  # index is now a dictionary
    if keyword in index:
        return index[keyword]
    else:
        return None 
