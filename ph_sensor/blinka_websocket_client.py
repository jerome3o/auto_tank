from typing import List
import asyncio
import websockets
import json
import matplotlib.pyplot as plt
import numpy as np
import queue
from matplotlib.animation import FuncAnimation

address = "ws://rpi2:5678"

# Set up the plot

n_points = 100
fig, ax = plt.subplots()
x_data = np.arange(n_points)  # Adjust this to the desired number of data points
voltage_data = np.zeros(n_points)
line, = ax.plot(x_data, voltage_data)

# Set up the queue
adc_queue = queue.Queue()

# Update the plot with new data
def update_plot(adc_value: List[dict]):
    # get all new values
    new_values = [value["voltage"] for value in adc_value]
    # append to the data
    voltage_data[:-len(new_values)] = voltage_data[len(new_values):]
    voltage_data[-len(new_values):] = new_values

    line.set_ydata(voltage_data)
    ax.relim()
    ax.autoscale_view()
    plt.draw()

# Define the animation update function
def animate(i):
    new_values = []
    if not adc_queue.empty():
        while not adc_queue.empty():
            new_values.append(adc_queue.get())
        
        update_plot(new_values)  # Update with the desired channel value

# Set up the animation
ani = FuncAnimation(fig, animate, interval=50, blit=False)

# WebSocket listener
async def listen():
    async with websockets.connect(address) as websocket:
        while True:
            adc_values_str = await websocket.recv()
            adc_values = json.loads(adc_values_str)
            adc_queue.put(adc_values)
            # sleep a bit
            await asyncio.sleep(0.5)

# Show the plot and run the WebSocket listener in the same event loop
async def main():
    _listener_task = asyncio.create_task(listen())  

    # Use asyncio.ensure_future(listen()) for Python 3.4-3.6
    plt.show(block=False)

    while True:
        await asyncio.sleep(0.1)
        plt.pause(0.1)

asyncio.run(main())  # Use asyncio.get_event_loop().run_until_complete(main()) for Python 3.6

