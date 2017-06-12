import socket
import cPickle as pickle
import numpy as np
import pygame
from config import MAPPING, HOST, PORT
import time

def deadband(realval, band):
    if realval < band:
        return 0.0
    return realval

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    done = None
    
    pygame.init()
    clock = pygame.time.Clock()
    pygame.joystick.init()
    deadbandval = 0.1

    while True:
        joystick_count = pygame.joystick.get_count()
        
        for event in pygame.event.get():
            pass
    
        for i in range(joystick_count):
    
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
    
            name = joystick.get_name()
            axes = joystick.get_numaxes()
            buttons = joystick.get_numbuttons()
            hats = joystick.get_numhats()
    
            js_vals = np.zeros((axes + buttons + hats,))
            
            for i in range( axes ):
                axis = joystick.get_axis( i )
                js_vals[i] = deadband(axis, deadbandval)
                
            for i in range( buttons ):
                button = joystick.get_button( i )
                js_vals[axes + i] = button
    
            #for i in range( hats ):
            #    hat = joystick.get_hat( i )
            #    js_vals[buttons + axes + i] = hat
    
        print js_vals
        js_packed = pickle.dumps(js_vals)
        s.send(js_packed)
    
        time.sleep(0.1)
        
    pygame.quit ()




if __name__ == "__main__":
    main()