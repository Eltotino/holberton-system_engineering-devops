#!/usr/bin/python3
"""Advanced API"""
import json
import requests


def top_ten(subreddit):
    """top ten posts for a subreddit"""
    api_url = 'https://www.reddit.com'
    query = 'r/{}/hot.json'.format(subreddit)
    headers = {
        "User-Agent": "linux.hbtn.advanced.api (by u/Disastrous-Mistake72)"
    }
    parameters = {
        "limit": 10
    }
    requ = requests.get(
        url='{}/{}'.format(api_url, query),
        headers=headers,
        params=parameters,
        allow_redirects=False
    )
    if requ.status_code == 404:
        print('None')
        return
    res = requ.json().get('data').get('children')
    for children in res:
        print(children.get('data').get('title'))
