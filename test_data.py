#this file will just be used to test the functions in expenseTracker.py

import os
from expenseTracker import load_data, create_data_file, validate_json_data


print("running")

def test_create_data_file():
    test_expenses = [{
        "activity": "swim",
        "value": 23,
        "category": "entertainment",
        "date": "02/08/2024"
    },
    {
        "activity": "shopping",
        "value": 30,
        "category": "food and clothes",
        "date": "02/04/2024"
    }]


    create_data_file(test_expenses, "test_expenses_data.json")

    new_data = load_data("test_expenses_data.json")
    assert test_expenses == new_data, "Error the expenses hadn't been saved"
    


def test_validate_json_data():
    #This function checkes that validate_json_data is working well
    valid_non_empty = [{ 
        "activity": "gym",
        "value": 50,
        "category": "sport",
        "date": "01/09/2024"}]
    valid_empty = []
    non_dict = [(1,2,3,4)]
    bad_date =[{
            "activity": "gym",
            "value": 50,
            "category": "sport",
            "date": "31/02/2024"}]  #there is no 31 of february
    missing_category = [{ 
            "activity": "gym",
            "category": "sport",
            "date": "01/09/2024"}]
    bool_value = [{
        "activity": "gym",
        "value": True,
        "category": "sport",
        "date": "01/02/2024"
    }]
    date_str = [
        {"activity": "gym",
        "value": 50,
        "category": "sport",
        "date": "hi"
        }]
    value_str = [
            {"activity": "gym",
            "value": "50",
            "category": "sport",
            "date": "01/02/2024"
            }]
    negative_value = [
        {"activity": "gym",
        "value": -10,
        "category": "sport",
        "date": "01/02/2024"
        }]
    assert validate_json_data(valid_non_empty) is True, "Error in the valid data, non empty data"
    assert validate_json_data(valid_empty) is True, "Error in the valid data and empty"
    assert validate_json_data(non_dict) is False, "Error in the non dict data"
    assert validate_json_data(bad_date) is False, "Error in the invalid date"
    assert validate_json_data(missing_category) is False, "Error in the missing category"
    assert validate_json_data(bool_value) is False, "Error in the bool value"
    assert validate_json_data(date_str) is False, "Error in the str date"
    assert validate_json_data(value_str) is False, "Error in the str value"
    assert validate_json_data(negative_value) is False, "Error in the negative value"
    print("All validations from validate_json_data are working")

def test_load_data():
    file_name = "fake_expenses_data.json"
    assert load_data(file_name) == [], "Error in the different file name"
    assert os.path.exists(file_name), "Error this file doesn't exist"



test_validate_json_data()
test_create_data_file()
test_load_data()
