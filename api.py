from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import mysql.connector
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

#database configuration

db_config={
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

def db_conn():
    return mysql.connector.connect(**db_config)

@app.route('/')
def login_page():
    return render_template("loginpage.html")

@app.route('/submit', methods=['POST'])
def login_data_compre():
    login=request.form.get('login')
    password=request.form.get('password')

    connection = db_conn()
    cursor= connection.cursor()

    cursor.execute("SELECT * FROM users WHERE name = %s", (login,))
    user=cursor.fetchone()

    cursor.close()
    connection.close()

    if user:
        db_pass=user[2]
        if db_pass == password:
            print("loged in")
            return redirect(url_for('login_page')) # next template
        else:
            print("wrong password")
            return redirect(url_for('login_page'))
    else:
        print("user not found")
        return redirect(url_for('login_page'))

@app.route('/welocome')
def welcome():
    return render_template("qwe.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)