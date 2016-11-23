# app.exceptions
# Exceptions that are specific to the WOTD application
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Nov 23 10:20:48 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: exceptions.py [] benjamin@bengfort.com $

"""
Exceptions that are specific to the WOTD application
"""

##########################################################################
## Imports
##########################################################################

class WOTDException(Exception):
    pass


class ImproperlyConfigured(WOTDException):
    pass
