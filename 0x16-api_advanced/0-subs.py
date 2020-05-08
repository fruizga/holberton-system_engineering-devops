#!/usr/bin/python3
""" using the reddit api, returns info about subscribers """
import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers"""
    headers = {'user-agent': 'X-Modhash'}
    url = 'https://www.reddit.com/r/'
    req = requests.get(url + '{}/about.json'.format(subreddit), headers=headers)
    subs = req.json()
    try:
        all_subs = subs['data']['subscribers']
        return all_subs
    except:
        return 0
