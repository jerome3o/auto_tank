import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c, gain=16)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0, ADS.P1)

# print in a loop
while True:
    print(chan.value, chan.voltage)
    time.sleep(0.01)
