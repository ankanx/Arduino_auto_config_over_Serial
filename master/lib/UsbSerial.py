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
            
        except:
            print "Connection failed!"
            print "Unexpected error:", sys.exc_info()[0]
            raise

    def connectionMade(self):
        print 'Arduino device: ', serialConn, ' is connected.'
        global reading_service
        reading_service = reader(True)
        reading_service.start()
        reading_service.setName("Reading Thread")
       

    def dataReceived(self,data):
        print 'USBclient.dataReceived called with:'
        print data

    def send(self,data):
        print 'Sending ', repr(data), ' to device.'
        serialConn.write(data)
        # .encode()?
        #serialConn.flush()

    def disconnect(self):
        print "disconnected"
        reading_service.disconnected()
        serialConn.close()
        print serialConn._checkClosed()


class reader(threading.Thread):
        def __init__(self,connected):
            threading.Thread.__init__(self)
            self.connected = connected
    
        # Main
        def run(self):
            print "Starting Reader"
            print self.connected
            # Continious port serch
            while self.connected:
                time.sleep(1)
                print threading.currentThread().getName(), "Heartbeat"
                if serialConn.in_waiting > 0:
                    print "Serial responce: " ,serialConn.read_all()
                else:
                    print "No data in serial buffer"

        def disconnected(self):
            time.sleep(0.5)
            self.connected = False