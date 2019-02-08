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

    # Logout is returning 500 errors. Can't find correct headers
    def Logout(self):
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        return requests.delete('https://api.capenetworks.com/user/logout', headers=headers)
    def getUserProfile(self):
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        r = requests.get('https://api.capenetworks.com/user/profile', headers=headers)
        data = r.json()
        self.comp_id = data['company_uid']
        return data

    def getStartupData(self):
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        r = requests.get('https://api.capenetworks.com/dashboard/startup', headers=headers)
        data = r.json()
        return data

    def getUsers(self):
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        r = requests.get('https://api.capenetworks.com/user', headers=headers)
        data = r.json()
        return data

    def getSSID(self, ssid):
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        # Build nice uri
        uri = 'https://api.capenetworks.com/ssid/' + ssid
        r = requests.get(uri, headers=headers)
        data = r.json()
        return data

    def getTimezones(self):
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        uri = 'https://api.capenetworks.com/timezone-list'
        r = requests.get(uri, headers=headers)
        data = r.json()
        return data

    def getSensorNeighbors(self):
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        uri = 'https://api.capenetworks.com/ssid/recent'
        r = requests.get(uri, headers=headers)
        data = r.json()
        return data

    def editUser(self, userID, role):
        if role == 'viewer':
            restricted = True
        else:
            restricted = False
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        params = {
            "userId": "user-17a633826a03",
            "role": role,
            "restricted": restricted,
            "groups": []
        }
        uri = 'https://api.capenetworks.com/user/role'
        r = requests.post(uri, data=json.dumps(params), headers=headers)
        data = r.json()
        return data

    def createUser(self, firstname, surname, email, role):
        if role == 'viewer':
            restricted = True
        else:
            restricted = False
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        params = {
            "clientId": self.comp_id,
            "email": email,
            "firstname": firstname,
             "surname": surname,
            "role": role,
            "restricted": restricted,
            "groups": []
        }
        uri = 'https://api.capenetworks.com/user'
        r = requests.post(uri, data=json.dumps(params), headers=headers)
        data = r.json()
        return data

    def removeUser(self, userID):
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        uri = 'https://api.capenetworks.com/user' + userID
        r = requests.delete(uri, headers=headers)
        data = r.json()
        return data

    def removeSSID(self, ssid):
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        uri = 'https://api.capenetworks.com/ssid/' + ssid
        r = requests.delete(uri, headers=headers)
        data = r.json()
        return data

    def createSSID(self, ssid, security, passphrase, hidden=False, external=False, bandlock='auto'):
        alias = ssid
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        params = {
            "ssid": ssid,
            "hidden": hidden,
            "security": security,
            "alias": alias,
            "external_connectivity": external,
            "band_locking": bandlock,
            "phase2_auth": "",
            "proxies": {},
            "security_details": {"passphrase": passphrase}
        }
        uri = 'https://api.capenetworks.com/ssid'
        r = requests.post(uri, data=json.dumps(params), headers=headers)
        data = r.json()
        return data