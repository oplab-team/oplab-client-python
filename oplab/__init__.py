import requests
from datetime import datetime
from oplab.errors import *

class Client:
    """
    Client class that represents the oplab api client

    ...

    Attributes
    ----------
    version : str
        The API version. This is not implemented as of yet. TODO

    Methods
    -------
    login(email = None, password = None)
        Logs in to the API using the email and password.
    get_token()
        Returns the access-token from the auth object. Must be logged in.
    get_historical_data(symbol = None, _from: datetime, _to = None, resolution = '1d', token = None)
        Gets a symbol's historical data. Must be logged in.
    get_options_positions()
        Gets user's options positions.
    get_stocks_positions()
        Gets user's stocks positions.
    get_options_analysis(symbol)
        Gets a symbols option analysis.
    get_stock_ewma(symbol = None)
        Gets a stock's ewma.
    """

    BASE_URL = 'https://api.oplab.com.br/'

    def __init__(self, version = 'latest'):
      
        self.auth = {}
        self.is_logged = False

    def login(self, email, password):
        r = requests.post('%sv2/users/authenticate' % Client.BASE_URL, {'email': email, 'password': password})
        self.auth = r.json()
        if (self.auth['access-token']):
            self.is_logged = True
            return(self.auth)
        raise WrongCredentialsError

    def get_token(self):
        if (self.is_logged):
            return self.auth['access-token']
        raise NotLoggedInError

    def get_historical_data(self, symbol, _from: datetime, _to = None, resolution = '1d', token = None):
        if (token is None):
            token = self.get_token()
        if not isinstance(_from, datetime):
            raise Exception('_from must be of type date.')
        r = requests.get('%sv2/charts/data/%s/%s?from=%s&to=%s' % (Client.BASE_URL, symbol, resolution, _from.strftime('%Y%m%d%H%M'), _to.strftime('%Y%m%d%H%M') if _to else ''), headers = {'Access-Token': token})
        return r.json()

    def get_options_positions(self, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.get('%sv2/positions' % Client.BASE_URL, headers = {'Access-Token': token})
        return r.json()

    def get_stocks_positions(self, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.get('%sv2/portfolio' % Client.BASE_URL, headers = {'Access-Token': token})
        return r.json()

    def get_options_analysis(self, symbol, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.get('%sv2/studies/%s' % (Client.BASE_URL, symbol), headers = {'Access-Token': token})
        return r.json()

    def get_stock_ewma(self, symbol, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.get('%sv2/studies/%s' % (Client.BASE_URL, symbol), headers = {'Access-Token': token})
        return r.json()['target']['ewma-current']

