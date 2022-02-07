import os
from oplab import Client
import json

# Create a client
c = Client()
email = os.getenv("EMAIL", default="youremail@gmail.com")
password = os.getenv("PASSWORD", default="yourpassword")

# Connect to Oplab
print("User data:", c.login(email, password))

# Get the default portifolio
default_portfolio_id = c.domain.get_default_portfolio_id()

# Get the trading account
trading_accounts = c.domain.get_trading_accounts()
print("trading accounts:", json.dumps(trading_accounts, indent=4, sort_keys=True))

# Create a robot structure
robot = {
    'trading_account_id': trading_accounts[0]['id'],
    'debug': 4,
    'mode': 'performance',
    'expire_date': '2022-02-15',
    'spread': 1170,
    'strategy': {
        'name': 'collar b3',
        'underlying': 'B3SA3',
        },
    'legs': [
        {
            'symbol': 'B3SA3',
            'target_amount': 100,
            'side': 'buy'
        },
        {
            'symbol': 'B3SAO125',
            'target_amount': 100,
            'side': 'buy'
        },
        {
            'symbol': 'B3SAC121',
            'target_amount': 100,
            'side': 'sell'
        }
    ]
}

# Create the robot
# Dry_run = True will really post the robot.
# Dry_run = False will not post the robot, but only printout what should be posted
data = c.domain.create_robot(default_portfolio_id, robot, dry_run=False)

# pretty print
print(json.dumps(data, indent=4, sort_keys=True))

