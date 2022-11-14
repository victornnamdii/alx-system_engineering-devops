#!/usr/bin/python3
"""
    Python script that returns information using a REST API
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    all_user_info = requests.get('{}users'.format(url)).json()

    user_ids = []
    for user in all_user_info:
        user_ids.append(user.get('id'))

    user_dict = {}

    for id in user_ids:
        listof_dict = []
        user_info = requests.get('{}users/{}'.format(url, id)).json()
        username = user_info.get('username')
        all_tasks = requests.get('{}todos?userId={}'.format(url, id)).json()
        for task in all_tasks:
            task['task'] = task['title']
            task.pop('title')
            task['username'] = username
            task.pop('userId')
            task.pop('id')
            listof_dict.append(task)
        user_dict[id] = listof_dict

    with open('todo_all_employees.json', 'w') as f:
        json.dump(user_dict, f)
