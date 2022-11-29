#!/usr/bin/python3
"""
    Contains the function top_ten
"""

from requests import get


def top_ten(subreddit):
    """
        Prints the titles of the first 10 hot posts listed for
        a given subreddit.
        Prints None if subreddit doesn't exist.
    """
    parameters = {"limit": 10}
    header = {"User-Agent": "victornnamdii"}
    result = get('https://www.reddit.com/r/{}/hot.json'.format(subreddit),
                 headers=header, allow_redirects=False, params=parameters)
    if result.status_code == 404:
        print(None)
    else:
        for item in result.json().get('data').get('children'):
            print(item.get('data').get('title'))
