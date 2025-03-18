import configparser

from os import environ

CONFIG_FILE = './config/config.ini'

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

API_TOKEN = environ.get('API_TOKEN') if environ.get('API_TOKEN') else config.get('SETTINGS', 'API_TOKEN')

