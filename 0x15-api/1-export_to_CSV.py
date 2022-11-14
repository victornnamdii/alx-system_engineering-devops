#!/usr/bin/python3
"""
    Python script that returns information using a REST API
"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    userId = argv[1]
    user_info = requests.get('{}users/{}'.format(url, userId)).json()
    username = user_info.get('username')
    all_tasks = requests.get('{}todos?userId={}'.format(url, userId)).json()

    with open('{}.csv'.format(userId), 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in all_tasks:
            csvwriter.writerow([int(userId), username,
                               task.get('completed'), task.get('title')])
