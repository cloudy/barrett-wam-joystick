import socket
import pickle
import numpy as np
import pygame
from config import MAPPING, HOST, PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

done = None

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()
    
while True:
    joystick_count = pygame.joystick.get_count()
    
    for event in pygame.event.get():
        pass

    for i in range(joystick_count):

        js_vals = np.zeros((21,))

        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        name = joystick.get_name()
        axes = joystick.get_numaxes()
        buttons = joystick.get_numbuttons()
        hats = joystick.get_numhats()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            js_vals[i] = axis
            
        for i in range( buttons ):
            button = joystick.get_button( i )
            js_vals[axes + i] = button

        #for i in range( hats ):
        #    hat = joystick.get_hat( i )
        #    js_vals[buttons + axes + i] = hat

    print js_vals
    js_packed = pickle.dumps(js_vals)
    s.send(js_packed)

    clock.tick(20)
    
pygame.quit ()
