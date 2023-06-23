import hashlib
import base64
import getpass
import requests
import os
from typing import Tuple


def get_username_and_pass_from_env_vars() -> tuple:
    username = os.environ.get("IRACING_UNAME")
    password = os.environ.get("IRACING_SECRET")
    return username, password


def ask_for_auth():
    """Asks the user for their iRacing username and password.

    Returns:
        str: Username of the iRacing account.
    """
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    return username, password


class iRacingAPI:
    def __init__(self, username, password) -> None:
        self.base_url = "https://members-ng.iracing.com/auth"
        self.session = requests.Session()
        self.username = username
        self.encoded_password = self.encode_auth(username, password)
        self.authenticate_on_iracing(username, self.encoded_password)
        

    def encode_auth(self, username: str, password: str) -> str:
        """Encodes the username and password into a base64 string.
        The iRacing API requires a base64 encoded string of the SHA256 hash of the password + username in lowercase.

        Args:
            username (str): Username of the iRacing account.
            password (str): Password of the iRacing account.

        Returns:
            str: Base64 encoded string of the SHA256 hash of the password + username in lowercase.
        """
        initialHash = hashlib.sha256((password + username.lower()).encode('utf-8')).digest()
        hashInBase64 = base64.b64encode(initialHash).decode('utf-8')
        return hashInBase64


    def authenticate_on_iracing(self, username: str, password: str):
        headers = {
            'Content-Type': 'application/json',
        }
        data = {"email": username, "password": password}
        
        # Try sending POST request to iRacing API
        try:
            resp = self.session.post(self.base_url, headers=headers, json=data)
            print(resp.status_code)
            print(resp.text)
        except requests.ConnectionError:
            raise RuntimeError("Error: Connection to iRacing API failed.")
        except requests.Timeout:
            raise RuntimeError("Error: Connection to iRacing API timed out.")
        
        # Check if the response is valid
        if resp.status_code != 200:
            raise RuntimeError("Error: Invalid response from iRacing API.")
    
    
# username, password = ask_for_auth()
# api = iRacingAPI(username=username, password=password)
# pwValueToSubmit = api.encode_auth(username, password)
# api.authenticate_on_iracing(username, pwValueToSubmit)
# print("Authenticated!")

