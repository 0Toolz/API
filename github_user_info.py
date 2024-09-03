import requests

# Replace 'octocat' with any GitHub username you want to look up
username = '0Toolz'

# GitHub API URL for user information
url = f'https://api.github.com/users/0Toolz'

# Send a GET request to the GitHub API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    user_data = response.json()
    
    # Display the user's information
    print(f"Username: {user_data['login']}")
    print(f"Name: {user_data['name']}")
    print(f"Bio: {user_data['bio']}")
    print(f"Public Repositories: {user_data['public_repos']}")
    print(f"Followers: {user_data['followers']}")
    print(f"Following: {user_data['following']}")
    print(f"Profile URL: {user_data['html_url']}")
else:
    print(f"Failed to retrieve data: {response.status_code}")