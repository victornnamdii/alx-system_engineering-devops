#!/usr/bin/python3
""" Functions to adcquire info from API Reddit"""
from requests import get


def count_words(subreddit, word_list):
    """Count the titles found with wordlist in subreddit"""
    my_list = recurse(subreddit)
    my_dict = {}
    count = 0

    if my_list is not None:
        for word in word_list:
            my_dict[word] = 0

        for title in my_list:
            title_split = title.split(" ")

            for iter in title_split:
                for iter_split in word_list:
                    if iter.lower() == iter_split.lower():
                        count = 1
                        my_dict[iter_split] += 1
        if count == 0:
            return
        for key, val in sorted(my_dict.items(),  key=lambda x: x[1],
                               reverse=True):
            if val != 0:
                print("{}: {}".format(key, val))
    else:
        return


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
    if result.status_code != 200:
        return None

    after = result.json().get('data').get('after')

    for item in result.json().get('data').get('children'):
        hot_list.append(item.get('data').get('title'))

    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
