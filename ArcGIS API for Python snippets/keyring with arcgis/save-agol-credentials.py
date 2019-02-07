# Prompt user to enter password for username in ArcGIS Online
# Authenticate against AGOL
# Prompt again if authentication fails
# Save credentials securely using your system's keyring manager
# Windows: windows Credential Manager
# Mac OS: Keychain
# See https://pypi.org/project/keyring/#what-is-python-keyring-lib for more info
# 
# Credentials are stored under <keyringProfileName>@arcgis_python_api_profile_passwords
# 

import getpass
from arcgis.gis import GIS
from config import agolUsername, agolURL, keyringProfile

while True:
    try:
        password = getpass.getpass(prompt="Password for user %s:" % agolUsername, stream=None)
        gis = GIS(agolURL, username=agolUsername, profile=keyringProfile, verify_cert=False, password=password)
        print("Successfully logged in as: " + gis.properties.user.username + " and stored credentials in .arcgisprofile")
        break
    except RuntimeError as e:
        print(str(e))