import os
from oplab import Client
import json

# Create a client
c = Client()
email = os.getenv("EMAIL", default="youremail@gmail.com")
password = os.getenv("PASSWORD", default="yourpassword")

# Connect to Oplab
print("User data:", c.login(email, password))

# Get quotes and details from a symbol
print("PETR4 quote:")
data = c.market.get_stock('PETR4')
print(json.dumps(data, indent=4, sort_keys=True))
