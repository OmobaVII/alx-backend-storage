#!/usr/bin/env python3
"""
This module contains a class that is used to store
and write strings to Redis
"""
import redis
from uuid import uuid4


class Cache:
    """creates a class Cache"""

    def __init__(self, host='localhost', port=6379):
        """
        this defines the attribute of _redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        returns a string representation of the id
        given to the instance of Redis
        """
        key = str(uuid4())
        self._redis.set(key, data)

        return key
