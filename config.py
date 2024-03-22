# imports
import configparser
import typing

class BaseConfig():
    '''
    Base model class for config reading and writing.
    Usage example:

        class Config(BaseConfig):
            key1: str = value # str param with default value
            key2: int = value # int param with default value
            key3: bool # bool param without default value

        config = Config.from_file('config.ini')
          or
        config = Config(key3 = True).create_file('config.ini')
    '''
    def __init__(self, filename='config.ini'):
        self.config = configparser.ConfigParser()
        self.filename = filename
    
    def read(self, filename=None):
        if filename is None:
            filename = self.filename
        self.config.read(filename)
        return self.config
    
    def write(self, filename=None):
        if filename is None:
            filename = self.filename
        with open(filename, 'w') as configfile:
            self.config.write(configfile)

    @classmethod
    def from_file(cls, filename='config.ini'):
        # read config from file
        config = cls(filename)
        config.read(filename)
        return config

    def create_file(self, filename=None):
        if filename is None:
            filename = self.filename
        self.write(filename)