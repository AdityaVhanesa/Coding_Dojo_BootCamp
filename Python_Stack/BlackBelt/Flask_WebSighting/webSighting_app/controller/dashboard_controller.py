from flask import render_template, session, redirect

from webSighting_app import app
from webSighting_app.models.Sightings import Sighting
from webSighting_app.models.Users import User
from webSighting_app.models.Skeptics import Skeptic


@app.route("/dashboard")
def dashBoardView():
    if "user_id" not in session:
        return redirect("/")

    allSightings = Sighting.getAll()
    return render_template("/dashBoard/dashboard_index.html", sightings = allSightings)
