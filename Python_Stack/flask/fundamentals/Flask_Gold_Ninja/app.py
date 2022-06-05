from random import randint
from flask import Flask, render_template, request, session, redirect
from datetime import datetime

app = Flask(__name__)
app.secret_key = "This is Secrate key for the Gold Ninja Game"
isAppStart = True


@app.route('/')
def hello_world():  # put application's code here
    global isAppStart
    if isAppStart:
        session.clear()
        isAppStart = False

    if 'score' not in session:
        session['score'] = 0
        session['font'] = 'teal'
        session['logs'] = {}

    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_form():
    GoldCoins = {
        'farm': randint(10, 20),
        'cave': randint(5, 10),
        'house': randint(2, 5),
        'casino': randint(-50, 50)
    }
    currentLocation = request.form.get('location')
    coinEarned = GoldCoins[currentLocation]
    earningType = "Earned" if coinEarned >= 0 else "Loss"
    fontColor = "teal-font" if coinEarned >= 0 else 'red-font'
    if not 0 > coinEarned > session['score']:
        session['score'] += coinEarned

    if coinEarned < 0:
        coinEarned = 0 - coinEarned

    currentDate = datetime.now().__str__()
    logString = f"{earningType} {coinEarned} coins from the {currentLocation}! {currentDate}"

    session['logs'][currentDate] = [logString, fontColor]
    return redirect('/')


if __name__ == '__main__':
    app.run()
