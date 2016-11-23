import usb.core
import usb.util

dev = usb.core.find(find_all=True)

# get next item from the generator
d = dev.next() 
print d.get_active_configuration()