import os
from oplab import Client
import json

# Create a client
c = Client()
email = os.getenv("EMAIL", default="youremail@gmail.com")
password = os.getenv("PASSWORD", default="yourpassword")

# Connect to Oplab
print("User data:", c.login(email, password))

# Print assets in down trend
data = c.market.get_ranking_trend(limit_to=5, sort='asc')

# pretty print
print(json.dumps(data, indent=4, sort_keys=True))
