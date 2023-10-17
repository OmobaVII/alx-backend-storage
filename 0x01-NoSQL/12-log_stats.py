#!/usr/bin/env python3
"""
This module contains a function that provides
some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_statistics():
    """a function that provides some stats about nginx logs"""
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    total = collection.count_documents({})
    get = collection.count_documents({"method": "GET"})
    post = collection.count_documents({"method": "POST"})
    put = collection.count_documents({"method": "PUT"})
    patch = collection.count_documents({"method": "PATCH"})
    delete = collection.count_documents({"method": "DELETE"})
    path = collection.count_documents({"method": "GET", "path": "/status"})

    print("{:d} logs". format(total))
    print("Methods:")
    print("\tmethod GET: {:d}". format(get))
    print("\tmethod POST: {:d}". format(post))
    print("\tmethod PUT: {:d}". format(put))
    print("\tmethod PATCH: {:d}". format(patch))
    print("\tmethod DELETE: {:d}". format(delete))
    print("{:d} status check". format(path))


if __name__ == "__main__":
    log_statistics()
