import hashlib
import os
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)
    # Use environment variable for secret key
    secret_key = os.environ.get(
        'SECRET_KEY', 'dev-key-for-local-development-only'
    )
    app.config['SECRET_KEY'] = secret_key

    @app.route('/')
    def home():
        return 'Hello, World! GFG43'

    @app.route('/hash/<text>')
    def hash_text(text):
        # Use SHA-256 for better security.
        # This addresses SonarQube's vulnerability report.
        if not text:
            return jsonify({"error": "No text provided"}), 400
        return hashlib.sha256(text.encode()).hexdigest()

    @app.after_request
    def add_security_headers(response):
        # Security headers for SonarQube
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        csp = "default-src 'self'"
        response.headers['Content-Security-Policy'] = csp
        return response

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({"error": "Not Found"}), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({"error": "Internal Server Error"}), 500

    return app


if __name__ == '__main__':
    app = create_app()
    # Use environment variables for host and port
    host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_RUN_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() in (
        'true', '1', 't'
    )
    app.run(host=host, port=port, debug=debug)
