import sys
import numpy
import json


def get_stats(filename):
	try:
		file = open(filename)
	except Exception as e:
		print "Could not open file: {0}\n{1}".format(filename, e)
		exit()

	times = json.load(file)
	if "1" in times:
		base_mean = numpy.mean(times["1"])
	else:
		base_mean = None

	for key, values in times.iteritems():
		mean = numpy.mean(values)
		print "\n\nNumber of processes: {0}".format(key)
		if len(values) < 6:
			print "Times: {0}".format(values)
		print "Mean time: {0}".format( '%.2f' % mean)
		if base_mean:
			improvement = (mean - base_mean)/base_mean*100
			print "Time improvement: {0}% {1} in time".format( '%.2f' % abs(improvement),  "decrease" if improvement < 0 else "increase")
	# Print stats to file?


if __name__ == '__main__':
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	else:
		filename = "test results/test_1501776089.88.txt"
		# print "must provide filename"
		# exit()
	get_stats(filename)