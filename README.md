# Sensordata-BME680
Python scripts for BME680 and Nextcloud Sensorlogger 


# rc.local
give execution right to the file 

add :

```
sudo -u pi mount /home/pi/ram/ && cd /home/pi/Bosch/bsec_bme680_linux/ && sudo -u pi ./bsec_bme680 > /home/pi/ram/bme280.log &

sudo -u pi python3 /home/pi/pSensordata-BME680.py &
```
prior ```exit 0```

# Sensordata-BME680.py
Declare the sensor in sensor data, see repo : https://github.com/alexstocker/sensorlogger

Edit and add ```cloud address```, ```login``` and ```app password``` 

# bme680.c 
Use this file to compile the driver from the repo : https://github.com/alexh-name/bsec_bme680_linux
