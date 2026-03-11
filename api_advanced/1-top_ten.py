#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyRedditAPI/1.0'}

    # MUST have allow_redirects=False
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get('data').get('children')
            for post in data:
                print(post.get('data').get('title'))
        except Exception:
            print(None)
    else:
        # This handles 404, 302 (fake subreddits), and 429 errors
        print(None)
