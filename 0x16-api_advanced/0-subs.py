#!/usr/bin/python3
"""Advanced API"""
import json
import requests


def number_of_subscribers(subreddit):
	"""number of subscribers for a subreddit"""
	api_url = 'https://www.reddit.com'
	query = 'r/{}/about.json'.format(subreddit)
	headers = {
	"User-Agent": "linux.hbtn.advanced.api (by u/Disastrous-Mistake72)"
	}
	requ = requests.get(
		url='{}/{}'.format(api_url, query),
		headers=headers,
		allow_redirects=False
	)
	if requ.status_code == 404:
		return 0
	res = requ.json()
	return res.get('data').get('subscribers')

if __name__ == '__main__':
	number_of_subscribers(subreddit)
