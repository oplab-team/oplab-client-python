import os
from oplab import Client
import json

# Create a client
c = Client()
email = os.getenv("EMAIL", default="youremail@gmail.com")
password = os.getenv("PASSWORD", default="yourpassword")

# Connect to Oplab
print("User data:", c.login(email, password))

# Get all robots from default portifolio where state is "running"
# The state 11 is "running"
default_portfolio_id = c.domain.get_default_portfolio_id()
robots = c.domain.get_robots(default_portfolio_id, 11)

# Cancel all robots
for robot in robots:
    c.domain.cancel_robot(default_portfolio_id, robot['id'])
