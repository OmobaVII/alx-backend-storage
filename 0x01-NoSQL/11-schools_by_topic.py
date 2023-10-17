#!/usr/bin/env python3
"""This module contains a function that returns
the list of school having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """returns documents containing specific topic"""
    return mongo_collection.find({"topics": topic})


if __name__ == "__main__":
    schools_by_topic(mongo_collection, topic)
