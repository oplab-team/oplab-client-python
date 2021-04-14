class Quant:
    def __init__(self, client) -> None:
        self.client = client

    def url(self):
        return '%s%s' % (self.client.config['base_url'], 'quant')
