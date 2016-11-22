import usb
busses = usb.busses()
for bus in busses:
    devices = bus.devices
    for dev in devices:
        print "Device:", dev.filename
        print "  idVendor: %d (0x%04x)" % (dev.idVendor, dev.idVendor)
        print "  idProduct: %d (0x%04x)" % (dev.idProduct, dev.idProduct)