import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

value = config.items("extensions")

print(value)