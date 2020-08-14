from flask import Flask

# import flask-bootstrap
from flask_bootstrap import Bootstrap

# Initializations
app = Flask(__name__)
bootstrap = Bootstrap(app)

# importing routes at bottom of file to avoid circular imports
from app import routes
