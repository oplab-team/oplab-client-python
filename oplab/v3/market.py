from datetime import datetime, timedelta
import requests
from oplab.errors import WrongParameterError


class Market:
    def __init__(self, client) -> None:
        self.client = client

    def historical_options(self, symbol, start=datetime.strftime(datetime.today() - timedelta(days=1), '%Y-%m-%d'), to=datetime.strftime(datetime.today() - timedelta(days=1), '%Y-%m-%d'), token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/historical/options/%s/%s/%s' %
                         (self.url(), symbol, start, to), headers={'Access-Token': token})
        return r.json()

    def get_historical_data(self, symbol, amount=None, _from=None, _to=None, resolution='1d', fill='business_days', token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/historical/%s/%s?amount=%d&from=%s&to=%s&fill=%s' % (self.url(), symbol, resolution, amount if amount else '',
                         _from.strftime('%Y%m%d%H%M') if _from else '', _to.strftime('%Y%m%d%H%M') if _to else '', fill), headers={'Access-Token': token})
        return r.json()

    def url(self):
        return '%s%s' % (self.client.config['base_url'], 'market')

    def get_options_from_symbol(self, underlying_symbol = None, token=None):
        '''
        Get options from symbol
        This is a helper function to get options from underlying_symbol
        '''
        if (underlying_symbol is None):
            raise WrongParameterError
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/options/%s' % (self.url(), underlying_symbol), headers={'Access-Token': token})
        return r.json()

    def get_stock(self, symbol = None, token=None):
        '''
        Get Stock details based on symbol
        '''
        if (symbol is None):
            raise WrongParameterError
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/stocks/%s' % (self.url(), symbol), headers={'Access-Token': token})
        return r.json()

    def get_ranking_trend(self, limit_to = 20, sort = "asc", volume = 10000000, days = 90, token=None):
        '''
        Get Ranking Trend based on m9 and m21
        limit_to: number of items to return
        sort: asc or desc
        volume: volume of the stock
        days: number of days
        '''
        if (limit_to is None):
            raise WrongParameterError
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/statistics/ranking/m9_m21?&limit=%d&sort=%s&financial_volume_start=%d&days=%d'
                        % (self.url(), limit_to, sort, volume, days), headers={'Access-Token': token})
        return r.json()
