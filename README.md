# Python class for Aruba / Cape Sensors
[https://www.emerickcc.com](https://www.emerickcc.com)

# Usage
```python
from capepy import Cape

user = 'username'
upass = 'password'

#### Creating the Cape object will log you in automatically and store the API token.
test = Cape(user, upass)

#### ID_Token for API calls
print(test.token)

#### User Profile
userProfile = test.getUserProfile()
print(userProfile)
```

## See examples/examples.py for more examples.

## TODO:
1. Add preferences endpoint(s)
2. Fix Logout()
3. Find services endpoint.
4. Add PCAP endpoint. (use issues endpoint)
