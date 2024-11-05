import requests

# Use your actual Bearer Token
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIk4wwEAAAAAxiOIKtEEuBUYLHd6yJwwoiLLTno%3DKmCNXdzelNpWntPoh4ubkJp9DDkuVi0K7QPcVNeVwWnbPSQSRb'

USER_ID = "614257897"  # Make sure this is the numeric user ID

url = f"https://api.twitter.com/2/users/{USER_ID}/followers"
headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

params = {
    "user.fields": "verified",
    "max_results": 1000
}

verified_count = 0
next_token = None

while True:
    if next_token:
        params["pagination_token"] = next_token

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if 'data' in data:
        verified_count += sum(1 for follower in data['data'] if follower.get("verified"))
        next_token = data.get('meta', {}).get('next_token')
        if not next_token:
            break
    else:
        print("No data available or API issue:", data)
        break

print("Number of verified followers:", verified_count)
