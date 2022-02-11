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

    def get_default_portfolio_id(self, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/portfolios/' % self.url(),
                         headers={'Access-Token': token})
        portfolios = r.json()
        default_portfolio_id = None
        for p in portfolios:
            if p["is_default"]:
                default_portfolio_id = p["id"]
                break
        return default_portfolio_id

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

    def get_strategies(self, portfolio_id, token=None):
        if (portfolio_id is None):
            raise WrongParameterError
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/portfolios/%d/strategies/' %
                         (self.url(), portfolio_id),
                         headers={'Access-Token': token})
        return r.json()

    def get_trading_accounts(self, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/trading_accounts/' % self.url(),
                         headers={'Access-Token': token})
        return r.json()

    def create_robot(self, portifolio_id, robot, dry_run = False, token=None):
        if (token is None):
            token = self.client.get_token()

        if (dry_run):
            print('%s/portfolios/%d/robots with data %s' % (self.url(), portifolio_id, robot))
            return
        else:
            r = requests.post('%s/portfolios/%d/robots' %
                             (self.url(), portifolio_id),
                             json=robot, headers={'Access-Token': token})
            return r.json()

    def get_robots(self, portifolio_id, status = None, token=None):
        if (token is None):
            token = self.client.get_token()
        if (status is None):
            r = requests.get('%s/portfolios/%d/robots' %
                             (self.url(), portifolio_id),
                             headers={'Access-Token': token})
        else:
            r = requests.get('%s/portfolios/%d/robots?status=%s' %
                (self.url(), portifolio_id, status), headers={'Access-Token': token})
        return r.json()

    def get_robot(self, portifolio_id, robot_id, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/portfolios/%d/robots/%d' %
                         (self.url(), portifolio_id, robot_id),
                         headers={'Access-Token': token})
        return r.json()

    def cancel_robot(self, portifolio_id, robot_id, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.delete('%s/portfolios/%d/robots/%d' %
                            (self.url(), portifolio_id, robot_id),
                            headers={'Access-Token': token})
        return r.json()

    def pause_robot(self, portifolio_id, robot_id, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.post('%s/portfolios/%d/robots/%d/pause' %
                         (self.url(), portifolio_id, robot_id),
                         headers={'Access-Token': token})
        return r.json()

    def resume_robot(self, portifolio_id, robot_id, token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.post('%s/portfolios/%d/robots/%d/resume' %
                         (self.url(), portifolio_id, robot_id),
                         headers={'Access-Token': token})
        return r.json()
