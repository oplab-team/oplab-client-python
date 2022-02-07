import os
from oplab import Client

# Create a client
c = Client()
email = os.getenv("EMAIL", default="youremail@gmail.com")
password = os.getenv("PASSWORD", default="yourpassword")

# Connect to Oplab
print("User data:", c.login(email, password))

# Print the portifolios
portifolios = c.domain.get_portfolios()
print("Portifolios:", portifolios)

# Use the API to find default portifolio
default_portfolio_id = c.domain.get_default_portfolio_id()
print("Default portfolio id:", default_portfolio_id)

# Print all strategies in the default portfolio
print("Portifolio strategies", c.domain.get_strategies(default_portfolio_id))



