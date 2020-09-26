from flask import Flask, render_template, request, redirect, url_for
import os
import json

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


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),     #must give a host (IP address)
            port=int(os.environ.get('PORT')),   #networking clients access
            debug=True)
