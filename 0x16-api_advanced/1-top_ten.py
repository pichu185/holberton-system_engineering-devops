#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of
    the first 10 hot posts
    """
    url = "https://www.reddit.com/r/'+subreddit+'/hot.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for i in range(10):
            hot = response.json()['data']['children'][i]['data']['title']
            print(hot)
    print("None")
