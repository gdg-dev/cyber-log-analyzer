#this file will just be used to test the functions in expenseTracker.py
from expenseTracker import load_data, create_data_file, validate_json_data, InvalidDate
import pytest 
import copy



data = {
    "expenses": [
          {
        "activity": "swim",
        "value": 23,
        "category": "entertainment",
        "date": "2/8/2024"
    }],
    "budget":100
}





def test_json_validator():
   
    assert validate_json_data(data) is True

def test_missing_keys():
    
    changed_dict = copy.deepcopy(data)
    del changed_dict["expenses"][0]["activity"]
    assert validate_json_data(changed_dict) is False



def test_negative_expense_values():
    changed_dict = copy.deepcopy(data)
    changed_dict["expenses"][0]["value"] = -10
    assert validate_json_data(changed_dict) is False


def test_invalid_dates():
    changed_dict = copy.deepcopy(data)
    changed_dict["expenses"][0]["date"] = 20
    assert validate_json_data(changed_dict) is False

def test_incorrect_data_types():
    changed_dict = copy.deepcopy(data)
    changed_dict["expenses"][0]["activity"] = 20
    assert validate_json_data(changed_dict) is False
        


def test_negative_budget():
    changed_dict = copy.deepcopy(data)
    changed_dict["budget"] = -100
    assert validate_json_data(changed_dict) is False