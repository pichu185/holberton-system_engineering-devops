#!/usr/bin/python3
"""Export to JSON"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = requests.get(url + "users/{}".format(argv[1])).json()
    all = requests.get(url + "todos", params={"userId": argv[1]}).json()
    completed_tasks = []
    for task in all:
        task_dic = {}
        task_dic["task"] = task.get("title")
        task_dic["completed"] = task.get("completed")
        task_dic["username"] = user.get("username")
        completed_tasks.append(task_dic)
    json_obj = {}
    json_obj[argv[1]] = completed_tasks
    with open(argv[1] + ".json", "w") as jsonFile:
        json.dump(json_obj, jsonFile)
