import requests

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIk4wwEAAAAANrr4lP1RPLAEA8rPpLsvQVlTPYw%3DNMuDhwfoRVT0v30bmNzZ1TPqhxk0flRcAjtBMFYY4fK5nYEczY'
username = 'BayoBreel'  # Replace with your Twitter username

url = f"https://api.twitter.com/2/users/by/username/{username}"
headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

response = requests.get(url, headers=headers)
user_data = response.json()

if 'data' in user_data:
    USER_ID = user_data['data']['id']
    print("User ID:", USER_ID)
else:
    print("Error fetching User ID:", user_data)


# Client ID - djdReGFzbnN2azRNcTNOZWJ6ZnY6MTpjaQ
# Client Secret - fi_QbFzp8ZRX-sREKVNV5nuqar0YTV0pY5IGptbz0CqwyTMOPV

# fi_QbFzp8ZRX-sREKVNV5nuqar0YTV0pY5IGptbz0CqwyTMOPV

# userId - 614257897