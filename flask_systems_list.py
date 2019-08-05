#!/usr/bin/env python3
"""
Quick flask application that provides a systems list concept.
Requires: pip3 install flask flask_restful
"""

# Import Flask module
from flask import Flask

# Import flask restful modules
from flask_restful import Api, Resource, reqparse

# Create Flask app and restful api
app = Flask(__name__)
api = Api(app)

# Systems Data (instead of database)
systems = [
    {"hostname": "server01", "os": "CentOS 7", "type": "hw"},
    {"hostname": "server02", "os": "Ubuntu", "type": "vm"},
]

# -- API Endpoints (Systems) --#
class Systems(Resource):
    """Class definition for system entries"""

    def get(self, hostname):
        """
        Retrieve existing entries by hostname
        Example:
        curl -X GET http://localhost:5000/systems/server01
        """

        for system in systems:
            if hostname == system["hostname"]:
                return system, 200

        return "System not found", 404

    def post(self, hostname):
        """
        Add new entries by hostname, os argument
        Example:
        curl --request POST --url http://localhost:5000/systems/server05 \
        --header 'content-type: application/json' \
        --data '{ "os":"Ubuntu 19.10", "type": "vm"}'
        """
        parser = reqparse.RequestParser()
        parser.add_argument("os")
        parser.add_argument("type")
        args = parser.parse_args()

        for system in systems:
            if hostname == system["hostname"]:
                return f"System with name {hostname} already exists", 400

        system = {"hostname": hostname, "os": args["os"], "type": args["type"]}
        systems.append(system)

        return system, 201

    def put(self, hostname):
        """
        Modify existing entries by hostname, os argument
        Example:
        curl --request PUT --url http://localhost:5000/systems/server05 \
        --header 'content-type: application/json' \
        --data '{ "os":"CentOS 8", "type": "vm"}'
        """
        parser = reqparse.RequestParser()
        parser.add_argument("os")
        parser.add_argument("type")
        args = parser.parse_args()

        for system in systems:
            if hostname == system["hostname"]:
                # Modify existing system if it exists
                system["os"] = args["os"]
                system["type"] = args["type"]
                return system, 200

        # Add new system if it does not exist already
        system = {"hostname": hostname, "os": args["os"], "type": args["type"]}
        systems.append(system)

        return system, 201

    def delete(self, hostname):
        """
        Remove entries by hostname
        Example:
        curl -X DELETE http://localhost:5000/systems/server02
        """
        global systems
        systems = [system for system in systems if system["hostname"] != hostname]

        return "{hostname} is deleted.", 200


# -- End of API Endpoint (Systems) --##


def main():
    """Execute Flask application"""

    # Add Systems resource to API and specify endpoint (/systems/)
    api.add_resource(Systems, "/systems/<string:hostname>")

    # Run the app in debug mode
    app.run(debug=True)


if __name__ == "__main__":
    main()
