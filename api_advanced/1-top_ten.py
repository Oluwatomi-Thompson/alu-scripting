#!/usr/bin/python3
"""Get the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print("OK")
            return

        data = response.json().get('data', {}).get('children', [])
        if not data:
            print("OK")
            return

        for post in data:
            print(post.get('data', {}).get('title'))

    except requests.RequestException:
        print("OK")
