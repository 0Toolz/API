#	•	Endpoint: https://api.github.com/users/{username}/repos
#	•	Method: GET
#	•	Parameters: {username} is the GitHub username

import requests

username = '0Toolz'
url = f'https://api.github.com/users/0Toolz/repos'

response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    
    print(f"Repositories for user {username}:")
    for repo in repos: 
    	print(f"Name: {repo['name']}, Stars: {repo['stargazers_count']}, Language: {repo['language']}, URL: {repo['html_url']}")
    else:
    	print(f"Failed to retrieve repositories: {response.status.code}")