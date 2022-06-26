from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'AZXY-126'


@app.route('/')
def hello_session():  # put application's code here
    if 'visit' in session:
        session['visit'] += 1
    else:
        session['visit'] = 0
    return render_template('index.html')


@app.route("/destroy_session")
def bye_session():
    print(session)
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run()
