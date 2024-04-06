from assignment2 import get_time_of_day

def test_get_time_of_day():
    # Test case: Known time at 14:30 should return 14
    assert get_time_of_day("01/01/2022 14:30") == 14
    # Test case: Midnight should return 0
    assert get_time_of_day("01/01/2022 00:00") == 0
    # Test case: 11:59 PM should return 23
    assert get_time_of_day("01/01/2022 23:59") == 23
    
    print("All tests passed for get_time_of_day.")