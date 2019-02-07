# Retrieve saved arcgis credentials from keyring

from arcgis.gis import GIS
import config

# Authenticate with ArcGIS Online
gis = GIS(profile=config.keyringProfile)
logging.info("Successfully logged in as: " + gis.properties.user.username)