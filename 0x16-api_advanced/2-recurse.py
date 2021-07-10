#!/usr/bin/python3
"""Advanced API"""
import json
import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    """Recursively returns hotest title"""
    api_url = 'https://www.reddit.com'
    query = 'r/{}/hot.json'.format(subreddit)
    headers = {
        "User-Agent": "linux.hbtn.advanced.api (by u/Disastrous-Mistake72)"
    }
    parameters = {
        "after": after,
        "count": count
    }
    requ = requests.get(
        url='{}/{}'.format(api_url, query),
        headers=headers,
        params=parameters,
        allow_redirects=False
    )
    if requ.status_code == 404:
        return None
    res = requ.json().get('data')
    after = res.get('after')
    count += res.get('dist')
    children = res.get('children')
    for infant in children:
        hot_list.append(infant.get('data').get('title'))
    if after:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
