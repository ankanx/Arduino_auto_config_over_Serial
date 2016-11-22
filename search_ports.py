import usb.core
import usb.util
import usb
import serial.tools.list_ports

#show device iformation
dev = usb.core.find(idVendor=0x2341, idProduct=0x0043)
if dev is None:
    raise ValueError('Our device is not connected')
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

#List actual ports    
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print p