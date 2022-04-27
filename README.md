# vl53l1x-python

Python library for the VL53L1X Laser Ranger with the I2C-MP-USB, an USB to I²C interface.

https://shop.pimoroni.com/products/vl53l1x-breakout

https://www.fischl.de/i2c-mp-usb/

https://github.com/EmbedME/pyI2C_MP_USB

# Installing

```
pip install git+https://github.com/EmbedME/pyI2C_MP_USB
sudo pip install git+https://github.com/Michdo93/vl53l1x-python-pyI2C_MP_USB
```

# Usage

```python
import VL53L1X

# Open and start the VL53L1X sensor.
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open()

# Optionally set an explicit timing budget
# These values are measurement time in microseconds,
# and inter-measurement time in milliseconds.
# If you uncomment the line below to set a budget you
# should use `tof.start_ranging(0)`
# tof.set_timing(66000, 70)

tof.start_ranging(1)  # Start ranging
                      # 0 = Unchanged
                      # 1 = Short Range
                      # 2 = Medium Range
                      # 3 = Long Range

# Grab the range in mm, this function will block until
# a reading is returned.
distance_in_mm = tof.get_distance()

tof.stop_ranging()
```

See examples for more advanced usage.
