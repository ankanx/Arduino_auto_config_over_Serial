import socket
import sys
import serial
import math
import io
import time
import sqlite3
import datetime
from enum import Enum

class configureFlag(Enum):
    UUID = 'U'
class settingsFlag(Enum):
    Name  = 'N'
    Type = 'T'

def listen():

    global sPort

    while True:
        print >>sys.stderr, '\nwaiting to receive message'
        
        sPort = '/dev/ttyACM0'
        ser = serial.Serial(sPort, 9600)

        print >>sys.stderr, 'received %s bytes from %s' 
        print >>sys.stderr, repr(data)

        if data:
            readMessage(data, sock, address)

def sendCmd(cmd,ser):
    ser.write(cmd)


def readMessage(sPort,ser,cmd):
    print repr(cmd)
    sendCmd(cmd,ser)

if __name__ == '__main__':
    listen()
