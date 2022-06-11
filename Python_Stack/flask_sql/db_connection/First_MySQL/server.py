from flask import Flask, request, render_template, redirect
from friend import Friend

app = Flask(__name__)
app.secret_key = "This is Secret key for the Flask Application"


@app.route('/')
def index():
    friend = Friend.all()
    return render_template('index.html', all_friends = friend)


@app.route('/friend')
def friend_page():
    return  render_template('friend.html')


@app.route('/create_friend', methods=["POST"])
def create_friend():
    data = {
        "f_name": request.form.get('f_name'),
        "l_name": request.form.get('l_name')
    }
    Friend.add(data)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
