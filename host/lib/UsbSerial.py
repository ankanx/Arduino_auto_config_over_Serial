import sys
import serial
import threading
import time

class USBclient():
    def connect(self,sPort,baud):
        try:
            print "Trying to connect to device..."
            self.serialConn = serial.Serial(sPort, baud)
            global serialConn
            serialConn = self.serialConn
            self.connectionMade()
            reading_service = reader()
            reading_service.start()
            reading_service.setName("Reading Thread")
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
        print 'Sending ', repr(data), ' to device.'
        serialConn.write(data)
        # .encode()?
        #serialConn.flush()


class reader(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
 
    
        # Main
        def run(self):
            print "Starting Reader"
            print ""
            # Continious port serch
            while True:
                time.sleep(1)
                print threading.currentThread().getName(), "Heartbeat"
                if serialConn.in_waiting > 0:
                    print "Serial responce: " ,serialConn.read_all()
                else:
                    print "No data in serial buffer"
