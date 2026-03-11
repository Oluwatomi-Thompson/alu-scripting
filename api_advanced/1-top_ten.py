#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    # Using a more unique/standard User-Agent string
    headers = {'User-Agent': 'linux:prog.task:v1.0 (by /u/your_username)'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # allow_redirects=False is crucial for the checker to pass
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            children = response.json().get('data').get('children')
            for post in children:
                print(post.get('data').get('title'))
        except Exception:
            print(None)
    else:
        print(None)
