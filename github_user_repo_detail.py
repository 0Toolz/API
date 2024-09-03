#	•	Endpoint: https://api.github.com/repos/{owner}/{repo}
#	•	Method: GET
#	•	Parameters: {owner} is the GitHub username, and {repo} is the repository name.

import requests

owner = '0Toolz'
repo = 'API'
url = f'https://api.github.com/repos/{owner}/{repo}'

response = requests.get(url)

if response.status_code == 200:
    repo = response.json()

    print(f"Repository: {repo['name']}")
    print(f"description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Forks: {repo['forks_count']}")
    print(f"Open Issues: {repo['open_issues_count']}")
    print(f"Language: {repo['language']}")
    print(f"Clone URL: {repo['clone_url']}")
else:
    print(f"Failed to retrieve repository details: {response.status_code}")


