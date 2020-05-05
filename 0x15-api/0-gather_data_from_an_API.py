#!/usr/bin/python3
"""Using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    url1 = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    url2 = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    user = requests.get(url1).json()
    todo_list = requests.get(url2).json()
    done = 0
    ready = []
    for task in todo_list:
        if task["completed"] is True:
            done += 1
            ready.append(task["title"])
    print("Employee {} is done with tasks({}/{}):".
          format(user['name'], done, len(todo_list)))
    for task in ready:
        print("\t {}".format(task))
