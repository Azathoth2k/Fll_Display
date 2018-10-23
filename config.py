"""Configuration settings for FLL Pit Display."""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'fllipit.db')
DEBUG = True
EVENT_NAME = 'Litteton FLL Qualifier'
TEST_DB = False
DB_FILE = 'E:\\temp\\fll_5rounds.accdb'
