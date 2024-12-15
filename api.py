from flask import Flask, request, jsonify
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

@app.route('/', methods=['GET'])
def get_users():
    data=request.get_json()
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)