# app.home.views
# Views for the home blueprint
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Nov 23 10:29:47 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: views.py [] benjamin@bengfort.com $

"""
Views for the home blueprint
"""

##########################################################################
## Imports
##########################################################################

import requests

from flask import current_app as app
from flask import render_template
from dateutil.parser import parse

# Import the Blueprint
from . import home


WOTD_URL = "http://api.wordnik.com:80/v4/words.json/wordOfTheDay"

##########################################################################
## Root View
##########################################################################

@home.route('/', methods=['GET',])
def index():
    # Fetch the WOTD from wordnick
    apikey = app.config['WORDNIK_API_KEY']
    response = requests.get(WOTD_URL, params={"api_key": apikey})
    context  = response.json()

    word = context['word']
    pubdate = parse(context['publishDate']).strftime("%A, %B %d, %Y")
    definitions = context['definitions']

    return render_template('index.html', word=word, pubdate=pubdate, definitions=definitions)
