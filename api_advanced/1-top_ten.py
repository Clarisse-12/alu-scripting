#!/usr/bin/python3
"""
Reddit API Query Script

This module contains a function to query the Reddit API and print the
titles of the first 10 hot posts listed for a given subreddit.

Functions:
    - top_ten(subreddit): Prints the top 10 hot post titles.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the titles or "None" if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)  
        return

    headers = {'User-Agent': 'CustomUserAgent/1.0'} 
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}  

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            
            if not posts:
                print(None) 
            
            for post in posts:
                print(post.get('data', {}).get('title', "Unknown Title"))
        else:
            print(None) 

    except requests.RequestException:
        print(None)  
