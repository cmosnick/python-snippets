# Prompt user to enter password for username in ArcGIS Online
# Save credentials securely using your system's keyring manager
# Windows: windows Credential Manager
# Mac OS: Keychain
# See https://pypi.org/project/keyring/#what-is-python-keyring-lib for more info
# 
# Credentials are stored under <keyringProfileName>@arcgis_python_api_profile_passwords
# 

import getpass
import keyring
from config import username, keyringProfile


def validatePassword(username, password):
  # Insert actual validation here
  return True


while True:
  # Prompt user for password. getpass hides the password entry in console.
    password = getpass.getpass(prompt="Password for user %s:" % username, stream=None)

    # Try authenticating using the password provided
    success = validatePassword(username, password)
    if(success):
        keyring.set_password(keyringProfile, username, password)
        break

    print("Password invalid, try again\n\n")

print("Password successfully saved for {0}".format(username))
