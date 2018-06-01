from flask import Flask


app = Flask(__name__)
app.config.from_pyfile('../config.py')
SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']

from controllers import main  # noqa
app.register_blueprint(main)
