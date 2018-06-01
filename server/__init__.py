from flask import Flask
from controllers import main


app = Flask(__name__)
app.register_blueprint(main)
app.config.from_pyfile('../config.py')
