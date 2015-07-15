# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:58:13 2015
# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.
@author: Mychal
"""


# your first attempt
# def make_hashtable(nbuckets):
#    hashtbl = []
#    i = 0
#    while i < nbuckets:
#        hashtbl.append([])
#        i = i + 1
#    return hashtbl


# better
def make_hashtable(nbuckets):
    hashtbl = []
    for unused in range(0, nbuckets):  # goes from 0 to nbuckets-1
        hashtbl.append([])
    return hashtbl
