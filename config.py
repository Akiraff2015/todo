from custom_class.load_json import open_file

DEBUG = True
TEMPLATES_AUTO_RELOAD = True
SECRET_KEY = open_file('key.json', 'key', 'SECRET_KEY')
SQLALCHEMY_DATABASE_URI = open_file('key.json', 'db', 'url')
SQLALCHEMY_TRACK_MODIFICATIONS = True