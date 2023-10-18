#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

cache = Cache()
cache.store("foooo")
cache.store("barrr")
cache.store(68)
replay(cache.store)
