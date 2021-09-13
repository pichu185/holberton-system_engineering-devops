#!/usr/bin/python3
"""Export to CSV"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = requests.get(url + "users/{}".format(argv[1])).json()
    all = requests.get(url + "todos", params={"userId": argv[1]}).json()
    completed_tasks = []
    for task in all:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))

    with open(str(argv[1]) + ".csv", "w") as file:
        w = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in all:
            w.writerow([int(argv[1]), user_id.get('username'),
                        task.get('completed'), task.get('title')])
