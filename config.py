class Config:
    _api_key = ''

    def __init__(self):
        # Create the database, then close the connection to avoid bug
        if (self._api_key == ''):
            with open('config.txt') as config:
                config_data = [x.strip().split(':') for x in config.readlines()]
            for key,value in config_data:
                if (key == 'API_KEY'):
                    self._api_key = value

    def get_api_key(self):
        return self._api_key
