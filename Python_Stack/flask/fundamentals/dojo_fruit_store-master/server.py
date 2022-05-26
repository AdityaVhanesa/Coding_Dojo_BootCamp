from flask import Flask, render_template, request

app = Flask(__name__)


def showData(data, user):
    total_items = 0
    for _, value in data.items():
        total_items += int(value)

    student_name = user['first_name'] + " " + user['last_name']
    print(f"charging {student_name} for {total_items} fruits")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    fruit_count = {
        'apple': request.form['apple'],
        'raspberry': request.form['strawberry'],
        'strawberry': request.form['raspberry']
    }
    user = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'id': request.form['student_id']
    }
    showData(fruit_count, user)
    return render_template("checkout.html", fruit_count=fruit_count, user=user)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
