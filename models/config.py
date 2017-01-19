import ConfigParser


class Config(object):
    """docstring for Config"""
    config_file = './config/config.ini'

    def __init__(self):
        pass

    @staticmethod
    def parse_config(section, key):
        config = ConfigParser.ConfigParser()
        config.read(Config.config_file)
        return config.get(section, key)
