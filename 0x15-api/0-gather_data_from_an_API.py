#!/usr/bin/python3
"""Using REST API, for a given employeeID."""
from sys import argv
import requestsif __name__ == "__main__":
    """Getting TODO"""
    iD = argv[1]
    Z = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(iD)).json()
    Req_A = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(iD)).json()
    N = Z.get('name')
    Req_Form = [i for i in Req_A if i.get('userId') == Z.get('id')]
    Ready = [i for i in Req_Form if i.get('completed')]
    print("Employee {} is done with tasks({}/{}):".
          format(N, len(Ready), len(Req_Form)))
    [print('\t', i.get('title')) for i in Ready]