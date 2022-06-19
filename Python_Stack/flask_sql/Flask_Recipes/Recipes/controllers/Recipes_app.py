from flask import render_template, redirect, request, flash, session

from Recipes import app
from Recipes.config.forms import RegistrationForm
from Recipes.models.users import User


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=['POST'])
def register():
    formObject = RegistrationForm(request.form)
    form = formObject.isValid()
    isValid = True
    for key in form:
        isValid = form[key][0] and isValid
        if not isValid:
            flash(form[key][1])

    if isValid:
        User.save(formObject.getData())
        flash("Registration Success")

    return redirect("/")


@app.route("/login", methods=['POST'])
def logIn():
    logInData = {
        "email": request.form.get("email"),
        "password": request.form.get("password")
    }

    user = User.validateLogin(logInData)
    if user:
        session["user_id"] = user.id
        return redirect("/dashboard")

    else:
        flash("Invalid Credentials")
        return redirect("/")


@app.route("/dashboard")
def dashBoard():
    user = User.getById({
        "idusers": session['user_id']
    })
    return render_template("dashboard.html", user=user)


@app.route("/logout")
def logOut():
    session.clear()
    return redirect("/")


@app.route("/recipes/create")
def createRecipes():
    user = User.getById({
        "idusers": session['user_id']
    })
    return render_template("new_recipes.html", user=user)

















