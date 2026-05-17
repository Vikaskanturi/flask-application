import hashlib
from flask import Flask


def create_app():
    app = Flask(__name__)
    # SonarQube will flag this hardcoded secret key as a vulnerability
    # Flake8 doesn't check for secret key strength/hardcoding by default
    app.config['SECRET_KEY'] = 'dev-key-very-insecure-12345'

    @app.route('/')
    def home():
        return 'Hello, World! GFG43'

    @app.route('/hash/<text>')
    def hash_text(text):
        # SonarQube will flag MD5 as a weak cryptographic algorithm
        # Flake8 won't detect this as a bug
        return hashlib.md5(text.encode()).hexdigest()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
