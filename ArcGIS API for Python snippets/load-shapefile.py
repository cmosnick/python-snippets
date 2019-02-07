import arcpy
import os


shpFile = 'C:\\Users\\cmosnick\\Git Repos\\osd-building-footprints\\data\\Buildings\\buildings.shp'


arcpy.env.workspace = "C:\Data"
outputWorkspace = "C:\Data"
if not os.path.exists(os.path.join(outputWorkspace, "data.gdb")):
	arcpy.CreateFileGDB_management(outputWorkspace, "data.gdb")

print "loading shapefile into featureclass"
outputFile = os.path.join(*[arcpy.env.workspace, "data.gdb", "buildings"])
buildings = arcpy.CopyFeatures_management(shpFile, outputFile)

