from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "THIS IS SECret Key fOR Dojo_SURVEY"


@app.route('/')
def hello_survey():  # put application's code here
    return render_template('index.html')


@app.route('/process', methods=['post'])
def process_form():
    print(request.method)
    print(request.form)
    session['name'] = request.form['s_name']
    session['dojo_location'] = request.form['s_dojo_location']
    session['language'] = request.form['s_fav_language']
    session['comment'] = request.form['s_comment']
    return redirect('/result')


@app.route('/result')
def result_form():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
