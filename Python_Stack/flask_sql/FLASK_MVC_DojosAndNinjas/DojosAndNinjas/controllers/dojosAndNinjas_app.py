from flask import render_template, request, redirect

from DojosAndNinjas import app
from DojosAndNinjas.models.dojos import Dojo
from DojosAndNinjas.models.ninjajs import Ninja


@app.route("/")
def home():
    return redirect("/dojos")


@app.route("/dojos")
def index():
    dojosList = Dojo.getAll()
    return render_template('index.html', dojos=dojosList)


@app.route("/dojo/create", methods=['POST'])
def createDojo():
    dojoDict = {
        "name": request.form.get('dojo_name')
    }
    Dojo.save(dojoDict)
    return redirect('/')


@app.route("/ninja/")
def addNinja():
    dojoList = Dojo.getAll()
    return render_template('add_ninja.html', dojos=dojoList)


@app.route("/ninja/create", methods=['POST'])
def createNinja():
    dojoId = Dojo.getByName({'name': request.form.get('dojo')}).id
    ninjaDict = {
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'age': request.form.get('age'),
        'dojo_id': dojoId,
    }
    Ninja.save(ninjaDict)
    return redirect("/")


@app.route('/dojo/<dojoName>')
def viewNinjas(dojoName):
    dojoId = Dojo.getByName({'name': dojoName})
    ninjas = Ninja.getByDojoID({"dojo_id": dojoId.id})
    return render_template('view_ninjas.html', users=ninjas)
