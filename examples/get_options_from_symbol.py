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
options = c.market.get_options_from_symbol('PETR4')
print("Options:")
print(json.dumps(options, indent=4, sort_keys=True))
print("Fount options:", len(options))
