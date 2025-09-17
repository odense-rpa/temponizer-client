from datetime import date
from dotenv import load_dotenv
from temponizer_client.manager import TemponizerClientManager

load_dotenv()


def test_hent_vagtplan(temponizer_manager: TemponizerClientManager):
    """Test the hent_vagtplan function with a real API call."""
    # Test parameters
    startdato = date(2025, 9, 17)
    slutdato = date(2025, 9, 23)
    plantype = "upcoming"
    
    # Call the function through the manager
    result = temponizer_manager.vagtplaner.hent_vagtplan(startdato, slutdato, plantype)
    
    # Assertions - since this is a real API call, we test the structure
    # The result could be None (404) or a list of shift dictionaries
    if result is not None:
        assert isinstance(result, list), "Result should be a list of shifts"
        
        # If there are shifts, validate the structure of each shift
        if len(result) > 0:
            shift = result[0]  # Test the first shift
            assert isinstance(shift, dict), "Each shift should be a dictionary"
            
            # Validate required fields exist
            required_fields = ['shiftId', 'date', 'startTime', 'endTime', 'duration', 
                             'workerId', 'workerName', 'clientId', 'clientName']
            for field in required_fields:
                assert field in shift, f"Shift should contain '{field}' field"
            
            # Validate field types
            assert isinstance(shift['shiftId'], int), "shiftId should be an integer"
            assert isinstance(shift['date'], str), "date should be a string"
            assert isinstance(shift['startTime'], str), "startTime should be a string"
            assert isinstance(shift['endTime'], str), "endTime should be a string"
            assert isinstance(shift['duration'], (int, float)), "duration should be numeric"
            assert isinstance(shift['workerId'], int), "workerId should be an integer"
            assert isinstance(shift['workerName'], str), "workerName should be a string"
            assert isinstance(shift['clientId'], int), "clientId should be an integer"
            assert isinstance(shift['clientName'], str), "clientName should be a string"
            
            # Validate date format (YYYY-MM-DD)
            import re
            date_pattern = r'^\d{4}-\d{2}-\d{2}$'
            assert re.match(date_pattern, shift['date']), "date should be in YYYY-MM-DD format"
            
            # Validate ISO datetime format for start and end times
            datetime_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$'
            assert re.match(datetime_pattern, shift['startTime']), "startTime should be in ISO format"
            assert re.match(datetime_pattern, shift['endTime']), "endTime should be in ISO format"
            
    else:
        # A None result indicates a 404, which is also valid (no shifts found)
        assert result is None

