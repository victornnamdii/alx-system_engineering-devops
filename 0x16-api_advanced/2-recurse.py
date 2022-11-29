#!/usr/bin/python3
"""
    Contains the function recurse
"""

from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """
        Returns a list containing the titles of all hot articles
        for a given subreddit.
        Returns None if subreddit doesn't exist.
    """
    parameters = {"after": after}
    header = {"User-Agent": "victornnamdii"}
    result = get('https://www.reddit.com/r/{}/hot.json'.format(subreddit),
                 headers=header, allow_redirects=False, params=parameters)
    if result.status_code == 404:
        return None

    after = result.json().get('data').get('after')

    for item in result.json().get('data').get('children'):
        hot_list.append(item.get('data').get('title'))

    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
