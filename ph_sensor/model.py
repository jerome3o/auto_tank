import time
from typing import Dict
from pydantic import BaseModel
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS
import board
import busio

_PH_NAME = "pH Sensor"
_TEMPERATURE_NAME = "Temperature Sensor"


class AdcSensorReading(BaseModel):
    voltage: float
    count: int
    time: float

    @classmethod
    def from_analog_in(cls, analog_in: AnalogIn):
        return cls(
            voltage=analog_in.voltage,
            count=analog_in.value,
            time=time.time(),
        )


# TODO(j.swannack): Don't hard code, add this as config
def load_sensors() -> Dict[str, AnalogIn]:
    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c, gain=1, mode=ADS.Mode.CONTINUOUS)

    # Create single-ended input on channel 0
    ph = AnalogIn(ads, ADS.P0, ADS.P1)
    temperature = AnalogIn(ads, ADS.P2)

    return {
        _PH_NAME: ph,
        _TEMPERATURE_NAME: temperature,
    }


class Adc:
    def __init__(self, sensors: Dict[str, AnalogIn]):
        self.sensors = sensors

    def get_sensor_readings(self) -> Dict[str, AdcSensorReading]:
        return {
            name: AdcSensorReading.from_analog_in(sensor)
            for name, sensor in self.sensors.items()
        }

    def get_averaged_sensor_readings(
        self, 
        n_samples: int,
        sleep_time: int,
    ) -> Dict[str, AdcSensorReading]:
        readings = []
        for i in range(n_samples):
            readings.append(self.get_sensor_readings())
            time.sleep(sleep_time)

        averaged_readings = {}
        for name in self.sensors.keys():
            voltage = 0
            count = 0
            for reading in readings:
                voltage += reading[name].voltage
                count += reading[name].count
            averaged_readings[name] = AdcSensorReading(
                voltage=voltage / n_samples,
                count=count / n_samples,
                time=time.time(),
            )

        return averaged_readings


def get_adc():
    return Adc(load_sensors())

