import requests

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIk4wwEAAAAANrr4lP1RPLAEA8rPpLsvQVlTPYw%3DNMuDhwfoRVT0v30bmNzZ1TPqhxk0flRcAjtBMFYY4fK5nYEczY'

username = "BayoBreel"  # Replace with your Twitter username
user_url = f"https://api.twitter.com/2/users/by/username/{username}"
user_response = requests.get(user_url, headers={"Authorization": f"Bearer {BEARER_TOKEN}"})
user_data = user_response.json()

if 'data' in user_data:
    USER_ID = user_data['data']['id']  # Get the user ID from the response
    print(USER_ID)
else:
    print("Error fetching user ID:", user_data)
