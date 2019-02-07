# Get password saved in keyring

import keyring
from config import username, keyringProfile

password = keyring.get_password(keyringProfile, username)
print(password)