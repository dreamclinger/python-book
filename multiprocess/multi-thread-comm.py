from multiprocessing import Process, Queue
import os, time, random

def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value
if __name__=='__main__':
	# parent thread create Queue, then trans to child threads
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
	#since infinite loop, force terminate
    pr.terminate()
