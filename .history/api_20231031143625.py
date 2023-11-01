import mysql.connector
from flask import Flask
from flask_cors import CORS
import json



api = Flask(__name__)
CORS(api)
config_file_path = r"C:\Users\laeat\Documents\Coding\Wherehouse app\app\build\intermediates\assets\debug\config.json"

class DataRetrieval:
    def __init__(self, config_path):
        self.config_path = config_path
        self.load_config()
        self.connect_to_database()

    def load_config(self):
        with open(self.config_path, "r") as config_file:
            self.configdata = json.load(config_file)

    def connect_to_database(self):
        self.connection = mysql.connector.connect(
            user=self.configdata["user"],
            password=self.configdata["password"],
            host=self.configdata["host"],
            database=self.configdata["database"]
        )
        self.cursor = self.connection.cursor()

    def retrieveData(self):
        self.cursor.execute("SELECT * FROM tblSalesStatistics ORDER BY ItemID ASC")
        result = self.cursor.fetchall()
        return result

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

data_retrieval = DataRetrieval(config_file_path)

@api.route('/get_data', methods=['GET'])
def get_data():
    results = data_retrieval.retrieveData()
    return results


if __name__ == "__main__":
    api.run(host='0.0.0.0', port=5000)
