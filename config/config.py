import config.version as v

class Settings():
    """ Settings Class """
    def __init__(self):
        self.version = v.get_version()
