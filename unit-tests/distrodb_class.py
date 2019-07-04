"""
Distro Class to show examples on unit testing a class
"""

# For reading the db_data.json file
import json


class DistroDB:
    def __init__(self):
        self.data = None

    def connect(self, db_file):
        with open(db_file) as json_file:
            self.data = json.load(json_file)

    def get_data(self, name):
        for distro in self.data["distros"]:
            if distro["name"] == name:
                return distro

    def disconnect(self):
        print("\nClosing DB connection.")
