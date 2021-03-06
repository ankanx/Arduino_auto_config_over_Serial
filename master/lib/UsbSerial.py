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
        print "disconnecting"
        print "check if open", serialConn.isOpen()
        reading_service.disconnected()
        serialConn.flush()
        serialConn.close()
        print "Is serial open",serialConn.isOpen()


class reader(threading.Thread):
        def __init__(self,connected_local):
            threading.Thread.__init__(self)
            self.connected = connected_local
            #global connected
            #connected = self.connected
        # Main
        def run(self):
            print "Starting Reader"
            # Continious port serch
            while self.connected:

                #print "readingloop :",connected
                print "readingloop :",self.connected
                time.sleep(2)
                print threading.currentThread().getName(), "Heartbeat"
                try:
                    print "serial inw: ",serialConn.inWaiting()
                    if serialConn.in_waiting > 0:
                        print "Readline:",serialConn.readline()
                        print "Serial responce: " ,serialConn.read_all()
                    else:
                        print "No data in serial buffer"
                        print "readline:",serialConn.readline()
                except:
                    print "Serial Read failed! probably becouse of dismounting"
                    print "cycle done"
            print "----------------------should kill reader"


        def disconnected(self):
            #connected = False
            self.connected = False
            print "connected set to false!"