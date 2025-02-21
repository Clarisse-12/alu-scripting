#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of total subscribers 
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The total number of subscribers for the subreddit.
             Returns 0 if the subreddit is invalid or an error occurs.
    """
    # Define the User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    
    # Construct the API URL for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    # Send a GET request to the Reddit API without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the number of subscribers from the JSON response
        return response.json().get('data', {}).get('subscribers', 0)
    
    # Return 0 if the request fails (e.g., invalid subreddit)
    return 0

