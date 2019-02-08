from capepy import Cape

user = 'username'
upass = 'password'

# Creating the Cape object will log you in automatically and store the API token.
test = Cape(user, upass)

#### ID_Token for API calls
print(test.token)

#### User Profile
userProfile = test.getUserProfile()
print(userProfile)

#### Company UID
# Need this to create users!
print(userProfile['company_uid'])

# Print network information
startup = test.getStartupData()

#### Startup Data
print(startup)

#### DHCP Data
print(startup['network']['dhcp'])

#### DNS Data
print(startup['network']['dns'])

#### Sensor Configs
print(startup['sensor_configs'])

#### User Data
print(test.getUsers())

#### SSID info
print(test.getSSID('ssid-fd78781c74b1'))

#### Get Timezone List
print(test.getTimezones())

#### Get Sensor Neighbors
print(test.getSensorNeighbors())

#### Edit User
# Returns:
# {'groups': [], 'restricted': True, 'role': 'viewer'}
# Find the userID by using the getUsers() method
userID = 'user-17a633826a02'
role = 'viewer' # viewer / admin
#print(test.editUser(userID, role))

#### Create User
# createUser(firstname, surname, email, role):
#print(test.createUser('first', 'Last', 'email@email.com', 'viewer'))

#### Delete User
# userID = user-ca2f45d44267
#print(test.removeUser(userID))

#### Delete SSID
# ssid = ssid-ca2f45d44267
#print(test.removeSSID(ssid))

#### Create SSID
# createSSID(self, ssid, security, passphrase, hidden=False, external=False, bandlock='auto')
# Can also pass a data object shown below.
data = {
    "ssid" : "ESSID",
    "security": "wpa-psk",
    "passphrase": "passphrase"
}
#print(test.createSSID(**data))

#### Get SSIDs
print(test.getSSIDs())

#### Get Issues
issues = test.getIssues()
#for issue in issues['issues']:
#    print(issue)
print(issues)

#### Get Sensors
print(test.getSensors())

#### Get Mutes
print(test.getMutes())

#### Get Groups
print(test.getGroups())

#### Create Groups

#print(test.createGroup('Test'))

#### Delete Group
# Get Group from test.GetGroups()
#print(test.removeGroup(groupID))

#### Get Latest Test Data
# Not real sure what the return values mean, yet.
print(test.getLatest())