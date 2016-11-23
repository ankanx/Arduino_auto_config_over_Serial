import usb.core

dev = usb.core.find(idVendor=0x2341, idProduct=0x0043)
if dev is None:
    raise ValueError('Our device is not connected')
else:
    print "Connected a device.."
    print dev
