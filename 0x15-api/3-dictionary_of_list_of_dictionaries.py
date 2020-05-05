#!/usr/bin/python3
"""xport data in the JSON format"""
import json
import requests


if __name__ == "__main__":
    """export JSON"""
    u = requests.get("https://jsonplaceholder.typicode.com/users").json()
    url2 = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    a_dict = {}
    for i in u:
        Name = [j for j in url2 if j.get('userId') == i.get('id')]
        Name = [{'username': i.get('username'), 'task': j.get('title'),
                 'completed': j.get('completed')} for j in Name]
        a_dict[str(i.get('id'))] = Name
    with open("todo_all_employees.json", 'w') as JSONfile:
        json.dump(a_dict, JSONfile)
