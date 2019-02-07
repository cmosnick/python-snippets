## How to save and retrieve credentials securely using keyring

This is especially handy when:
* You don't want to store passwords or other important things in a config file (do you ever want to??)
* A script is run on a scheduled basis, and you don't want to enter your credentials every time it runs

Using the `keyring` module, you can store your keys securely using your OS's built-in password manager.
On Windows: Windows Credential Manager
On Mac OS: Keychain

See the [keyring docs](https://pypi.org/project/keyring/) for more information.
