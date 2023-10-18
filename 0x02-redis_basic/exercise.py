#!/usr/bin/env python3
"""
This module contains a class that is used to store
and write strings to Redis
"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator to count the number of times a method is called
    and store it in redis
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """a wraps method"""
        self._redis.incr(key)
        result = method(self, *args, **kwargs)

        return result
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    A decorator to store the history of inputs and outputs for a
    particular function
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper method"""
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


class Cache:
    """creates a class Cache"""

    def __init__(self, host='localhost', port=6379):
        """
        this defines the attribute of _redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        returns a string representation of the id
        given to the instance of Redis
        """
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float, None]:
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
