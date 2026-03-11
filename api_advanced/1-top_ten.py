#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    # Try a very generic but established User-Agent
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com{}/hot.json?limit=10".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        children = data.get('children')
        if children:
            for post in children:
                print(post.get('data').get('title'))
        else:
            print(None)
    else:
        # If 302 (fake), 404, or 429 (blocked), print None
        print(None)
