#!/usr/bin/env python3
"""
This module implements a get_page function
that uses the requests module to obtain html content
of a particular URL and returns it
"""
import redis
import requests
red = redis.Redis()
counts = 0


def get_page(url: str) -> str:
    """returns the html content of a URL"""
    cache_key = "count:{}".format(url)
    cache_html = red.get(url)

    if cache_html:
        access_count = red.incr(cache_key)
        return cache_html.decode("utf-8")

    response = requests.get(url)
    html_content = response.text
    red.setex(url, 10, html_content)
    red.setex(cache_key, 10, 1)
    return html_content


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/https://www.example.com"
    get_page(url)
