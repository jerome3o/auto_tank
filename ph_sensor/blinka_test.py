import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c, gain=2, mode=ADS.Mode.CONTINUOUS)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P2, ADS.P3)


n_samples = 10

# print in a loop
while True:

    voltage = 0
    for i in range(n_samples):
        voltage += chan.voltage
        time.sleep(0.01)

    voltage /= n_samples
    print(f"{voltage:0.3f}")
