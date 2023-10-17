#!/bin/usr/env python3
"""
This module contains a function that lists all
documents in a collection
"""


def list_all(mongo_collection):
    """returns a list of all documents in a collection"""
    if not mongo_collection:
        return []
    return (mongo_collection.find())
