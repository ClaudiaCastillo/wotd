# app.home
# The homepage application (Blueprint)
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Nov 23 10:27:32 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
The homepage application (Blueprint)
"""

##########################################################################
## Blueprint Object
##########################################################################

from flask import Blueprint

home = Blueprint('home', __name__)

##########################################################################
## Imports
##########################################################################

from . import views
