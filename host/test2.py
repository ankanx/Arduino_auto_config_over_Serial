import dev_handler

#devHandler = dev_handler.dev_handler()

#devHandler.list_active_ports()
#print ""
devhandler = dev_handler.dev_handler()

#devhandler.find_port(devhandler.mounted_Arduino_Uno.idVendor)
devhandler.list_active_ports()
devhandler.serach_ports()



print "------------------------------------------------------"

#devHandler.list_device_info()
devhandler.start()
print "bajsbajsbja"
print "------------------------------------------------------"
print "stuff"
#devhandler.list_device_info()
print "stuuffff22"
#print devHandler.mounted_Realtek_wifi.idProduct
#print hex(devHandler.mounted_Arduino_Nano.idProduct)