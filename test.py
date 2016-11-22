import sys
import serial
import UsbSerial

test = UsbSerial.USBclient()
test.connect('/dev/ttyACM0',9600)
print "still running tho"