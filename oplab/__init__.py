from datetime import datetime
import os
from oplab.errors import *

import requests


class Market:
    def __init__(self, client) -> None:
        self.client = client
    def url(self):
        return '%s%s'%(self.client.config['base_url'],'market')

class Domain:
    def __init__(self, client) -> None:
        self.client = client
        
    def url(self):
        return '%s%s'%(self.client.config['base_url'],'domain')

    def get_portfolio_orders(self, id, token = None):
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/portfolios/%d/orders' % (self.url(), id), headers = {'Access-Token': token})
        return r.json()

    def create_order(self, order, id, token = None):
        if (token is None):
            token = self.client.get_token()
        r = requests.post('%s/portfolios/%d/orders' % (self.url(), id), data = order, headers = {'Access-Token': token})
        return r.json()
    
    def update_balancing(self, balancing, id, token = None):
        if (token is None):
            token = self.client.get_token()
        r = requests.put('%s/portfolios/%d/balancings' % (self.url(), id), data = balancing, headers = {'Access-Token': token})
        return r.json()
    
    def get_portfolios(self, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/portfolios/' % self.url(), headers = {'Access-Token': token})
        return r.json()
    
    def get_portfolio(self, portfolio_id, token=None):
        if (portfolio_id is None):
            raise WrongParameterError
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/portfolios/%s' % (self.url(), portfolio_id), headers = {'Access-Token': token})
        return r.json()

    def get_historical_data(self, symbol, amount=None, _from= None, _to = None, resolution = '1d', fill = 'business_days', token = None):
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/charts/data/%s/%s?amount=%d&from=%s&to=%s&fill=%s' % (self.url(), symbol, resolution, amount if amount else '', _from.strftime('%Y%m%d%H%M') if _from else '', _to.strftime('%Y%m%d%H%M') if _to else '', fill), headers = {'Access-Token': token})
        return r.json()

class Quant:
    def __init__(self, client) -> None:
        self.client = client
    def url(self):
        return '%s%s'%(self.client.config['base_url'],'quant')

class Client:
    """
    Client class that implements the REST API as in: https://apidocs.oplab.com.br/
    ...

    Attributes
    ----------
    config: object
        Object with configuration regarding this client.
    version : str
        The API version. default: v3

    Methods
    -------
    login(email = None, password = None)
        Logs in to the API using the email and password.
    get_token()
        Returns the access-token from the auth object. Must be logged in.
    """
    
    def __init__(self, config=None, version = 'v3' ):
        self.config = config if config is not None else {
            'base_url': '%s%s/' % (os.getenv('HOST', default='https://api.oplab.com.br/'), version)
            }
        self.auth = {}
        self.is_logged = False
        self.market = Market(self)
        self.domain = Domain(self)
        self.quant= Quant(self)

    def login(self, email, password):
        r = requests.post('%sdomain/users/authenticate' % self.config['base_url'], {'email': email, 'password': password})
        self.auth = r.json()
        if (self.auth['access-token']):
            self.is_logged = True
            return(self.auth)
        raise WrongCredentialsError

    def get_token(self):
        if (self.is_logged):
            return self.auth['access-token']
        raise NotLoggedInError



    def get_options_positions(self, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.get('%sv2/positions' % self.config['base_url'], headers = {'Access-Token': token})
        return r.json()

    def get_stocks_positions(self, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.get('%sv2/portfolio' % self.config['base_url'], headers = {'Access-Token': token})
        return r.json()

    def get_options_analysis(self, symbol, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.get('%sv2/studies/%s' % (self.config['base_url'], symbol), headers = {'Access-Token': token})
        return r.json()

    def get_stock_ewma(self, symbol, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.get('%sv2/studies/%s' % (self.config['base_url'], symbol), headers = {'Access-Token': token})
        return r.json()['target']['ewma-current']
        
    def get_portfolio_orders(self, id, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.get('%sdomain/portfolios/%d/orders' % (self.config['base_url'], id), headers = {'Access-Token': token})
        return r.json()

    def create_order(self, order, id, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.post('%sdomain/portfolios/%d/orders' % (self.config['base_url'], id), data = order, headers = {'Access-Token': token})
        return r.json()
    
    def update_balancing(self, balancing, id, token = None):
        if (token is None):
            token = self.get_token()
        r = requests.put('%sdomain/portfolios/%d/balancings' % (self.config['base_url'], id), data = balancing, headers = {'Access-Token': token})
        return r.json()
