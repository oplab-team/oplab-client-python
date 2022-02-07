import os
from oplab import Client

import asyncio
import json
import websockets

# Create a client
c = Client()
email = os.getenv("EMAIL", default="youremail@gmail.com")
password = os.getenv("PASSWORD", default="yourpassword")

# Connect to Oplab
print("User data:", c.login(email, password))

# Define methods to be called when a message is received
def on_tick(df, message):
    print("Tick: ", message)

def on_order(df, message):
    print("Order: ", message)

def on_robot(df, message):
    print("Robot: ", message)

def on_system(df, message):
    print("System: ", message)

# Start the datafeed
c.start_datafeed(['PETR4'], tick_callback=on_tick, order_callback=on_order, robot_callback=on_robot, system_callback=on_system)

