#!/usr/bin/env python3
"""
This module contains a class that is used to store
and write strings to Redis
"""
import redis
from uuid import uuid4
from typing import Union


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

    def get(self, key: str, fn: Callable = None) -> \
            Union[str, bytes, int, float, None]:
        """
        Retrieve data from redis using provided key
        and apply the callable option
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        retrieve and return data as a string
        """
        return self.get(key, str)

    def get_int(self, key, str) -> int:
        """
        retrieve and return data as an integer
        """
        return self.get(key, int)
