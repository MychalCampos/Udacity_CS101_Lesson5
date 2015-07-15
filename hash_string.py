# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 22:30:03 2015
# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.
@author: Mychal
"""


# # my solution, this works but can be computationally more expensive
# def hash_string(keyword, buckets):
#    keyord = 0
#    for s in keyword:
#        keyord = keyord + ord(s)
'''
this last line may take long to compute if we have a long string and
and therefore a large value for keyord
'''
#    return keyord % buckets


# instructor's solution
def hash_string(keyword, buckets):
    h = 0
    for s in keyword:
        h = (h + ord(s)) % buckets  # more efficient computationally
    return h


print hash_string('a', 12)
# >>> 1

print hash_string('b', 12)
# >>> 2

print hash_string('a', 13)
# >>> 6

print hash_string('au', 12)
# >>> 10

print hash_string('udacity', 12)
# >>> 11
