#!/usr/bin/env python3
"""
This module has a function that inserts a new
document in a collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """returns the id of the newly created documents"""
    return mongo_collection.insert_one(kwargs).inserted_id

if __name__ == "__main__":
    insert_school(mongo_collection, **kwargs)
