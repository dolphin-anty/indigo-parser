import requests

INDIGO_TOKEN = '<indigo_token>'  # Replace <indigo_token> to token from Indigo settings
INDIGO_PORT = '<indigo_port>'  # Replace <indigo_port> to port from Indigo settings
DOLPHIN_LOGIN = '<dolphin_login>'  # Replace <dolphin_login> to login for Dolphin Anty
DOLPHIN_PASSWORD = '<dolphin_password>'  # Replace <dolphin_password> to password for Dolphin Anty


# Don't touch the code below
def get_dolphin_token(login, password):
    json_data = {
        'username': DOLPHIN_LOGIN,  # Replace <your_login> to your login for Dolphin Anty Browser
        'password': DOLPHIN_PASSWORD,  # Replace <your_password> to your login for Dolphin Anty Browser
    }
    response = requests.post('https://dolphin-anty-api.com/auth/login', json=json_data)
    return response.json()['token']


DOLPHIN_TOKEN = f'Bearer {get_dolphin_token(DOLPHIN_LOGIN, DOLPHIN_PASSWORD)}'
