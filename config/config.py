# -*- coding: utf-8 -*-
import json
import os


class Config(object):
    APP_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_ROOT, os.pardir))
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # currently is postgres db
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')



class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
