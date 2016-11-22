import sys
import serial
import datetime
from twisted.internet.serialport import SerialPort
from twisted.internet import reactor
serServ = None

class USBclient():
    def connectionMade(self):
        global serServ
        serServ = self
        print 'Arduino device: ', serServ, ' is connected.'

    def sendCmd(self, cmd):
        for byte in cmd:
            serServ.transport.write(chr(byte))
        #leaving all newlines for debug reasons
        #print cmd, ' - sent to Arduino.'

    def dataReceived(self,data):
        print 'USBclient.dataReceived called with:'
        print data

    def send(self,data):
        print 'Seding ', data, ' to host.'
        for byte in cmd:
            serServ.transport.write(chr(byte))


SerialPort(USBclient(), '/dev/ttyACM0', reactor, baudrate='9600')
reactor.run()
myArduino = USBclient()

