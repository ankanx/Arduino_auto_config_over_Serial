import usb.core
import usb.util
import usb
import serial.tools.list_ports

#show device iformation
dev = usb.core.find(idVendor=0x2341, idProduct=0x0043)
if dev is None:
    #raise ValueError('Our device is not connected')
    print ""
    print "Target Device is not connected!"
    print ""
    print "Listing connected devices..."
    print "*****************************************************************"
    print usb.core.show_devices()
    devices = usb.core.find(find_all=True)
    for dev in devices:
        print ""
        print "------> " + dev.product
        print ""
        print dev._get_full_descriptor_str()
    print "*****************************************************************"
    
else:
    print "Connected a device.."
    print dev
    print "derp!"
    print usb.core.show_devices()
    print dev.get_active_configuration()
    print dev._get_full_descriptor_str()
    print usb.core.show_devices()
    test = usb.busses()
    print test
    print dev.bus
    print dev.__iter__
    print dev._langids

#List Active ports
print ""
print "Avaveble ports:"    
print serial.tools.list_ports.main()
#print serial.tools.list_ports.comports()
#print "Linux COM Ports Active:"
#print serial.tools.list_ports_linux.comports()
print ""

if serial.tools.list_ports.comports() != []:
    print "Found ports!"
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print p
        print p.manufacturer
        #match usb with serial tool serial_number
        print ""
        print p.serial_number
        print dev.serial_number
        print ""
        print p.usb_info()
        print p.subsystem
        print p.usb_description()
        print p.vid
        