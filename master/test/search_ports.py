import usb.core
import usb.util
import usb
import serial.tools.list_ports

#show device iformation
dev = usb.core.find(idVendor=0x2341, idProduct=0x0043)
wlan = usb.core.find(idVendor=0x7392, idProduct=0x7811)

# If no wlan
if wlan is None:
    
    print "No Wlan connected"

else:
    print "Wlan Connected"
    print wlan.product
    #print wlan.get_active_configuration()
    print wlan.manufacturer

# If arduino nano (Chinease)
if dev is None:
    dev = usb.core.find(idVendor=0x1a86, idProduct=0x7523)

# If no arduino at all
if dev is None:
    print "Failed to connect to any arduino"
else:
    #if dev.manufacturer
    #print dev.product
    print hex(dev.__getattribute__('idProduct'))
    print hex(dev.__getattribute__('idVendor'))

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
    print ""
    print ""
    print "Listing connected devices..."
    print "*****************************************************************"
    # get the full description of each connected device
    devicees = usb.core.find(find_all=True)
    for devs in devicees:
        print "dev :::::::::::::::::::"
        print devs._get_full_descriptor_str()
    
    
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
        