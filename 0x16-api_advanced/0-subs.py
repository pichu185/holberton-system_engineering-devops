#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscri"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/'+subreddit+'/about.json"
    response = requests.get(url, headers={'User-Agent': 'Pichu'},
                            allow_redirects=False)
    if response.status_code == 200:
        users = response.json().get('data')
        return users.get('subscribers')
    return 0
