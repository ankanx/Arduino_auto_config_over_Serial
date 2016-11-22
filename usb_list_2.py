#!/usr/bin/env python
# fstick.py

import usb.core
import usb.util
import sys
 
# find device
devs = usb.core.find(find_all=True)

for dev in devs:
   for cfg in dev:
      for intf in cfg:
         print 'Bus %03x,Device %03x | %04x:%04x - (%d) ... bDeviceClass %02x , bInterfaceClass %02x' % (dev.bus, dev.address, dev.idVendor, dev.idProduct, dev.bNumConfigurations, dev.bDeviceClass, intf.bInterfaceClass)
         if dev.bDeviceClass == 0 and intf.bInterfaceClass == 8 :
            print 'Bus %03x,Device %03x | %04x:%04x' % (dev.bus, dev.address, dev.idVendor, dev.idProduct)