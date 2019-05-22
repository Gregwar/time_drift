import time
import zmq
import sys
import numpy as np

if len(sys.argv) < 2:
    print('Usage: time_client.pt [host]')
    exit()
host = sys.argv[1]

startTime = time.time()
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://'+host+':8881')

def measureOffset():
    offset = []
    # Sending 50 requests and averaging
    for x in range(50):
        start = time.time()
        socket.send_string('?')
        reply = float(socket.recv())
        end = time.time()
        avg = (start+end)/2.0
        offset.append(avg-reply)

    return np.median(offset)

base = measureOffset()
while True:
    offset = measureOffset()-base

    # Output is time since start, and drift of clock
    print('%f %.9f' % (time.time()-startTime, offset))
    sys.stdout.flush()
