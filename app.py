#! /usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'bankUser'
app.config['MYSQL_PASSWORD'] = '!tMifKb7V_Qf)I8i'
app.config['MYSQL_DB'] = 'minecraftvote'

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
    mobs = ["Zombie", "Skeleton", "Creeper", "Enderman", 
            "Spider", "Witch", "Blaze", "Slime", "Piglin", 
            "Warden", "Chicken Jockey", "Illager"]
    return render_template('vote.html', mobs=mobs)

@app.route('/vote-mob', methods=['POST'])
def vote_mob():
    selected_mob = request.form.get('mob')
    if selected_mob:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO vote (mobVote) VALUES (%s)", (selected_mob,))
        mysql.connection.commit()
        cur.close()
        flash(f"Thanks for Voting!")
    else:
        flash("Please select a mob before submitting.")
    return redirect(url_for('vote'))

@app.route('/about.html')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
