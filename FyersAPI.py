import requests

def get_access_token(client_id, client_secret, username, password):
    # FYERS API endpoint for access token
    auth_url = 'https://api.fyers.in/api/v1/token'

    # Request parameters
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'password',
        'username': username,
        'password': password
    }

    try:
        response = requests.post(auth_url, data=data)
        response_data = response.json()
        access_token = response_data['access_token']
        return access_token
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching access token:", e)
        return None

def main():
    # Your FYERS API credentials
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'

    # Your FYERS account credentials
    username = 'YOUR_USERNAME'
    password = 'YOUR_PASSWORD'

    # Get the access token
    access_token = get_access_token(client_id, client_secret, username, password)

    if access_token:
        print("Access Token:", access_token)
    else:
        print("Failed to get the access token.")

if __name__ == '__main__':
    main()
