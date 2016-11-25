# config
# WOTD Web Configuration
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Nov 23 09:20:28 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: config.py [] benjamin@bengfort.com $

"""
WOTD Web Configuration
"""

##########################################################################
## Imports and Module Constants
##########################################################################

import os
import flask_dotenv as dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))


##########################################################################
## Configuration Objects
##########################################################################

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or "theeaglefliesatmidnight"
    WORDNIK_API_KEY = os.environ.get('WORDNIK_API_KEY')

    @staticmethod
    def init_app(app):
        env = dotenv.DotEnv()
        env.init_app(app)


class DevelopmentConfig(Config):

    DEBUG = True


class TestingConfig(Config):

    TESTING = True


class ProductionConfig(Config):

    DEBUG = False
    TESTING = False


##########################################################################
## Configuration Objects
##########################################################################

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
