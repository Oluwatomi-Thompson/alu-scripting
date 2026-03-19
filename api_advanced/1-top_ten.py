#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts of a subreddit."""
    headers = {
        'User-Agent': 'python:alu.reddit.api:v1.0 (by /u/demo_user)'
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get('data', {}).get('children', [])

    for post in posts[:10]:
        print(post.get('data', {}).get('title'))
