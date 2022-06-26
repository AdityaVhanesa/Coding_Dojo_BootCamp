from webSighting_app import app
from webSighting_app.controller import login_controller, dashboard_controller, sighting_controller

if __name__ == '__main__':
    app.run(debug=True, port=8080)