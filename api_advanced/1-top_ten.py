#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    # Use a descriptive User-Agent as required by Reddit's API guidelines
    headers = {'User-Agent': 'ALX-Project-v1.0 (by /u/username)'}
    url = "https://www.reddit.com{}/hot.json".format(subreddit)
    
    # params='limit=10' is better than slicing in a loop
    params = {'limit': 10}
    
    # allow_redirects=False is the absolute requirement
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post.get('data', {}).get('title'))
    else:
        # If not a valid subreddit or any other error, print None
        print(None)
