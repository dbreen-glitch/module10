import json
from wmata_api import app
import unittest

class WMATATest(unittest.TestCase):
    """Unit test for WMATA API"""
    def test_http_success(self):
        """Unit test for WMATA API http success"""
        escalator_response = app.test_client().get('/incidents/escalators').status_code
        self.assertEqual(escalator_response, 200)

        elevator_response = app.test_client().get('/incidents/elevators').status_code
        self.assertEqual(elevator_response, 200)

################################################################################

    def test_required_fields(self):
        """Unit test for WMATA API required fields"""
        required_fields = ['StationCode', 'StationName', 'UnitType', 'UnitName']

        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # Test for required fields
        for incident in json_response:
            for field in required_fields:
                self.assertIn(field, incident)

################################################################################

    # Ensure all entries returned by the /escalators endpoint have a UnitType of "ESCALATOR"
    def test_escalators(self):
        """Unit test for WMATA API escalators"""
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # For each incident in the JSON response, assert that the 'UnitType' is "ESCALATOR"
        for incident in json_response:
            self.assertEqual(
                incident['UnitType'].upper(), 'ESCALATOR'
            )
################################################################################

    # Ensure all entries returned by the /elevators endpoint have a UnitType of "ELEVATOR"
    def test_elevators(self):
        """Unit test for WMATA API elevators"""
        response = app.test_client().get('/incidents/elevators')
        json_response = json.loads(response.data.decode())

        # For each incident in the JSON response, assert that the 'UnitType' is "ELEVATOR"
        for incident in json_response:
            self.assertEqual(
                incident['UnitType'].upper(), 'ELEVATOR'
            )
################################################################################

# Use to run
if __name__ == "__main__":
    unittest.main()