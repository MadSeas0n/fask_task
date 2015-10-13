import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktask.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'some delicios_shit'

DATABASE_PATH = os.path.join(basedir, DATABASE)