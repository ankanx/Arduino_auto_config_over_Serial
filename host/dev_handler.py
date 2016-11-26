import usb.core
import usb.util
import usb
import serial.tools.list_ports
import threading
import time
import sys
import serial
import lib.UsbSerial

class Arduino_Uno():
    
    def __init__(self):
        self.idVendor = 0x2341
        self.idProduct = 0x0043

class Arduino_Nano():

    def __init__(self):
        self.idVendor = 0x1a86
        self.idProduct = 0x7523
    
class Realtek_802_11n():

    def __init__(self):
        self.idVendor = 0x7392
        self.idProduct = 0x7811

class dev_handler(threading.Thread):
    
    # Initiate the dev handler
    def __init__(self):
        threading.Thread.__init__(self)
        self.mounted_Arduino_Uno = Arduino_Uno()
        self.mounted_Arduino_Nano = Arduino_Nano()
        self.mounted_Realtek_wifi = Realtek_802_11n()
        global mounted_Arduino_Uno
        global mounted_Arduino_Nano
        global mounted_Realtek_wifi
        mounted_Arduino_Uno = self.mounted_Arduino_Uno
        mounted_Arduino_Nano = self.mounted_Arduino_Nano
        mounted_Realtek_wifi = self.mounted_Realtek_wifi

    def run(self):
        print "Starting Devhandler"
        print ""
        while True:
            time.sleep(1)
            print "threading"
            self.serach_ports()


    # List the connected devices
    def list_device_info(self):
        devs = usb.core.find(find_all=True)
        counter = 1
        for dev in devs:
            print ""
            print "Dev " ,counter
            # In case iProduct could not be loaded
            try:
                print dev.product
            except:
                print "could not find iProduct description"
            print ""
            print dev._get_full_descriptor_str()
            counter = counter +1

    # List the active COM ports
    def list_active_ports(self):
        print "Listing Active Ports"
        print ""
        print serial.tools.list_ports.main()
    
    # Find a specific port given a vendor
    def find_port(self,idVendor):
        print "Searching for match"
        print ""
        ports = list(serial.tools.list_ports.comports())
        match = False
        for port in ports:
            if hex(port.vid) == hex(idVendor):
                print "Found Match at port:", port.device
                print "idVendor: ", hex(port.vid)
                print "idProduct: ", hex(port.pid)
                print "Serial_Number: ", port.serial_number
                match = True
        if match == False:
            print "Could not find a match"

    # Serch for active ports and print info
    def serach_ports(self):
        print "Seraching ports......"
        print ""
        ports = list(serial.tools.list_ports.comports())
        counter = 0
        if ports == []:
            print "No Active Ports 2"
        if ports is None:
            print "No Active Ports!"
        else:
            for port in ports:
                print ""
                if port.pid == mounted_Arduino_Uno.idProduct:
                    print "Is a sertified Arduino Uno - Starting configuration"
                    conf_thread = configure_device(port.device)
                    conf_thread.start()
                elif port.pid == mounted_Arduino_Nano.idProduct:
                    print "Is a sertified Arduino Nano"
                    conf_thread = configure_device(port.device)
                    conf_thread.start()
                elif port.pid == mounted_Realtek_wifi.idProduct:
                    print "Is a sertified Realtek_802_11n"
                else:
                    print "Device is not a sertified device"    
                counter = counter +1
                print "Active port nr: ", counter
                print "_____________________________________________________________________"
                print "Hardware ID: ", port.hwid
                print "Device: ", port.device
                print "Device path:", port.device_path
                print "Interface: ", port.interface
                print "Location: ", port.location
                print "Manifacturer: ", port.manufacturer
                print "Name: ", port.name
                print "Product id: ", hex(port.pid)
                print "Product: ", port.product
                print "Serial_Number: ", port.serial_number
                print "Subsystem: ", port.subsystem
                print "Device path: ", port.usb_device_path
                print "Vendor ID: " , hex(port.vid)
                print "Description: ", port.description
                print "_____________________________________________________________________"
            
            
# Threaded configuration            
class configure_device (threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        

    def run(self):
        print "Starting the config thread"
        data = "stuff"
        self.configure(self.port,data)
        print "Configuration Thread Exiting"

     # Configure a serial connected device
     # Standard baudrate is 9600
    def configure(self,port,data):
        baud = 9600
        device = lib.UsbSerial.USBclient()
        print "Connecting to " + port
        try:
            device.connect(port,baud)
            device.send(data)
            print "Succeeded to configure device"           
        except:
            print "Error configuring Device"

            
            # shows the (www.arduino.cc statement)
            #print port.manufacturer