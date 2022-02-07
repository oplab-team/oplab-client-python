import os
from oplab import Client
import json

# Create a client
c = Client()
email = os.getenv("EMAIL", default="youremail@gmail.com")
password = os.getenv("PASSWORD", default="yourpassword")

# Connect to Oplab
print("User data:", c.login(email, password))

# Get all robots from default portifolio where state is 1 (finished)
default_portfolio_id = c.domain.get_default_portfolio_id()
data = c.domain.get_robots(default_portfolio_id, status=1)
print(json.dumps(data, indent=4, sort_keys=True))

