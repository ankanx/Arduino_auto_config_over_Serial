import dev_handler

devHandler = dev_handler.dev_handler()

#devHandler.list_active_ports()
#print ""

devHandler.find_port(devHandler.mounted_Arduino_Uno.idVendor)

print "------------------------------------------------------"

#devHandler.list_device_info()

print "------------------------------------------------------"
#print devHandler.mounted_Realtek_wifi.idProduct
#print hex(devHandler.mounted_Arduino_Nano.idProduct)