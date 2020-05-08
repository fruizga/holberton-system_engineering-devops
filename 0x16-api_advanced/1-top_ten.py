#!/usr/bin/python3
""" Top 10 titles """
import requests


def top_ten(subreddit):
    """ Top 10 titles in subreddit """
    headers = {'user-agent': 'X-Modhash'}
    url = 'https://www.reddit.com/r/'
    re = requests.get(url + '{}/.json'.format(subreddit), headers=headers)
    subs = re.json()
    try:
        all_subs = subs['data']
        all_children = all_subs['children']
        for i in range(10):
            print(all_children[i]['data']['title'])
    except:
        print("None")
    return
