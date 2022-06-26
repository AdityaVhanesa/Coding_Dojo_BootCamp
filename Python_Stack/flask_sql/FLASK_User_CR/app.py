from flask import Flask, render_template, request, redirect

from users import USER

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    users_dict = USER.all()
    print(users_dict)
    return render_template('index.html', users=users_dict)


@app.route('/add_user')
def add_user():
    return render_template('create_friend.html')


@app.route('/create_user', methods=['POST'])
def create_user():
    user_dict = {
        "first_name": request.form.get('first_name'),
        "last_name": request.form.get('last_name'),
        "email": request.form.get('email')
    }
    USER.add(user_dict)
    return redirect('/')


@app.route('/users/<int:user_id>')
def showUser(user_id):
    userObject = USER.getUserById({"id": user_id})
    return render_template("show_user.html", user=userObject)


@app.route('/users/<int:user_id>/delete')
def removeUser(user_id):
    USER.removeUserById({"id": user_id})
    return redirect("/")


@app.route('/users/<int:user_id>/edit')
def updateUserForm(user_id):
    userObject = USER.getUserById({"id": user_id})
    return render_template("update_user.html", user=userObject)


@app.route('/users/<int:user_id>/update', methods=["POST"])
def updateUser(user_id):
    USER.updateUserById({"id": user_id,
                         "first_name": request.form.get("first_name"),
                         "last_name": request.form.get("last_name"),
                         "email": request.form.get("email")
                        })

    return redirect(f"/users/{user_id}")


if __name__ == '__main__':
    app.run()
