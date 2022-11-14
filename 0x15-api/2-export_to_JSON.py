#!/usr/bin/python3
"""
    Python script that returns information using a REST API
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    userId = argv[1]
    user_info = requests.get('{}users/{}'.format(url, userId)).json()
    username = user_info.get('username')
    all_tasks = requests.get('{}todos?userId={}'.format(url, userId)).json()

    user_dict = {}
    listof_dict = []

    for task in all_tasks:
        task['task'] = task['title']
        task.pop('title')
        task['username'] = username
        task.pop('userId')
        task.pop('id')
        listof_dict.append(task)

    user_dict[userId] = listof_dict

    with open('{}.json'.format(userId), 'w') as f:
        json.dump(user_dict, f)
