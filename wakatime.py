import requests

# Set your WakaTime API key
api_key = 'waka_0dc22ffa-5469-4c65-a263-b771955058bc'

# Set the username of the GitHub account you want to display the data for
github_username = 'Ronnie-Leon76'

# Set the repository name of the repository you want to display the data for
repository_name = 'PivotClub-Backend'

# Make a request to the WakaTime API to retrieve the data
response = requests.get(f'https://wakatime.com/api/v1/users/current/github/{github_username}/{repository_name}/stats/last_7_days', headers={'Authorization': f'Basic {api_key}'})

# Check if the request was successful
if response.status_code == 200:
  # Parse the response data
  data = response.json()
  
  # Extract the relevant data from the response
  total_seconds = data['data']['grand_total']['total_seconds']
  human_readable_time = data['data']['grand_total']['human_readable_total']
  
  # Format the data for display in the README
  readme_markdown = f'Total time spent coding in the last 7 days: {human_readable_time} ({total_seconds} seconds)'
else:
  # Handle the error
  print(f'Error {response.status_code}: {response.text}')
