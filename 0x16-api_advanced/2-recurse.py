#!/usr/bin/python3
"""Recurse it!"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Write a recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    else:
        try:
            hot_list.append(response.json()['data']['children'][pos]['data']
                                                                    ['title'])
        except IndexError:
            return hot_list
    return (recurse(subreddit, hot_list, pos+1))
