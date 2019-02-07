import arcpy
import multiprocessing
import os
import math

fields = ['SHAPE@AREA', 'MUSYM']
fc = workspace = u"C:\Data\SSURGO_2017_CONUS_polygons\SSURGO_2017_CONUS_polygons.gdb\MUPOLYGON_CONUS"


def function_do_something(range):
	# print "here: {0}".format(os.getpid())
	where = "{0} <= OBJECTID AND OBJECTID < {1}".format(range[0], range[1])
	soils = {}
	with arcpy.da.SearchCursor(fc, fields, where) as cursor:
		for row in cursor:
			name = row[1]
			area = row[0]
			if name in soils.keys():
				soils[name] += area
			else:
				soils[name] = area
	return soils


def collapse_results(soil_counts):
	counts_agg = {}
	for obj in soil_counts:
		for key, count in obj.items():
			if key in counts_agg.keys():
				counts_agg[key] += count
			else:
				counts_agg[key] = count
	return counts_agg


def go(num_processes):
	if num_processes <= 0:
		return

	workspace = u"C:\Data\SSURGO_2017_CONUS_polygons\SSURGO_2017_CONUS_polygons.gdb"
	arcpy.env.workspace = workspace

	start = 0
	num_features = int(arcpy.GetCount_management(fc)[0])
	# num_features = 200
	inc = int(math.ceil((num_features+num_processes) / num_processes))
	end = inc-1

	ranges = []
	while (start < num_features):
		rge = [start, end]
		start = start + inc
		end = end + inc
		ranges.append(rge)
	print ranges


	# Get fc "MUPOLYGON_CONUS"
	pool = multiprocessing.Pool(num_processes)
	soil_counts = pool.imap_unordered(function_do_something, (ranges))

	pool.close()
	pool.join()

	print collapse_results([count for count in soil_counts])
	# print("done")


if __name__ == '__main__':
	go(4)