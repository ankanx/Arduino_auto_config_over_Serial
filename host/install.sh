#Install the Configuration Service dependencies
echo "Installing dependencies"
sudo apt-get update
sudo apt-get install git-core
sudo apt-get install python-dev
sudo apt-get install build-essential
sudo pip install pyserial
sudo pip install pyusb
echo "Finished installing dependencies"


#Install the Configuration Service
echo "Starting the configuration service install"
sudo cp device_config.service /lib/systemd/system/
echo ""
echo "Enabling sparc_htm service......"
echo ""
sudo systemctl enable device_config.service
echo ""
echo "Reloading systemctl daemon...."
echo ""
sudo systemctl daemon-reload
echo ""
echo "Starting sparc_htm service......"
echo ""
sudo systemctl start device_config.service
echo ""
echo "Checking sparc_htm service status......"
echo ""
sudo systemctl status device_config.service
echo ""
echo "Finished installing the configuration service"