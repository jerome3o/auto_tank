import time
import board
import busio
from Adafruit_ADS1x15.analog_in import AnalogIn
from Adafruit_ADS1x15.ads1x15 import ADS1115


# Initialize the I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the ADC object using the ADS1115 class.
adc = ADS1115(i2c)

# Create a single-ended input on channel A0.
chan = AnalogIn(adc, ADS1115.P0)

# Continuously print the voltage value.
while True:
    print("Channel A0 Voltage: {:.2f} V".format(chan.voltage))
    time.sleep(1)

