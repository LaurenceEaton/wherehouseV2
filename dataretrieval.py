import mysql.connector
import json
from flask import Flask, jsonify
from flask import send_from_directory
from flask import render_template
from flask import request
import os


app = Flask(__name__)

class DataRetrieval:
    config_path = r"C:\Users\laeat\Documents\Coding\Wherehousev2\wherehouseV2\app\build\intermediates\assets\debug\config.json"

    @staticmethod
    def connect_to_database():
        with open(DataRetrieval.config_path, "r") as config_file:
            configdata = json.load(config_file)

        connection = mysql.connector.connect(
            user=configdata["user"],
            password=configdata["password"],
            host=configdata["host"],
            database=configdata["database"]
        )

        cursor = connection.cursor()
        return connection, cursor

    @staticmethod
    def close_connection(cursor, connection):
        cursor.close()
        connection.close()

    @staticmethod
    def fetchdata(table):
        connection, cursor = DataRetrieval.connect_to_database()

        sql_query = f"SELECT * FROM {table} ORDER BY ItemID ASC"
        cursor.execute(sql_query)
        results = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        data = []

        for row in results:
            
            row_dictionary = dict(zip(columns, row))

            data.append(row_dictionary)

        DataRetrieval.close_connection(cursor, connection)
        return jsonify(data)

@app.route('/get_tblitems', methods=['GET'])
def get_tblitems():
    return DataRetrieval.fetchdata("tblitems")

@app.route('/get_tbllocations', methods=['GET'])
def get_tbllocations():
    return DataRetrieval.fetchdata("tbllocations")

@app.route('/get_tblsales', methods=['GET'])
def get_tblsales():
    return DataRetrieval.fetchdata("tblsales")

@app.route('/get_tblsalesstatistics', methods=['GET'])
def get_tblsalesstatistics():
    return DataRetrieval.fetchdata("tblsalesstatistics")

@app.route('/graph_<int:graph_id>.png')
def send_graph(graph_id):
    filename = f'graph_{graph_id}.png'
    return send_from_directory('static', filename)


@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.json
    item_id = data['itemid']
    item_name = data['itemname']
    expiry_date = data['expirydate']
    connection, cursor = DataRetrieval.connect_to_database()
    cursor = connection.cursor()
    sql_query = "INSERT INTO tblitems (ItemID, ItemName, ExpiryDate) VALUES (%s, %s, %s)"
    return jsonify({'status': 'success'})

@app.route('/add_to_quantity', methods=['POST'])
def update_item_quantity():
    data = request.get_json()
    item_id = data['ItemID']
    additional_quantity = data['addToQuantity']

    connection, cursor = DataRetrieval.connect_to_database()
    cursor.execute("SELECT Quantity FROM tblitems WHERE ItemID = %s", (item_id,))
    result = cursor.fetchone()
    if result:
        current_quantity = result[0]
        new_quantity = current_quantity + additional_quantity

        cursor.execute("UPDATE tblitems SET Quantity = %s WHERE ItemID = %s", (new_quantity, item_id))
        connection.commit()
        message = 'Quantity updated successfully'
    else:
        message = 'Item not found'

    cursor.close()
    connection.close()

    return jsonify({'message': message}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

