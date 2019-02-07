# Run 2 scenarios to convert lat/long into arcgis geometry objects using the arcgis geometry engine:
# - Convert 10 geometries 1 at a time
# - Convert 10 geometries as a batch in 1 request
# 
# Results:
# - Time for single geometries: 77.449588 s
# - Time for batch geometries:   6.457343 s
# 

import arcgis
from arcgis import GIS
import random
import time

def generateRandomLatLong(num=10):
    points = []
    for i in range(num):
        lat = random.uniform(-90, 90)
        lon = random.uniform(-180, 180)
        points.append({
            'y': lat,
            'x': lon,
        })

    return points


def main():
    # Get lat and long
    points = generateRandomLatLong(1000)
    print(points)

    # Connect to gis
    gis = GIS()

    # Convert in batch
    astarttime = time.time()
    allGeoms = arcgis.geometry.project(geometries=points, in_sr=4326, out_sr=3857)
    aendtime = time.time()
    print(allGeoms)

    # Convert one by one
    singleGeoms = []
    sstarttime = time.time()
    for i, point in enumerate(points):
        # convert form lat long to web mercator
        geom = arcgis.geometry.project(geometries=[points[i]], in_sr=4326, out_sr=3857)[0]
        singleGeoms.append(geom)
    sendtime = time.time()
    print(singleGeoms)


    # Compare order of elements
    for a, b in zip(singleGeoms, allGeoms):
        if (a != b):
            print("a does not equal b")
            return

    print("Time for single geometries: %f" % (sendtime - sstarttime))
    print("Time for all geometries:    %f" % (aendtime - astarttime))

if __name__ == '__main__':
    main()
