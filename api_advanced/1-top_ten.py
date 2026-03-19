#!/usr/bin/python3
"""Module that queries the Reddit API and prints top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts of a subreddit."""
    headers = {
        'User-Agent': 'python:alu.reddit.api:v1.0 (by /u/demo_user)'
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)

    # ❗ KEY FIX: check BOTH status and redirect
    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
    except Exception:
        print(None)
        return

    # ❗ Ensure posts exist
    if not posts:
        print(None)
        return

    for post in posts[:10]:
        print(post.get('data', {}).get('title'))
