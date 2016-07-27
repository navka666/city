# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

def register_blueprints(app):
    # Prevents circular imports
    from city.views import citys
    app.register_blueprint(citys)

register_blueprints(app)


if __name__ == '__main__':
    app.run()