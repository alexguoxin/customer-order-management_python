from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'voa87dy8p9wdep9aw'

    from . import customer_management
    app.register_blueprint(customer_management.bp)

    return app