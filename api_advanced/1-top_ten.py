#!/usr/bin/python3
"""Write a function that queries the Reddit API
"""


import requests


import sys


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """

    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        hot_posts = response.json().get('data').get('children')
        for post in hot_posts:
            print(post.get('data').get('title'))
    else:
        print(None)

