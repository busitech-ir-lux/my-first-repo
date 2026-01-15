#!/usr/bin/python3
import sys
import requests

# Get username and password from command line arguments
username = sys.argv[1]
password = sys.argv[2]

# GitHub API endpoint for authenticated user
url = 'https://api.github.com/user'

# Make request with Basic Authentication
response = requests.get(url, auth=(username, password))

# Check if the request was successful
if response.status_code == 200:
    # Display the user id
    print(response.json().get('id'))
else:
    # If authentication fails, print None
    print("None")
