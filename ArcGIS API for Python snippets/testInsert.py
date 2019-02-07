# Test the insertion of a simple feature into 
# an ArcGIS Online feature layer

import sys
import os
from arcgis.gis import GIS

def findLayerInItem(agolItem, layerName):
    for itemLayer in agolItem.layers:
            if layerName in itemLayer.properties.name:
                return itemLayer
    return None

def insertFeature():
    # ArcGIS Online Authentication
    print("...Authenticating with ArcGIS Online")
    agolURL = 'agolurl'
    agolUsername = 'username'
    agolPwd = 'password'

    gis = GIS(agolURL, agolUsername, agolPwd)
    print("...Connected to ArcGIS Online")

    # Find arcgis online item and layer
    itemId = config.get('ArcgisOnline', 'agolItemId')
    agolItem = gis.content.get(itemId)
    layerName = config.get('ArcgisOnline', 'agolLayerName')
    agolLayer = findLayerInItem(agolItem, layerName)


    # Create feature to insert
    insertFeature = {
        'attributes':
        {
            'foo': 'bar',
            'key': 'value',
        },
        'geometry':
        {
            'x': -8372854.089165498,
            'y': 4882472.522499578
        }
    }

    print(insertFeature)
    res = agolLayer.edit_features(adds=[insertFeature])
    print(res)

if __name__ == '__main__':
    insertFeature()
