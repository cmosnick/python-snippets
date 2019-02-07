import soils
import time
import multiprocessing as mp
import json


NUM_TESTS = 1

def write_to_file(times):
	ts = time.time()
	output_file = "test results/test_{0}.txt".format(str(ts))
	file = open(output_file, "w+")
	json.dump(times, file, sort_keys=True)
	file.close()


if __name__ == '__main__':

	times = {}
	max_procs = mp.cpu_count()
	print "Number of CPUs: {0}".format(max_procs)
	for i in range(max_procs):
		times [i+1] = []
		for x in range(NUM_TESTS):
			# Set up timing
			start = time.time()
			soils.go(i+1)
			end = time.time()
			t_elapsed = (end-start)
			print str(t_elapsed) + " seconds"
			times[i+1].append(t_elapsed)
	print times

	write_to_file(times)
