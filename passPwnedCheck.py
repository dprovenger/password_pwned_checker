# passPwnedCheck.py utilizes the API from haveibeenpwned.com; which contains over 1/2 billion passwords
# These passwords have been exposed in previous breaches and stored in SHA-1 hash
# Details of the site/API can be found under https://haveibeenpwned.com/API/v3#PwnedPasswords
#
# pasPwnedCheck.py does not expose the password or its hash to haveibeenpwned.com
# As they implement a k-Anonymity model; which allows querying by partial hash only
#

import hashlib
import requests

# Adding interactive mode
print('--<>--')
print('Welcome, you are using passPwnedCheck.py in interactive mode!')
print('Enter the password you are considering using:')
print('--<>--')
password = input()

print('--<>--')
print('Thank you, searching if that phrase has been pwned!')
print('...')

# Hashing password to sha1
pwdHash = hashlib.sha1(password.encode())
pwdHashValue = pwdHash.hexdigest()

# Dividing hash to query API
hashPrefix = pwdHashValue[0:5]
hashSuffix = pwdHashValue[5:40]
print(pwdHashValue)
print(hashPrefix)
print(hashSuffix)