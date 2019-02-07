## Save and retrieve ArcGIS Online credentials securely using keyring

See my general [keyring example]() for more info.  This is what the ArcGIS API for Python uses on the backend. The API makes it even easier than the keyring example!

This is especially handy when:
* You don't want to store passwords or other important things in a config file (do you ever want to??)
* A script is run on a scheduled basis, and you don't want to enter your credentials every time it runs

### Setup:

* Change the values in `config.py` to match your username, arcgis online url, and profile name your credentials will be stored under.

* [save-agol-credentials.py](https://github.com/cmosnick/python-snippets/blob/master/ArcGIS%20API%20for%20Python%20snippets/keyring%20with%20arcgis/save-agol-credentials.py) will securely prompt the user for their password and authenticate against ArcGIS online. It will continue to prompt until the password entered is correct. The user's profile is saved in the OS's password manager.

* [retrieve-agol-credentials.py](https://github.com/cmosnick/python-snippets/blob/master/ArcGIS%20API%20for%20Python%20snippets/keyring%20with%20arcgis/retrieve-agol-credentials.py) will retrieve the user's profile form the password manager, and use it to authenticate with ArcGIS Online. Use this at the beginning of your script.

