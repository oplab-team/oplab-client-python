from oplab.errors import WrongParameterError
import requests


class Domain:
    def __init__(self, client) -> None:
        self.client = client

    def url(self):
        return '%s%s' % (self.client.config['base_url'], 'domain')

    def get_portfolio_orders(self, id, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/portfolios/%d/orders' %
                         (self.url(), id), headers={'Access-Token': token})
        return r.json()

    def create_order(self, order, id, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.post('%s/portfolios/%d/orders' % (self.url(), id),
                          data=order, headers={'Access-Token': token})
        return r.json()

    def update_balancing(self, balancing, id, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.put('%s/portfolios/%d/balancings' % (self.url(), id),
                         data=balancing, headers={'Access-Token': token})
        return r.json()

    def get_portfolios(self, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/portfolios/' % self.url(),
                         headers={'Access-Token': token})
        return r.json()

    def get_portfolio(self, portfolio_id, token=None):
        if (portfolio_id is None):
            raise WrongParameterError
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/portfolios/%s' % (self.url(),
                         portfolio_id), headers={'Access-Token': token})
        return r.json()

    # DEPRECATED: use market.get_historical_data() instead
    def get_historical_data(self, symbol, amount=None, _from=None, _to=None, resolution='1d', fill='business_days', token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/charts/data/%s/%s?amount=%d&from=%s&to=%s&fill=%s' % (self.url(), symbol, resolution, amount if amount else '',
                         _from.strftime('%Y%m%d%H%M') if _from else '', _to.strftime('%Y%m%d%H%M') if _to else '', fill), headers={'Access-Token': token})
        return r.json()

    def get_portfolio_orders(self, id, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/portfolios/%d/orders' %
                         (self.url(), id), headers={'Access-Token': token})
        return r.json()

    def create_order(self, order, id, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.post('%s/portfolios/%d/orders' %
                          (self.url(), id), data=order, headers={'Access-Token': token})
        return r.json()

    def update_balancing(self, balancing, id, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.put('%s/portfolios/%d/balancings' %
                         (self.url(), id), data=balancing, headers={'Access-Token': token})
        return r.json()
