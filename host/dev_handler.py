import usb.core
import usb.util
import usb
import serial.tools.list_ports



class Arduino_Uno():
    
    def __init__(self):
        self.idVendor = 0x2341
        self.idProduct = 0x0043

    def get_idVendor(self):
        return self.idVendor


class Arduino_Nano():

    def __init__(self):
        self.idVendor = 0x1a86
        self.idProduct = 0x7523
    
class Realtek_802_11n():

    def __init__(self):
        self.idVendor = 0x7392
        self.idProduct = 0x7811

class dev_handler():
    
    # Initiate the dev handler
    def __init__(self):
        self.mounted_Arduino_Uno = Arduino_Uno()
        self.mounted_Arduino_Nano = Arduino_Nano()
        self.mounted_Realtek_wifi = Realtek_802_11n()
        global mounted_Arduino_Uno


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
        
    def find_port(self,idVendor):
        print "Searching for match"
        print ""
        ports = list(serial.tools.list_ports.comports())
        match = False
        for port in ports:
            if hex(port.vid) == hex(idVendor):
                print "Found Match at port:", port.device
                print "idVendor:", hex(port.vid)
                print "idProduct", hex(port.pid)
                match = True
        
        if match == False:
            print "Could not find a match"



#            try:
#                print port.__getattribute__('idProduct')
#            except:
#                print "Could not find idProduct"
#            try:
#                print port.__getattribute__('idVendor')
#            except:
#                print "Could not find idVendor"
            
#    print hex(dev.__getattribute__('idProduct'))
#    print hex(dev.__getattribute__('idVendor'))

#   print usb.core.show_devices()
 
#List Active ports
#print ""
#print "Avaveble ports:"    
#print serial.tools.list_ports.main()
#print serial.tools.list_ports.comports()
#print "Linux COM Ports Active:"
#print serial.tools.list_ports_linux.comports()


#if serial.tools.list_ports.comports() != []:
#    print "Found ports!"
#    ports = list(serial.tools.list_ports.comports())
#    for p in ports:
#        print p
#        print p.manufacturer
#        #match usb with serial tool serial_number
#        print ""
#        print p.serial_number
#        print dev.serial_number
#        print ""
#        print p.usb_info()
#        print p.subsystem
#        print p.usb_description()
#        print p.vid
        