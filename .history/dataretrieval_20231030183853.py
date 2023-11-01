import mysql.connector
import json

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

    def retrieve_data_ordered_by_item_id(self):
        self.cursor.execute("SELECT * FROM tblSalesStatistics ORDER BY ItemID ASC")
        result = self.cursor.fetchall()
        return result

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    config_file_path = r"C:\Users\laeat\Documents\Coding\Wherehousev2\app\build\intermediates\assets\debug\config.json"

    warehouse = DataRetrieval(config_file_path)

    results = warehouse.retrieve_data_ordered_by_item_id()

    for row in results:
        print(row)

    warehouse.close_connection()
