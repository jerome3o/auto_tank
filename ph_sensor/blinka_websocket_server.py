import asyncio
import websockets
import json
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c, gain=1)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0, ADS.P1)


def read_adc_values():
    return {
        "value": chan.value,
        "voltage": chan.voltage,
        "time": time.time(),
    }


async def serve(websocket, path):
    while True:
        adc_values = read_adc_values()
        await websocket.send(json.dumps(adc_values))
        await asyncio.sleep(0.05)


start_server = websockets.serve(serve, "0.0.0.0", 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
