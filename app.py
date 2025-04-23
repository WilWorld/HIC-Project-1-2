#! /usr/bin/python3
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'dbdev.cs.kent.edu'
app.config['MYSQL_USER'] = 'wnahra'  # Flashline username
app.config['MYSQL_PASSWORD'] = 'sKsvG13k'  # phpMyAdmin password
app.config['MYSQL_DB'] = 'wnahra'  # Flashline username

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/info.html')
def info():
    return render_template('info.html')

@app.route('/generated.html')
def generated():
    return render_template('generated.html')

@app.route('/tech.html')
def tech():
    return render_template('tech.html')

@app.route('/other.html')
def other():
    return render_template('other.html')

@app.route('/biomes.html')
def biomes():
    return render_template('biomes.html')

@app.route('/vote.html')
def vote():
    return render_template('vote.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
