import asyncio
import websockets
import json
import matplotlib.pyplot as plt
import numpy as np
import queue
from matplotlib.animation import FuncAnimation

address = "ws://rpi2:5678"

# Set up the plot

n_points = 1000
fig, ax = plt.subplots()
x_data = np.arange(n_points)  # Adjust this to the desired number of data points
voltage_data = np.zeros(n_points)
line, = ax.plot(x_data, voltage_data)

# Set up the queue
adc_queue = queue.Queue()

# Update the plot with new data
def update_plot(adc_value):
    voltage_data[:-1] = voltage_data[1:]
    voltage_data[-1] = adc_value
    line.set_ydata(voltage_data)
    ax.relim()
    ax.autoscale_view()
    plt.draw()

# Define the animation update function
def animate(i):
    if not adc_queue.empty():
        adc_values = adc_queue.get()
        update_plot(adc_values[0])  # Update with the desired channel value

# Set up the animation
ani = FuncAnimation(fig, animate, interval=50, blit=False)

# WebSocket listener
async def listen():
    async with websockets.connect(address) as websocket:
        while True:
            adc_values_str = await websocket.recv()
            adc_values = json.loads(adc_values_str)
            adc_queue.put(adc_values)

asyncio.get_event_loop().run_until_complete(listen())
plt.show()

