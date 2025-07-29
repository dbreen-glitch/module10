import json
import requests
from flask import Flask

# API endpoint URL's and access keys
WMATA_API_KEY = "069fe4c420d64b8da4ea57dffb4b8b82"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)

# Get incidents by machine type
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
    """Retrieves Incidents endpoint."""

    incidents = []

    # Condition unit_type for plural and singular inputs
    if unit_type.endswith('s'):
        unit_type = unit_type[:-1]

    # Condition to match api incident format
    unit_type = unit_type.upper()

    # Retrieve response from api and gather all incidents
    response = requests.get(INCIDENTS_URL, headers=headers)
    all_incidents = response.json()
    elevator_incidents = all_incidents['ElevatorIncidents']

    # Iterate through each incident to create subset of incidents
    for incident in elevator_incidents:
        if incident['UnitType'] == unit_type:
            incidents_dict = {
                'StationCode': incident['StationCode'],
                'StationName': incident['StationName'],
                'UnitType': incident['UnitType'],
                'UnitName': incident['UnitName']
            }
            incidents.append(incidents_dict)
    return json.dumps(incidents)


if __name__ == '__main__':
    app.run(debug=True)
