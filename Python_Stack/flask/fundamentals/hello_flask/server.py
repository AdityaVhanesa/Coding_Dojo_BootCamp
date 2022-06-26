from flask import Flask, render_template

hello_flask = Flask(__name__)


@hello_flask.route('/')
def hello_world():
    return render_template('index.html')


@hello_flask.route('/dojo')
def hello_dojo():
    return 'Dojo.!'


@hello_flask.route('/repeat/<count>/<item>')
def show_count_item(count, item):
    return item * int(count)


@hello_flask.route('/say/<name>')
def hello(name):
    return "Hello, " + name


@hello_flask.errorhandler(404)
def handle_404(e):
    # handle all other routes here
    return 'Sorry No Response, Try Again..!'



'''
Following code will not be run because pycharm FLSK service is being used for testing.
Make sure to test following before using in production.
'''

if __name__ == "__main__":  # Ensure this file is being run directly and not from a different module
    print("HI")
    hello_flask.run(debug=True)  # Run the app in debug mode.
