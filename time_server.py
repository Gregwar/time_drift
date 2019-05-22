import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:8881')

while True:
    request = socket.recv()
    answer = str(time.time())
    socket.send_string(answer)