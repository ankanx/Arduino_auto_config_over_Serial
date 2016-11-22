import sys
import serial


class USBclient():
    def connect(self,sPort,baud):
        try:
            print "Trying to connect to device..."
            #self.sPort = '/dev/ttyACM0'
            #self.ser = serial.Serial(sPort, 9600)
            self.ser = serial.Serial(sPort, baud)
        except:
            print "Connection failed!"
            print "Unexpected error:", sys.exc_info()[0]
            #raise

    def connectionMade(self):
        global serServ
        serServ = self
        print 'Arduino device: ', serServ, ' is connected.'

    def sendCmd(self, cmd):
        ser.write(cmd)
        #leaving all newlines for debug reasons
        #print cmd, ' - sent to Arduino.'

    def dataReceived(self,data):
        print 'USBclient.dataReceived called with:'
        print data

    def send(self,data):
        print 'Seding ', data, ' to host.'
        ser.write(data)


