from flask import Flask  # Import Flask to allow us to create our app

hello_flask = Flask(__name__)  # Create a new instance of the Flask class called "app"


@hello_flask.route('/')  # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@hello_flask.route('/dojo')
def hello_dojo():
    return 'Dojo.!'


@hello_flask.route('/repeat/<count>/<item>')
def show_count_item(count, item):
    return item * int(count)


@hello_flask.route('/say/<name>')  # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    return "Hello, " + name


@hello_flask.errorhandler(404)
def handle_404(e):
    # handle all other routes here
    return 'Sorry No Response, Try Again..!'


if __name__ == "__main__":  # Ensure this file is being run directly and not from a different module
    print("HI")
    hello_flask.run(debug=True)  # Run the app in debug mode.
