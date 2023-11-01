import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS
import json
from google.cloud import storage

api = Flask(__name__)
CORS(api)
config_bucket_name = "iconic-parsec-395409.appspot.com"
config_file_name = "config.json"

class DataRetrieval:
    def __init__(self, config_bucket_name, config_file_name):
        self.config_bucket_name = config_bucket_name
        self.config_file_name = config_file_name
        self.load_config()
        self.connect_to_database()

    def load_config(self):
        storage_client = storage.Client()

        bucket = storage_client.get_bucket(self.config_bucket_name)
        blob = bucket.blob(self.config_file_name)

        try:
            configcontent = blob.download_as_text()

            self.configdata = json.loads(configcontent)
        except:
            print("Error accessing config")

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

data_retrieval = DataRetrieval(config_bucket_name, config_file_name)

@api.route('/get_data', methods=['GET'])
def get_data():
    results = data_retrieval.retrieveData()
    return jsonify(results)  # Return the data as JSON

if __name__ == "__main__":
    api.run(host='0.0.0.0', port=5000)
