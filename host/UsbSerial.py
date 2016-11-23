import sys
import serial


class USBclient():
    def connect(self,sPort,baud):
        try:
            print "Trying to connect to device..."
            self.serialConn = serial.Serial(sPort, baud)
            global serialConn
            serialConn = self.serialConn
            self.connectionMade()
        except:
            print "Connection failed!"
            print "Unexpected error:", sys.exc_info()[0]
            raise

    def connectionMade(self):
        print 'Arduino device: ', serialConn, ' is connected.'

    def sendCmd(self, cmd):
        self.serialConn.write(cmd)

    def dataReceived(self,data):
        print 'USBclient.dataReceived called with:'
        print data

    def send(self,data):
        print 'Seding ', data, ' to host.'
        serialConn.write(data)


