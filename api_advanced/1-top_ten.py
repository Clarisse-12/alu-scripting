#!/usr/bin/python3
"""Write a function that queries the Reddit API
"""


import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """

    headers = {'User-Agent': 'CustomBot/1.0'} 
    params = {'limit': 10} 
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit) 

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        try:  
            data = response.json()
            hot_posts = data.get('data', {}).get('children', [])

            if not hot_posts:
                print(None)  
                return

            for post in hot_posts:
                title = post.get('data', {}).get('title')
                if title: 
                    print(title)
                else:
                    print("Unknown Title") 

        except (ValueError, KeyError):
            print(None)
            return

    else:
        print(None) 
        return 0
