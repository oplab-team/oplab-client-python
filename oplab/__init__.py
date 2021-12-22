import os
from datetime import datetime, timedelta
from oplab.v3.quant import Quant
from oplab.v3.domain import Domain
from oplab.v3.market import Market
from oplab.v3.datafeed import Datafeed
from oplab.errors import *

import requests


class Client:
    """
    Client class that implements the REST API as in: https://apidocs.oplab.com.br/
    ...

    Attributes
    ----------
    config: object
        Object with configuration regarding this client.

    Methods
    -------
    login(email = None, password = None)
        Logs in to the API using the email and password.
    get_token()
        Returns the access-token from the auth object. Must be logged in.
    start_datafeed(ticks, tick_callback = None, order_callback = None, robot_callback = None, system_callback = None)
        Starts the datafeed and never returns.
    """

    def __init__(self, config=None):
        self.config = config if config is not None else {
            'base_url': '%s%s/' % (os.getenv('HOST', default='https://api.oplab.com.br/'), 'v3')
        }
        self.auth = {}
        self.is_logged = False
        self.market = Market(self)
        self.domain = Domain(self)
        self.quant = Quant(self)

    def login(self, email, password):
        r = requests.post('%sdomain/users/authenticate' %
                          self.config['base_url'], {'email': email, 'password': password})
        self.auth = r.json()
        if (self.auth['access-token']):
            self.is_logged = True
            return(self.auth)
        raise WrongCredentialsError

    def get_token(self):
        if (self.is_logged):
            return self.auth['access-token']
        raise NotLoggedInError

    def start_datafeed(self, ticks, tick_callback = None, order_callback = None, robot_callback = None, system_callback = None):
        """
        Starts the datafeed and never returns

        Parameters
        ----------
        ticks: array of instruments ['PETR4', 'VALE3'],
            The symbols of ticks to be received.
        tick_callback: function
            Callback function for ticks.
        order_callback: function
            Callback function for orders.
        robot_callback: function
            Callback function for robots.
        system_callback: function
            Callback function for system.
        """
        if (self.is_logged):
            df_url = self.auth['endpoints'][0]
            df_token = self.auth['datafeed-access-token']
            self.datafeed = Datafeed(df_url, df_token, ticks, tick_callback, order_callback, robot_callback, system_callback)
            self.datafeed.start()
        raise NotLoggedInError
