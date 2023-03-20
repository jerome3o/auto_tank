# auto_tank
Documentation and code for a project to get metrics and try automate the maintenance of a reef tank

Following are some recommendations from ChatGPT

# Fish Tank Instrumentation Project

## Topics to Learn

1. **Sensors and Actuators**
   - Understand how different sensors work (temperature, pH, etc.)
      - [How pH sensors work](https://in-situ.com/en/faq/water-quality-information/ph-faqs/how-do-ph-sensors-work)
      - [pH sensor purchased](https://www.aliexpress.com/item/1005004359552599.html?spm=a2g0o.order_detail.order_detail_item.4.2f02f19ct9c07W), was missing the ADC board, bought an [ADS1115](https://instantpanel.co.nz/product/ads1115-16-bit-adc---4-channel-with-programmable-gain-amplifier.html)
      - [Better one?](https://nz.rs-online.com/web/p/arduino-compatible-boards-kits/2163779)
   - Learn about common actuators (motors, pumps, heaters, etc.)

2. **Basic Electronics**
   - Learn about voltage, current, resistance, and Ohm's Law
   - Study the basics of circuits, including series and parallel connections
   - Understand how to read and interpret datasheets for components

3. **Analog-to-Digital Conversion (ADC)**
   - Learn about ADCs and how they convert analog signals to digital data
   - Understand the concepts of resolution, sampling rate, and quantization error
   - Get familiar with ADC modules available on Raspberry Pi or standalone ADC chips (e.g., ADS1115)

4. **Signal Conditioning**
   - Understand the basics of amplification, filtering, and isolation
   - Learn how to use operational amplifiers (op-amps) for signal conditioning
   - Study the use of passive filters (low-pass, high-pass, band-pass, and band-stop)

5. **Interfacing with Raspberry Pi**
   - Learn about the Raspberry Pi GPIO pins and their functions
   - Understand common communication protocols (I2C, SPI, UART, etc.)
   - Study the basics of programming the Raspberry Pi using Python, especially libraries like RPi.GPIO and smbus

6. **Power Management**
   - Learn about power supply requirements for your components (sensors, actuators, Raspberry Pi)
   - Study voltage regulators and how to use them in your project

7. **Data Acquisition and Logging**
   - Understand how to collect and store data from your sensors
   - Learn how to timestamp and log the data locally or remotely (e.g., using a database)

8. **Data Visualization and Analysis**
   - Learn how to visualize your data using Python libraries (e.g., Matplotlib, Plotly)
   - Understand basic statistical analysis techniques to interpret the data

9. **Control Systems**
   - Study the basics of control theory and its applications
   - Learn about different types of control systems (open-loop, closed-loop, PID, etc.)

10. **IoT and Remote Access**
   - Understand the basics of networking and communication protocols (e.g., MQTT)
   - Learn how to connect your project to the internet for remote monitoring and control

## Recommended Resources

- Raspberry Pi's official documentation (https://www.raspberrypi.org/documentation/)
- Adafruit Learning System (https://learn.adafruit.com/)
- SparkFun Electronics tutorials (https://learn.sparkfun.com/)
- YouTube channels like EEVblog, GreatScott!, and Andreas Spiess



