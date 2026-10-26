#this file will just be used to test the functions in expenseTracker.py
import json
import os
import tempfile
from expenseTracker import load_data, create_data_file, validate_json_data



#this function creates data for testing
def create_test_data(test_data):
    
       
    try:
        with tempfile.NamedTemporaryFile(suffix=".json", encoding="utf-8", mode="w", delete=False) as temporary_file:
           

            json.dump(test_data, temporary_file, indent=4)

            #temporary_file.read()
            
            create_data_file(test_data, temporary_file.name)
            load_test_data = load_data(temporary_file.name)
            print(load_test_data)

            assert test_data == load_test_data, "Error the file content is different,check the load_data function"
            test_validate_json_data(load_test_data)

    finally:
        os.remove(temporary_file.name)
        print("all good")




def test_validate_json_data(data):
    #This function checkes that validate_json_data is working well
    print(data)
    #assert validate_json_data(data) is True, "Error in the valid data, non empty data"
    assert validate_json_data(data) is True, "Error something went wrong"
    #assert validate_json_data(data) is False, "Error in the non dict data"
    #assert validate_json_data(data) is False, "Error in the invalid date"
    #assert validate_json_data(data) is False, "Error in the missing category"
    #assert validate_json_data(data) is False, "Error in the bool value"
    #assert validate_json_data(data) is False, "Error in the str date"
    #assert validate_json_data(data) is False, "Error in the str value"
    #assert validate_json_data(data) is False, "Error in the negative value"
    print("All validations from validate_json_data are working")




test_expenses = [{
        "activity": "gym",
        "value": 50,
        "category": "sport",
        "date": "01/09/2024"
    },
    {
        "activity": "movie",
        "value": 15,
        "category": "entertainment",
        "date": "02/01/2024"
    }]

if __name__ == "__main__":
    
    create_test_data(test_expenses)

