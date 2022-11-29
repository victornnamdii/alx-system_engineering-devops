#!/usr/bin/python3
"""
    Contains the function number_of_subscribers
"""

from requests import get


def number_of_subscribers(subreddit):
    """
        Returns the number of subscribers for a given subreddit.
        Returns 0 if subreddit doesn't exist.
    """
    header = {"User-Agent": "victornnamdii"}
    result = get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                 headers=header, allow_redirects=False)
    if result.status_code == 404:
        return 0
    return result.json().get('data').get('subscribers')
