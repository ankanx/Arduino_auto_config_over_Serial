import sys
import serial
import UsbSerial
import time

test = UsbSerial.USBclient()
test.connect('/dev/ttyACM0',9600)
#test.connect('/dev/bus/usb/001/006',9600)
print "still running.."

print "Starting loop"
while True:
    time.sleep(1)
    test.send("test")