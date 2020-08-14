from flask import Flask
from config import Config


# Initializations
app = Flask(__name__)
app.config.from_object(Config)

# importing routes at bottom of file to avoid circular imports
from app import routes
