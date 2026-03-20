#!/usr/bin/python3
"""Module that queries the Reddit API and prints top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts of a subreddit."""
    # Use a highly specific, unique User-Agent to bypass bot detection
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36'
    }
    url = "https://www.reddit.com{}/hot.json?limit=10".format(subreddit)

    try:
        # allow_redirects=False is mandatory to catch invalid subreddits
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If status code is not 200, the subreddit is invalid or blocked
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data', {})
        children = data.get('children', [])

        if not children:
            print(None)
            return

        for post in children:
            print(post.get('data', {}).get('title'))

    except Exception:
        print(None)
