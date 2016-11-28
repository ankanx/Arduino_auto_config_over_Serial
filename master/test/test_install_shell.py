from subprocess import call
call(["sudo", "apt-get", "update"])
print ""
call(["sudo", "apt-get", "install","python-dev"])
print ""
call(["sudo", "pip", "install" ,"pyusb"])
print ""
call(["sudo", "pip", "install" ,"pyserial"])