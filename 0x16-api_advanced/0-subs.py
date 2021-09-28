#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""
    url = "https://www.reddit.com/r/'+subreddit+'/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        users = response.json().get("data")
        return users.get("subscribers")
    else:
        return 0
