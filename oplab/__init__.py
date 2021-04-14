import os
from datetime import datetime, timedelta
from oplab.v3.quant import Quant
from oplab.v3.domain import Domain
from oplab.v3.market import Market
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
