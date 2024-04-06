from assignment2 import get_day_of_week



def test_get_day_of_week():
    # Test case: Known date where 04/03/2022 is a Sunday
    assert get_day_of_week("04/03/2022 00:00") == 7  # Assuming 1=Sunday, 7=Saturday
    # Test case: Another known date
    assert get_day_of_week("04/04/2022 00:00") == 1  # Assuming 1=Sunday, Monday should be 2 if Sunday is 1
    
    print("All tests passed for get_day_of_week.")