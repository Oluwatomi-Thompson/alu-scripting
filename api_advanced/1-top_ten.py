#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints titles of top 10 hot posts for a subreddit"""
    url = "https://www.reddit.com{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyRedditAPI/1.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for post in children:
                print(post.get('data').get('title'))
        else:
            print(None)
    except Exception:
        print(None)
