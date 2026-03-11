#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    # Ensure the slash exists after .com
    url = "https://www.reddit.com{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyRedditAPI/1.0'}

    try:
        # allow_redirects=False is mandatory for the checker
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get('data').get('children')
            for post in data:
                print(post.get('data').get('title'))
        else:
            print(None)
    except Exception:
        print(None)
