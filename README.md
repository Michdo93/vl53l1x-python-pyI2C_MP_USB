# vl53l1x-python

Python library for the VL53L1X Laser Ranger with the I2C-MP-USB, an USB to I²C interface.

https://shop.pimoroni.com/products/vl53l1x-breakout

https://www.fischl.de/i2c-mp-usb/

https://github.com/EmbedME/pyI2C_MP_USB

# Installing

```
sudo pip install git+https://github.com/EmbedME/pyI2C_MP_USB
sudo pip install git+https://github.com/Michdo93/vl53l1x-python-pyI2C_MP_USB
```

# Uninstalling

```
sudo pip uninstall i2c-mp-usb-1.2
sudo pip uninstall vl53l1x
```

# Usage

```
#!/usr/bin/python3
import VL53L1X

class ToFVL53L1X(object):

    def __init__(self):
        self.address = 0x29

        # 1 = Short Range, 2 = Medium Range, 3 = Long Range 
        self.range = 1

        self.tof = VL53L1X.VL53L1X(i2c_bus=0, i2c_address = self.address)

    def start_sensor(self):
        self.tof.open()
        self.tof.start_ranging(self.range)

    def stop_sensor(self):
        self.tof.stop_ranging()
        
    def set_range(self, range):
        if range == "short":
            self.range = 1
        elif range == "medium":
            self.range = 2
        else:
            self.range = 3

        self.tof.stop_ranging()
        self.tof.start_ranging(self.range)

    def get_range(self):
        if self.range == 1:
            currentRange = "short"
        elif self.range == 2:
            currentRange = "medium"
        else:
            currentRange = "long"

        return currentRange

    def get_distance(self):
        distance = 0.0
        distance = self.tof.get_distance() * 0.1 # mm to cm conversion

        if distance >= 0:
            return distance
        else:
            return -1
          
if __name__ == "__main__":
    tof = ToFVL53L1X()
    tof.start_sensor()
    tof.set_range("short")
    
    while True:
        distance = float(tof.get_distance())
        
        print(distance)
```

See examples for more advanced usage.

# Troubleshooting

With `dmesg` you should get something like the following:

```
[19414.940598] usb 2-2.1: new full-speed USB device number 7 using uhci_hcd
[19415.265551] usb 2-2.1: New USB device found, idVendor=0403, idProduct=c631, bcdDevice= 1.01
[19415.265557] usb 2-2.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[19415.265558] usb 2-2.1: Product: I2C-MP-USB
[19415.265559] usb 2-2.1: Manufacturer: www.fischl.de
[19415.265560] usb 2-2.1: SerialNumber: 131ECCAC
[19415.535423] i2c-tiny-usb 2-2.1:1.0: version 1.01 found at bus 002 address 007
[19415.541033] i2c i2c-0: connected i2c-tiny-usb device
[19415.541475] usbcore: registered new interface driver i2c-tiny-usb
[19543.802310] usbcore: deregistering interface driver i2c-tiny-usb
[24133.198755] usb 2-2.1: USB disconnect, device number 7
```

If you receive following error message

```
usb1.USBErrorBusy: LIBUSB_ERROR_BUSY [-6]
```

please make sure that the kernel module is not loaded and the python library can access it:

```
sudo rmmod i2c-tiny-usb
```

With `sudo i2cdetect -y 0` you should see the sensor:

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- 29 -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- -- 
```
