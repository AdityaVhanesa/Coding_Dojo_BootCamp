from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def default():  # put application's code here
    row = 4
    coloumn = 4
    color1 = 'teal'
    color2 = 'lightgray'
    return render_template('index.html',
                           row=row,
                           coloumn=coloumn,
                           color_1=color1,
                           color_2=color2)


@app.route('/<int:x>')
def default_column(x):
    row = x
    coloumn = 4
    color1 = 'teal'
    color2 = 'lightgray'
    return render_template('index.html',
                           row=row,
                           coloumn=coloumn,
                           color_1=color1,
                           color_2=color2)


@app.route('/<int:x>/<int:y>')
def default_color(x, y):
    row = x
    coloumn = y
    color1 = 'teal'
    color2 = 'lightgray'
    return render_template('index.html',
                           row=row,
                           coloumn=coloumn,
                           color_1=color1,
                           color_2=color2)


@app.route('/<int:x>/<int:y>/<color_1>/<color_2>')
def default_box(x, y, color_1, color_2):
    row = x
    coloumn = y
    color1 = color_1
    color2 = color_2
    return render_template('index.html',
                           row=row,
                           coloumn=coloumn,
                           color_1=color1,
                           color_2=color2)


if __name__ == '__main__':
    app.run()
