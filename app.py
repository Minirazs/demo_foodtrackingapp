from flask import Flask, render_template, request, redirect, url_for
import os
import json
import random

app = Flask(__name__)
database = {}
with open('food.json') as fp:
    database = json.load(fp)


@app.route('/')
def home():
    return render_template('home.template.html')

@app.route('/user')
def show_users():
    return render_template('users.template.html', all_users=database)

@app.route('/user/add')
def show_add_user():
    return render_template('add_user.template.html')

@app.route('/user/add', methods=["POST"])
def process_add_customer():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    food = request.form.get('food')
    calorie = request.form.get('calorie')
    meal = request.form.get('meal')
    date = request.form.get('date')

    database.append({
        'id': random.randint(10000, 99999),
        'first_name': first_name,
        'last_name': last_name,
        'food': food,
        'calorie': calorie,
        'meal': meal,
        'date': date
    })

    with open('food.json', 'w') as fp:
        json.dump(database, fp)

    return redirect(url_for('show_users')) #redirect to function's name 'show_users'


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),     #must give a host (IP address)
            port=int(os.environ.get('PORT')),   #networking clients access
            debug=True)
