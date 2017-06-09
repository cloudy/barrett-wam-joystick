import socket
import pickle
import numpy
from config import MAPPING, HOST, PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()

print 'Connected by', addr

while 1:
    data = conn.recv(4096)
    if not data: break
    
    data = pickle.loads(data)
    print data

conn.close()