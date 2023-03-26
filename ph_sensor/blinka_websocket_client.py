import time
from typing import List
import asyncio
import websockets
import json
import matplotlib.pyplot as plt
import numpy as np
import queue
from matplotlib.animation import FuncAnimation

address = "ws://rpi2:5678"

# # Example data
# {
#     "mean": mean,
#     "variance": variance,
#     "min": min_voltage,
#     "max": max_voltage,
#     "time": time.time(),
# }

# Set up the plot

n_points = 100
fig, ax = plt.subplots()

_current_time = time.time()

data = {
    "mean": np.zeros(n_points),
    "variance": np.zeros(n_points),
    "min": np.zeros(n_points),
    "max": np.zeros(n_points),
    "time": np.full(n_points, _current_time),
}

lines = {
    key: ax.plot(data["time"], data[key], label=key)[0]
    for key in data.keys() if key != "time"
}


# Set up the queue
adc_queue = queue.Queue()

# Update the plot with new data
def update_plot(adc_value: List[dict]):
    
    for key in data.keys():
        # get all new values
        new_values = [value[key] for value in adc_value]
        # append to the data
        data[key][:-len(new_values)] = data[key][len(new_values):]
        data[key][-len(new_values):] = new_values


    for key in lines.keys():
        lines[key].set_data(data["time"], data[key])

    ax.relim()
    ax.autoscale_view()


def init_plot():
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Voltage (V)")
    ax.legend()

    return lines.values()


# Define the animation update function
def animate(i):
    new_values = []
    if not adc_queue.empty():
        while not adc_queue.empty():
            new_values.append(adc_queue.get())
        
        update_plot(new_values)  # Update with the desired channel value

# Set up the animation
ani = FuncAnimation(fig, animate, interval=100, blit=False, init_func=init_plot)

# WebSocket listener
async def listen():
    async with websockets.connect(address) as websocket:
        while True:
            print("Waiting for data...", end=" ")
            adc_values_str = await websocket.recv()
            adc_values = json.loads(adc_values_str)
            print("Received: ", len(adc_values), time.time())
            adc_queue.put(adc_values)
            # sleep a bit
            await asyncio.sleep(0.05)

# Show the plot and run the WebSocket listener in the same event loop
async def main():
    _listener_task = asyncio.create_task(listen())  

    # Use asyncio.ensure_future(listen()) for Python 3.4-3.6
    plt.show(block=False)

    while True:
        await asyncio.sleep(0.1)
        plt.pause(0.1)

asyncio.run(main())  # Use asyncio.get_event_loop().run_until_complete(main()) for Python 3.6

