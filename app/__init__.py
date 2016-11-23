# app
# The WOTD Flask application wrapper
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Nov 23 10:18:31 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
The WOTD Flask application wrapper
"""

##########################################################################
## Imports
##########################################################################

from flask import Flask
from config import config

from .exceptions import ImproperlyConfigured


##########################################################################
## Create Application
##########################################################################

def create_app(config_name='default'):
    """
    Create and configure a flask application.
    """

    if config_name not in config:
        raise ImproperlyConfigured(
            "No configuration named '{}'!".format(config_name)
        )

    # Create the application and fetch the configuration
    app  = Flask(__name__)
    conf = config[config_name]

    # Configure the application
    app.config.from_object(conf)
    conf.init_app(app)

    # Register the home page blueprint
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
