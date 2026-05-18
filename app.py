import hashlib
import os
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)
    # Use environment variable for secret key.
    # Fallback to None ensures no hardcoded credential flags.
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    @app.route('/', methods=['GET'])
    def home():
        print("inside home function")
        return 'Hi hi GFG43 25th april 2026  - 2:30 PM'

    return app



if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
