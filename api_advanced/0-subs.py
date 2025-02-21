#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """

    Write a function that queries the Reddit API and returns
    the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.

    """
    #define user-urgent to avoid unwanted error or many error
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    #url of subreddit
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    #send request
    response = requests.get(url, headers=headers, allow_redirects=False)

    #check if response is successfully
    if response.status_code == 200:
       #extracted number of subscriber
        return requests.json().get('data').get('subscribers')
    
    #return 0 if request is fail
    return 0
