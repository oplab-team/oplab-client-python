import os
from oplab import Client
import json

# Create a client
c = Client()
email = os.getenv("EMAIL", default="youremail@gmail.com")
password = os.getenv("PASSWORD", default="yourpassword")

# Connect to Oplab
print("User data:", c.login(email, password))

# Get robot from a portifolio where ID is 1864
default_portfolio_id = c.domain.get_default_portfolio_id()
data = c.domain.get_robot(default_portfolio_id, 3969)
print(json.dumps(data, indent=4, sort_keys=True))

