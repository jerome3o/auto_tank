import asyncio
import websockets
import json
import time
import board
import math
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


n_samples = 10
sample_rate = 50

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c, gain=1, mode=ADS.Mode.CONTINUOUS)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)


async def serve(websocket, path):
    while True:
        try:
            readings = []
            for i in range(n_samples):
                readings.append(chan.voltage)
                time.sleep(0.01)

            mean = sum(readings) / len(readings)
            variance = sum([((x - mean) ** 2) for x in readings]) / len(readings)
            min_voltage = min(readings)
            max_voltage = max(readings)

            data = {
                "mean": mean,
                "variance": variance,
                "min": min_voltage,
                "max": max_voltage,
                "time": time.time(),
            }

            # print data in single line
            print(
                f"{data['mean']:0.3f} V, "
                f"{data['variance']:0.3f} V, "
                f"{data['min']:0.3f} V, "
                f"{data['max']:0.3f} V, "
                f"{data['time']:0.3f} s"
            )

            await websocket.send(json.dumps(data))

        except Exception as e:
            print(e)


start_server = websockets.serve(serve, "0.0.0.0", 5678)

# start the server on the main thread
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
