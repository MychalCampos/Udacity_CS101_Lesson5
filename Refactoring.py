# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:20:44 2015
# Refactoring
# 6. In video 28. Update, it was suggested that some of the duplicate code in
# lookup and update could be avoided by a better design.  We can do this by
# defining a procedure that finds the entry corresponding to a given key, and
# using that in both lookup and update.

# Whenever we have duplicate code like the loop that finds the entry in the original
# hashtable_update and hashtable_lookup, we should think if there is a better way
# to write this that would avoid the duplication. We should be able to rewrite
# these procedures to be shorter by defining a new procedure and rewriting both
# hashtable_update and hashtable_lookup to use that procedure. This rewriting 
# process is called refactoring.

# Modify the code for both hashtable_update and hashtable_lookup to have the same
# behavior they have now, but using fewer lines of code in each procedure.  You
# should define a new procedure to help with this. Your new version should have
# approximately the same running time as the original version, but neither
# hashtable_update or hashtable_lookup should include any for or while loop, and
# the block of each procedure should be no more than 6 lines long.
@author: Mychal
"""

# original
def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return
    bucket.append([key, value])
    
# original
def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None


def make_hashtable(size):
    table = []
    for unused in range(0, size):
        table.append([])
    return table


def hash_string(s, size):
    h = 0
    for c in s:
         h = h + ord(c)
    return h % size


def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]


# # helper function (Your solution)
# # this works, but the bucket_find solution below from the instructor
# # is better and simpler
# def lookup(bucket, key):
#    for entry in bucket:
#        if entry[0] == key:
#            return entry[1]
#    return None


# # new (Your solution) 
# # this works, but the solution below from the instructor is simpler and better
# def hashtable_update(htable, key, value):
#    bucket = hashtable_get_bucket(htable, key)
#    if hashtable_lookup(htable, key) != None:
#        bucket[0][1] = value
#        return
#    bucket.append([key, value])
        

# # new (Your solution)
# # this works, but the solution below from the instructor is simpler and better 
# def hashtable_lookup(htable, key):
#    bucket = hashtable_get_bucket(htable, key)
#    return lookup(bucket, key)


# new (instructor's solution)
def bucket_find(bucket, key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None


# new (instructor's solution)
def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    entry = bucket_find(bucket, key)
    if entry:
        entry[1] = value
    else:
        bucket.append([key, value])


# new (instructor's solution)
def hashtable_lookup(htable, key):
    entry = bucket_find(hashtable_get_bucket(htable, key), key)    
    if entry:
        return entry[1]
    else:
        return None
        
        
# Your procedures should have the same behavior as the originals.  For example,
table = make_hashtable(10)
hashtable_update(table, 'Python', 'Monty')
hashtable_update(table, 'CLU', 'Barbara Liskov')
hashtable_update(table, 'JavaScript', 'Brendan Eich')
hashtable_update(table, 'Python', 'Guido van Rossum')
print hashtable_lookup(table, 'Python')
#>>> Guido van Rossum