#!/usr/bin/python3
"""Exports data in JSON format"""
import requests
import jsonif __name__ == "__main__":
    """export JSON"""
    u = requests.get("https://jsonplaceholder.typicode.com/users").json()
    url2 = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    Dict = {}
    for i in u:
        ar1 = i.get("id")
        Name = i.get('username')
        for j in url2:
            if (j.get('userId') == int(ar1)):
                dict = {}
                dict['task'] = i.get('title')
                dict['completed'] = i.get('completed')
                dict['username'] = Name
        Dict[ar1] = url2
    with open("todo_all_employees.json", 'w') as JSONfile:
        json.dump(MyDict, JSONfile)
