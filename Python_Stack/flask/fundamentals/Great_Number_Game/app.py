from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = 'AXYSB0123VBHD'


@app.route('/')
def hello_user():  # put application's code here
    session['bg'] = '##f4f1de'
    session['bt'] = 'GUESS'
    return render_template('index.html')


@app.route('/game')
def hello_game():
    if 'random' not in session:
        session['random'] = random.randint(0, 100)

    return render_template('game.html')


@app.route('/player_name', methods=['post'])
def cach_playerName():
    session['player'] = request.form['player_name']
    return redirect('/game')


@app.route('/process_number', methods=['post'])
def deterMineResult():
    randomNumber = session['random']
    user_number = int(request.form['user_number'])
    if user_number > randomNumber:
        session['bg'] = '#ffadad'
        session['bt'] = 'GUESS LOW'
    elif user_number < randomNumber:
        session['bg'] = '#fdffb6'
        session['bt'] = 'GUESS HIGH'
    else:
        session.pop('random')
        session['bg'] = '##f4f1de'
        session['bt'] = 'GUESS'
        return redirect('/game_complete')

    return redirect('/game')


@app.route('/game_complete')
def completeGame():
    return render_template('win_game.html')


if __name__ == '__main__':
    app.run()
