from multiprocessing import Process, Queue, Pipe, Lock, Value, Array
import os

def f(name):
	print "hello, ", name
	print "module name: ", __name__
	print "process id: ", os.getpid()

# Recieves a queue object
def f2(q):
	q.put([33, None, "hello"])

# Recieves a pipe object
def f3(conn):
	conn.send([33, None, "hello"])
	conn.close()

# Recieves a lock, number
def f4(lock, i):
	lock.acquire()
	print "here it is: {0}\npid: {1}".format(i, os.getpid())
	lock.release()


def f5(num, arr):
	num.value = 3.145926
	arr = reversed(arr)


if __name__ == '__main__':
	# Basic process spawning
	p = Process(target = f, args=("bob",))
	p.start()
	p.join()
	print "Parent process id: ", os.getpid()
	
	# Sharing objects between processes using Queue
	q = Queue()
	p = Process(target = f2, args=(q,))
	p.start()
	print q.get()
	p.join()

	#  Using Pipes
	parent_conn, child_conn = Pipe()
	p = Process(target=f3, args=(child_conn,))
	p.start()
	print parent_conn.recv()
	p.join()

	# Using locks for synchronization
	lock = Lock()
	for num in range(10):
		Process(target=f4, args=(lock, num)).start()

	# Sharing state (best to avoid)
	num = Value('d', 0.0)
	arr = Array('i', range(10))
	p = Process(target=f5, args=(num, arr))
	p.start()
	p.join()
	print num.value
	print arr[:]