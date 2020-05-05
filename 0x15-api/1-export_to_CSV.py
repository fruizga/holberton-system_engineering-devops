#!/usr/bin/python3
""" Exports data in CSV format """

import csv
import json
import requests
import sys


if __name__ == "__main__":
    """ Exports data in CSV format """

    ar1 = int(sys.argv[1])
    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(ar1)
    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(ar1)
    user = requests.get(url1).json()
    TODO = requests.get(url2).json()

    with open('{}.csv'.format(ar1), mode='w') as f:
        result = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in TODO:
            result.writerow([ar1, user.get('username\
            '), task.get('completed'), task.get('title')])
