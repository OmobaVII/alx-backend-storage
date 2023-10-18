#!/usr/bin/env python3
"""
This module contains a class that is used to store
and write strings to Redis
"""
import redis
import uuid


class Cache:
    """creates a class Cache"""

    def __init__(self, host='localhost', port=6379):
        """
        this defines the attribute of _redis
        """
        self._redis = redis.Redis(host=host, port=port)
        self._redis.flushdb()

    def store(self, data):
        """
        returns a string representation of the id
        given to the instance of Redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
