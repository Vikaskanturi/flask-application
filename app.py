import hashlib
import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    # Use environment variable for secret key, with a fallback for development
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-for-local-development-only')

    @app.route('/')
    def home():
        return 'Hello, World! GFG43'

    @app.route('/hash/<text>')
    def hash_text(text):
        # Use SHA-256 instead of MD5 for better security
        return hashlib.sha256(text.encode()).hexdigest()

    return app


if __name__ == '__main__':
    app = create_app()
    # Use environment variables for host and port, default to safer values
    host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_RUN_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    app.run(host=host, port=port, debug=debug)
