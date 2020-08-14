from flask import Flask


# Initializations
app = Flask(__name__)

# importing routes at bottom of file to avoid circular imports
from app import routes
