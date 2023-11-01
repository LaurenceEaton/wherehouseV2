from flask import Flask, jsonify
import mysql.connector

db_config = {
    'user': 'your_db_user',
    'password': 'your_db_password',
    'host': 'your_db_host',
    'database': 'your_db_name',
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Modify the 'get_data' route to execute SQL queries and fetch data as needed
@app.route('/get_data', methods=['GET'])
def get_data():
    query = "SELECT * FROM your_table"
    cursor.execute(query)
    data = cursor.fetchall()
    return jsonify(data)

api = Flask(__name__)

if __name__ == '__main__':
    api.run()
