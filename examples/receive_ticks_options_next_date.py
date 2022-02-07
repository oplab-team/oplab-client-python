import os
from oplab import Client
import json

# Create a client
c = Client()
email = os.getenv("EMAIL", default="youremail@gmail.com")
password = os.getenv("PASSWORD", default="yourpassword")

# Connect to Oplab
print("User data:", c.login(email, password))

# Get options from a symbol
options = c.market.get_options_from_symbol('MGLU3')

# For each option, add to subscription list
subscribe_options = []
for option in options:
    if option["days_to_maturity"] <= 30:
        subscribe_options.append(option["symbol"])

# Define the call back to called when a new tick is received
def on_tick(df, message):
    print("Tick: ", message)

# Start receiving ticks
c.start_datafeed(subscribe_options, tick_callback=on_tick)
