from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/play')
def hello_play():
    return render_template('index.html', box_color='lightblue', box_count=3)


@app.route('/play/<int:x>')
def hello_count_play(x):
    return render_template('index.html', box_color='lightblue', box_count=x)


@app.route('/play/<int:x>/<color>')
def hello_count_color_play(x, color):
    return render_template('index.html', box_color=color, box_count=x)


if __name__ == '__main__':
    app.run(debug=True)
