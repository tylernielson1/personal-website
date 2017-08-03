#!/usr/bin/python
import sys
import logging
from flaskapp import app as application

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/yourProjectName/")
application.secret_key = 'devkey'
