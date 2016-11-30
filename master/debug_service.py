import dev_handler
import time
import threading
#devHandler = dev_handler.dev_handler()

#devHandler.list_active_ports()
#print ""
devhandler = dev_handler.dev_handler()

#devhandler.find_port(devhandler.mounted_Arduino_Uno.idVendor)




print "------------------------------------------------------"

#devHandler.list_device_info()
devhandler.start()
devhandler.setName("Device Handler Thread")
#print "bajsbajsbja"
print "------------------------------------------------------"
#print "stuff"
#devhandler.list_device_info()
#print "stuuffff22"
#print devHandler.mounted_Realtek_wifi.idProduct
#print hex(devHandler.mounted_Arduino_Nano.idProduct)
while True:
    time.sleep(1)
    print threading.currentThread().getName(), "Heartbeat"
