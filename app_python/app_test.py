"""Importing required libraries"""

import datetime
import app

def test_time_response():
    """testing the time response"""
    moscow_time_res= app.moscow_time_now()
    
    print(datetime.datetime.strptime(moscow_time_res, "%H:%M:%S"))

if __name__ == "__main__":
    test_time_response()
    print("Test completed and passed")
