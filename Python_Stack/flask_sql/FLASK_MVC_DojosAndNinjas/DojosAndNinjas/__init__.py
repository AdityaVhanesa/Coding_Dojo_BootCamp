from flask import Flask

app = Flask(__name__)
app.secret_key = "This is secret key for the dojos and Ninjas"

