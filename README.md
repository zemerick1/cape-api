# Python class for Aruba / Cape Sensors

# Usage
from capepy import Cape

user = 'username'
upass = 'password'

## Creating the Cape object will log you in automatically and store the API token.
test = Cape(user, upass)

#### ID_Token for API calls
print(test.token)

#### User Profile
userProfile = test.getUserProfile()
print(userProfile)

# See examples/examples.py for more examples.