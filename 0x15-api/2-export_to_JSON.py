#!/usr/bin/python3
"""Exports data in JSON format"""
from sys import argv
import requests
import json

if __name__ == "__main__":
    """Exports data in JSON format"""
    ar1 = argv[1]
    u = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(ar1)).json()
    url2 = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ar1)).json()
    results = []
    for i in url2:
        res = {}
        res['task'] = i.get('title')
        res['completed'] = i.get('completed')
        res['username'] = u.get('username')
        results.append(res)
    FileInfo = {}
    FileInfo[ar1] = results
    with open("{}.json".format(ar1), 'w') as JSONfile:
        json.dump(FileInfo, JSONfile)
