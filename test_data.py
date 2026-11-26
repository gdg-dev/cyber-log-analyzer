#this file will just be used to test the functions in expenseTracker.py
from expenseTracker import load_data, create_data_file, validate_json_data, InvalidDate
import pytest 
import copy




@pytest.fixture()
def sample_data():
    return {
    "expenses": [
          {
        "activity": "swim",
        "value": 23,
        "category": "entertainment",
        "date": "2/8/2024"
    }
    ],
    "budget":100}
 






def test_json_validator(sample_data):
   
    assert validate_json_data(sample_data) is True

def test_missing_keys(sample_data):
    
   
    del sample_data["expenses"][0]["activity"]
    assert validate_json_data(sample_data) is False



def test_negative_expense_values(sample_data):
   
    sample_data["expenses"][0]["value"] = -10
    assert validate_json_data(sample_data) is False


def test_invalid_dates(sample_data):
   
    sample_data["expenses"][0]["date"] = 20
    assert validate_json_data(sample_data) is False

def test_incorrect_data_types(sample_data):

    sample_data["expenses"][0]["activity"] = 20
    assert validate_json_data(sample_data) is False
        
def test_empty_string_activity(sample_data):
    sample_data["expenses"][0]["activity"] = ""
    assert validate_json_data(sample_data) is False

def test_negative_budget(sample_data):
    
    sample_data["budget"] = -100
    assert validate_json_data(sample_data) is False


def test_nan_expense_value(sample_data):
   
    sample_data["expenses"][0]["value"] = float("nan")
    assert validate_json_data(sample_data) is False


def test_invalid_date_format(sample_data):
    sample_data["expenses"][0]["date"] = "not a date"
    assert validate_json_data(sample_data) is False

def test_expense_value_of_0(sample_data):
    sample_data["expenses"][0]["value"] = 0
    assert validate_json_data(sample_data) is False

def test_budget_of_0(sample_data):
    sample_data["budget"] = 0
    assert validate_json_data(sample_data) is True


def test_empty_expenses(sample_data):
    sample_data["expenses"][0] = []
    assert validate_json_data(sample_data) is False


def test_activity_with_just_spaces(sample_data):
    sample_data["expenses"][0]["activity"] = "   "
    assert validate_json_data(sample_data) is False






