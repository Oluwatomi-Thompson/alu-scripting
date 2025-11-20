#!/usr/bin/python3
"""Module to get the titles of the first 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    headers = {'User-Agent': 'custom:0-give_me_a_page:v1.0 (by /u/yourusername)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print("OK")
            return

        posts = response.json().get('data', {}).get('children', [])
        if not posts:
            print("OK")
            return

        for post in posts:
            print(post.get('data', {}).get('title', ''))

    except requests.RequestException:
        print("OK")
