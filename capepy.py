import json
import requests

class Cape():
    def __init__(self, username, password):

        self.Login(username, password)

    def Login(self, username, password):
        self.username = username
        self.password = password
        params = {
            "realm": "Username-Password-Authentication",
            "audience": "https://cape.auth0.com/userinfo",
            "client_id": "nSHMAgKcZCIoBjYXQtk5LvLdsz1B0Nk5",
            "scope": "openid email company roles firebase_data",
            "grant_type": "http://auth0.com/oauth/grant-type/password-realm",
            "username": self.username,
            "password": self.password
        }
        headers = {
            "content-type": "application/json",
            "Auth0-Client": "eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS42LjEifQ==",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 NETGEAR/v1 (iOS Vuezone)"
        }
        r = requests.post('https://cape.auth0.com/oauth/token', data=json.dumps(params), headers=headers)
        body = r.json()
        self.token = body['id_token']
        return body

    def Logout(self):
        headers = {
            "Authorization": self.token
        }
        return requests.delete('https://api.capenetworks.com/user/logout', headers=headers)