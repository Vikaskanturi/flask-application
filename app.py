from flask import Flask


def create_app():
    app = Flask(__name__)
    print("inside create_app function")

    @app.route('/')
    def home():
        print("inside home function")
        return 'Hi hi GFG43 25th april 2026  - 2:30 PM elaborate the date and time in the response to make it more informative and engaging for the users. This will help them understand the context of the message better and create a more personalized experience for them. Additionally, you can also include some relevant emojis or images to make the response more visually appealing and engaging for the users. Overall, the key is to provide value and create a connection with your audience through your responses.'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
