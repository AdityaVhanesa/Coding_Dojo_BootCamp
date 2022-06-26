from flask import render_template, request, redirect, session

from webSighting_app import app
from webSighting_app.forms.reportForm import ReportForm
from webSighting_app.models.Sightings import Sighting
from webSighting_app.models.Skeptics import Skeptic


@app.route("/view/<int:Id>")
def viewSighting(Id):
    if "user_id" not in session:
        return redirect("/")
    sightingObject = Sighting.getById({"id": Id})
    currentSkepticObject = False
    if sightingObject:
        currentSkepticObject = Skeptic.getByUserId_SightingId({
            "sightings_id": sightingObject.id,
            "users_id": session.get("user_id")
        })
    return render_template("/sighting/view.html", sighting=sightingObject, currentUserSkeptic=currentSkepticObject)


@app.route("/edit/<int:Id>")
def editSighting(Id):
    if "user_id" not in session:
        return redirect("/")
    sightingObject = Sighting.getById({"id": Id})
    return render_template("/sighting/update.html", sighting=sightingObject)


@app.route("/delete/<int:sId>")
def deleteSighting(sId):
    if "user_id" not in session:
        return redirect("/")
    Sighting.removeById({
        "users_id": session.get("user_id"),
        "sightings_id": sId
    })
    return redirect("/dashboard")


@app.route("/update/sighting/<int:sId>", methods=["POST"])
def updateSighting(sId):
    if "user_id" not in session:
        return redirect("/")
    form = ReportForm(request.form)
    if form.isValid():
        data = form.cleanData()
        data["users_id"] = session.get("user_id")
        data['id'] = sId
        Sighting.modify(data)
        return redirect("/dashboard")
    return redirect(f"/edit/{sId}")


@app.route("/new/sighting")
def newSightingView():
    if "user_id" not in session:
        return redirect("/")
    return render_template("/sighting/new.html")


@app.route("/new/sighting/create", methods=["POST"])
def createSighting():
    if "user_id" not in session:
        return redirect("/")
    form = ReportForm(request.form)
    print(form.date)
    if form.isValid():
        data = form.cleanData()
        data["users_id"] = session.get("user_id")
        Sighting.add(data)
        return redirect("/dashboard")
    return redirect("/new/sighting")


@app.route("/edit/skeptical/<int:uId>/<int:sId>")
def editCurrentUserSkeptical(uId, sId):
    if "user_id" not in session:
        return redirect("/")
    Skeptic.modify({
        "isSkeptical": 1,
        "isBeliever": 0,
        "sightings_id": sId,
        "users_id": uId
    })

    return redirect(f"/view/{sId}")


@app.route("/edit/believer/<int:uId>/<int:sId>")
def editCurrentUserBeliever(uId, sId):
    if "user_id" not in session:
        return redirect("/")
    Skeptic.modify({
        "isSkeptical": 0,
        "isBeliever": 1,
        "sightings_id": sId,
        "users_id": uId
    })

    return redirect(f"/view/{sId}")


@app.route("/add/believer/<int:uId>/<int:sId>")
def addCurrentUserBeliever(uId, sId):
    if "user_id" not in session:
        return redirect("/")
    Skeptic.add({
        "isSkeptical": 0,
        "isBeliever": 1,
        "sightings_id": sId,
        "users_id": uId
    })

    return redirect(f"/view/{sId}")


@app.route("/add/skeptical/<int:uId>/<int:sId>")
def addCurrentUserSkeptical(uId, sId):
    if "user_id" not in session:
        return redirect("/")
    Skeptic.add({
        "isSkeptical": 1,
        "isBeliever": 0,
        "sightings_id": sId,
        "users_id": uId
    })

    return redirect(f"/view/{sId}")
