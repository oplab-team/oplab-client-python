from datetime import datetime
import os
from oplab.errors import *

import requests

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

    BASE_URL =  '%s/' % os.getenv('HOST', default='https://api.oplab.com.br/')
    
    def __init__(self, version = 'latest'):
      
        self.auth = {}
        self.is_logged = False

    def login(self, email, password):
        r = requests.post('%sv3/domain/users/authenticate' % Client.BASE_URL, {'email': email, 'password': password})
        self.auth = r.json()
        if (self.auth['access-token']):
            self.is_logged = True
            return(self.auth)
        raise WrongCredentialsError

    def get_token(self):
        if (self.is_logged):
            return self.auth['access-token']
        raise NotLoggedInError

    def get_portfolios(self, token=None):
        if (token is None):
            token = self.get_token()
        r = requests.get('%sv3/domain/portfolios/' % Client.BASE_URL, headers = {'Access-Token': token})
        return r.json()
    
    def get_portfolio(self, portfolio_id, token=None):
        if (portfolio_id is None):
            raise WrongParameterError
        if (token is None):
            token = self.get_token()
        r = requests.get('%sv3/domain/portfolios/%s' % (Client.BASE_URL, portfolio_id), headers = {'Access-Token': token})
        return r.json()

    def get_historical_data(self, symbol, amount=None, _from= None, _to = None, resolution = '1d', fill = 'business_days', token = None):
        if (token is None):
            token = self.get_token()
        r = requests.get('%sv3/domain/charts/data/%s/%s?amount=%d&from=%s&to=%s&fill=%s' % (Client.BASE_URL, symbol, resolution, amount if amount else '', _from.strftime('%Y%m%d%H%M') if _from else '', _to.strftime('%Y%m%d%H%M') if _to else '', fill), headers = {'Access-Token': token})
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
        
    def get_portfolio_orders(self, id, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.get('%sv3/domain/portfolios/%d/orders' % (Client.BASE_URL, id), headers = {'Access-Token': token})
        return r.json()

    def create_order(self, order, id, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.post('%sv3/domain/portfolios/%d/orders' % (Client.BASE_URL, id), data = order, headers = {'Access-Token': token})
        return r.json()
    
    def update_balancing(self, balancing, id, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.put('%sv3/domain/portfolios/%d/balancings' % (Client.BASE_URL, id), data = balancing, headers = {'Access-Token': token})
        return r.json()
