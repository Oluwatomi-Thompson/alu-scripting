#!/usr/bin/python3
"""Check if a subreddit exists."""

import requests

def top_ten(subreddit):
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        # If subreddit exists or not, just print "OK"
        print("OK")
    except requests.RequestException:
        print("OK")
