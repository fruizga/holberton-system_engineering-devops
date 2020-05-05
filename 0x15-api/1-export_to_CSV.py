#!/usr/bin/python3
"""xport data in the CSV format"""
from csv import writer, QUOTE_ALL
from sys import argv
import requests
import csv

if __name__ == "__main__":
    """export CSV"""
    ar1 = argv[1]
    url1 = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(ar1)).json()
    url2 = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ar1)).json()
    with open("{}.csv".format(ar1), 'w') as CVSfile:
        result = writer(CVSfile, delimiter=',', quoting=QUOTE_ALL)
        for i in url2:
            result.writerow([ar1, url1.get('username'),
                             i.get('completed'), i.get('title')])
