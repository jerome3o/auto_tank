import time
from ph_sensor.model import get_adc

adc = get_adc()

n_samples = 100

# print in a loop
while True:

    readings = adc.get_averaged_sensor_readings(n_samples, 0.01)

    for reading in readings.values():
        print(reading)
