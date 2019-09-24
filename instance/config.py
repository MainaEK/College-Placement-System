""" Configuration file for the API """

class Config(object):
    """ Parent configuration class """
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """ Configuration for development environment """
    DEBUG = True


class TestingConfig(Config):
    """ Configuration for the testing environment """
    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'testing': TestingConfig
}
