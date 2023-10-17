#!/usr/bin/env python3
"""
This module has a function that returns
all students sorted by average score
"""
import pymongo


def top_students(mongo_collection):
    """a function that returns all students sorted
    by average scores"""
    result =  [
            {
                "$project": {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                    }
                },
            { 
                "$sort": {"averageScore": -1}
                }
            ]
    return list(mongo_collection.aggregate(result))
