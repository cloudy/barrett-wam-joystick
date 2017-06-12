import socket
import cPickle as pickle
import numpy
from config import MAPPING, HOST, PORT, WAMCONNECTED, HOMEPOS, MAXVAL

if WAMCONNECTED: 
    from WAMPy import *


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    nody = rospy.init_node("motion_control")

    
    conn, addr = s.accept()
    
    print 'Connected by', addr
    cur_position = HOMEPOS

    while True:
        data = conn.recv(131072)
        if not data: break
        
        data = pickle.loads(data)
    
        if WAMCONNECTED:
            live_wam_move(data[:MAPPING['AX4']], frequency=500)
    
        else:
            print 'AX0', data[MAPPING['AX0']]
            print 'AX1', data[MAPPING['AX1']]
            print 'AX2', data[MAPPING['AX2']]
            print 'AX3', data[MAPPING['AX3']]
            print 'AX4', data[MAPPING['AX4']]
            print 'AX5', data[MAPPING['AX5']]
    
    
       
    conn.close()



if __name__ == "__main__":
    main()