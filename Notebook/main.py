import requests
from requests_oauthlib import OAuth1

# Replace these with your actual credentials from Twitter API
API_KEY = ''
API_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Base URL for Twitter API v2 (GET request example: getting the user's timeline)
base_url = "https://api.x.com/2"

# Set up the OAuth1 authorization
auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


def send_get_request(endpoint, params=None):
    """
    Sends a GET request to the specified Twitter API endpoint.

    :param endpoint: The specific Twitter API endpoint.
    :param params: Dictionary of query parameters to be included in the request.
    :return: Response object from the GET request.
    """
    url = f"{base_url}/{endpoint}"
    response = requests.get(url, auth=auth, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


# Fetching the authenticated user's information
if __name__ == "__main__":
    endpoint = "users/me"
    params = {
        'user.fields': 'id,name,username,created_at'
    }

    user_data = send_get_request(endpoint, params)

    if user_data:
        print("Authenticated User Information:")
        print(user_data)
    else:
        print("Failed to get user information.")
