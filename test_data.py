#this file will just be used to test the functions in expenseTracker.py
import json
import os
import tempfile
from expenseTracker import load_data, create_data_file, validate_json_data



#this function creates data for testing
def create_test_data(test_data):

    temporary_file_name = None
       
    try:
        with tempfile.NamedTemporaryFile(suffix=".json", encoding="utf-8", mode="w", delete=False) as temporary_file:
           
            temporary_file_name = temporary_file.name
 
            create_data_file(test_data, temporary_file_name) #write data in the temporary file
            load_test_data = load_data(temporary_file_name) #loads data from the temporary file
            
           

            assert test_data == load_test_data, "Error the file content is different,check the load_data function"
            test_validate_json_data(load_test_data)

    finally:
        if temporary_file_name is not None:
            os.remove(temporary_file_name)
        

invalid_expense = [
    {
        "activity": "gym",
        "value": 50,
        "category": "d",
        "date": "31/02/2024"
    }
]
valid_expense = [
    {
        "activity": "gym",
        "value": 50,
        "category": "sport",
        "date": "01/09/2024"
    }
]
def test_validate_json_data(data):
    #This function checkes that validate_json_data is working well
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

#test_validate_json_data(invalid_expense)
#test_validate_json_data(valid_expense)


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




def my_function(num):

    if num < 0:
        raise ValueError
    

    def inner(num):
        print(num)
        
        if num <= 1:
            return 1

        return num * inner(num - 1)
        
    return inner(num)


value = my_function(4)
print(value)
print(value)