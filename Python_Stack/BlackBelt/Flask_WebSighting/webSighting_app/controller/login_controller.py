from flask import render_template, request, redirect, session

from webSighting_app import app
from webSighting_app.forms.loginForm import LoginForm
from webSighting_app.forms.registerForm import RegisterForm
from webSighting_app.models.Users import User


@app.route("/")
def index():
    return render_template('/login/index.html')


@app.route("/register_user", methods=['POST'])
def registerUser():
    form = RegisterForm(request.form)
    if form.isValid():
        User.add(form.cleanData())
        return render_template("/")
    return redirect("/")


@app.route("/login_user", methods=["POST"])
def loginUser():
    form = LoginForm(request.form)
    if form.isValid():
        user = User.getUserByEmail(form.cleanData())
        if user and User.validatePassword(user.password, form.password):
            session["user_id"] = user.id
            session["user_first_name"] = user.first_name
            session["user_last_name"] = user.last_name
            session["user_email"] = user.email
            return redirect("/dashboard")
    return redirect("/")


@app.route("/logout")
def logoutUser():
    session.clear()
    return redirect("/")


@app.route("/test_success")
def testSuccessView():
    return render_template("/login/test_success.html")


@app.route("/test_fail")
def testFailedView():
    return render_template("/login/test_fail.html")
