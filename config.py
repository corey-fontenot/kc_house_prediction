import os
import pandas as pd
basedir = os.path.abspath(os.path.dirname(__file__))


def get_zipcodes():
    """
    Returns a list of zipcodes populated from zipcodes.txt file
    :return: List
    """

    # open zipcodes.txt for read access
    f = open("zipcodes.txt", "r")

    # store contents of zipcodes.txt into a list of zipcodes
    zipcodes = f.readlines()

    # close file when done with it
    f.close()

    return zipcodes


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'password'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ZIPCODES = get_zipcodes()
