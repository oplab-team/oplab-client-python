from datetime import datetime, timedelta
import requests


class Market:
    def __init__(self, client) -> None:
        self.client = client

    def historical_options(self, symbol, start=datetime.strftime(datetime.today() - timedelta(days=1), '%Y-%m-%d'), to=datetime.strftime(datetime.today() - timedelta(days=1), '%Y-%m-%d'), token=None):
        if (token is None):
            token = self.client.get_token()
        r = requests.get('%s/historical/options/%s/%s/%s' %
                         (self.url(), symbol, start, to), headers={'Access-Token': token})
        return r.json()

    def url(self):
        return '%s%s' % (self.client.config['base_url'], 'market')
