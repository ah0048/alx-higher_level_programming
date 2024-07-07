#!/usr/bin/python3
'''list 10 commits'''
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    user = argv[2]
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    
    try:
        # Send GET request to fetch commits
        resp = requests.get(url)
        resp.raise_for_status()  # Raise exception for HTTP errors

        # Parse JSON response
        json_data = resp.json()

        # Print the most recent 10 commits (or less if there aren't enough)
        for i in range(min(10, len(json_data))):
            print("{}: {}".format(json_data[i]['sha'], json_data[i]['commit']['author']['name']))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError as e:
        print(f"Error parsing response: {e}")
