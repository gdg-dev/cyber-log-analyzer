#This is my project to track the expenses of the user. 
from datetime import datetime
import json
import os




date_format = "%d/%m/%Y"






def load_data(file_name="expenses_data.json"):
    #this function loads the data from the json file and returns it to the expenses variable
    try:
        with open(file_name, "r") as file:
            y = file.read()
            
            striped_y = y.strip()

            if not striped_y:  #no data neither empty data like ""
                x = {"expenses" : [], "budget": 0}
                return x

            else:
                x = json.loads(y)
                return x
                
                
                   


    except json.JSONDecodeError as e :
        raise SystemExit(f"Error the file has wrong format stoping program... {e}")
        
    
    except FileNotFoundError:
        print("Error the file wanted is not found. -creating a new file...")
        x = {"expenses": [], "budget":0}
        create_data_file(x, file_name)
        
        return x
    else:
        #assert isinstance(x, dict), "the file must contain a dict of expenses and budget."
        if not isinstance(x, dict):
            raise ValueError("the file must contain a dictionary with expenses and budget.")
        if not validate_json_data(x):
            raise ValueError("the file has invalid data")
        return x
    



def create_data_file(data, budget_num, file_name="expenses_data.json"):
    final_data = {"expenses":data, "budget":budget_num}
    with open(file_name, "w") as file:
        json.dump(final_data, file, indent=4)




def validate_json_data(data):
    #this function validates the data from the json file to make sure it is correct and not missing any key

    required_keys = ["activity", "value", "category", "date"]
    for expense in data["expenses"]:
        print(expense)
    #assert isinstance(expense, dict), "Each expense must be a dictionary"
        if not isinstance(expense, dict):
            print("Not a dictionary")
            return False
        #assert any(key  in expense for key in required_keys), "Missing keys in expense data"
        if any(key not in expense for key in required_keys):
            print("Missing keys in expense data")
            return False

        if not isinstance(expense['activity'], str):
            print("The activity isn't a string")
            return False
        #assert isinstance(expense['value'], bool) or not isinstance(expense['value'], (int, float)), "The value is a boolean"


        if isinstance(expense['value'], bool) or not isinstance(expense['value'], (int, float)):
            print("The value isn't a float or integer")
            return False
        
        elif expense['value'] < 0:
            print("The value is negative")
            return False
        #assert expense['value'] >= 0, "The value is negative"
        if not isinstance(expense['category'], str):
            print("The category isn't a string")
            return False
        try:
            
            if not isinstance(expense['date'], str):
                print("The date isn't a string")
                return False
            #assert datetime.strptime(expense['date'] , date_format), "The date is not in the correct format"
            datetime.strptime(expense['date'] , date_format)


            
            
        except ValueError as e:
            print(f"Json file date error the date isn't a datetime format: {expense['date']}, {e}")
            return False
        
    #assert True, "The data is valid"   
    return True

class InvalidDate(Exception):
    """This error just refers to the valid dates (1-12) """


class InvalidCategory(Exception):
    """This error is created to the invalid categories"""


def add_expense(activity, value, category):
    #this function add's a expense to expenses with a activity and a value given
    date = datetime.now()

    expenses.append({"activity": activity, "value": value, "category": category, "date": date.strftime(date_format)})   #<-- does not need to return because append already returns None

def show_expenses(filtered_expenses_dict):

    #this function shows the expenses from the given dictionary
    for i in filtered_expenses_dict:
        print(f"{i['activity']} --> €{i['value']:.2f}[{i['category'].lower()}] {i['date']}")
    
        
def set_budget(value):
    #this function changes the value of budget evendough using global is not the bette way
    global budget
    budget = value



def calculate_total(filtered_expenses_dict):
    #this function calculates the money spent and remaing from the user and also calls the show_expenses function to show only the expenses of the month choosen
    total_spent = 0
    
    for i in filtered_expenses_dict:
        total_spent += i['value']

    remaining = budget - total_spent
    return total_spent, remaining

def filter_expenses(given_month, category):
        #this function filters the expenses by mont and/or category
        filtered_expenses = []

        date_formate = "%d/%m/%Y"
        for expense in expenses:
            date_int = datetime.strptime(expense['date'], date_formate)
            month = date_int.month


            if not given_month or given_month == str(month):
               pass

            else:
                continue  #since the given month is wrong we can just ignore it
        

            if not category or category == expense['category']:
                pass
                    

            else:
                continue

            
           
                

           
            filtered_expenses.append(expense)
        return filtered_expenses
            


def menu():
    #this function works as a menu for the user
    
    print(f"""
--Menu--

1- Add Expenses;
2- Show Expenses;
3- Show Category;
4- Set Budget;
5- Show Budget;
6- Exit
""")

    #print(f"Current budget: €{budget_now:.2f}")
   
    user_answar = input("what is your choice: ")

    if user_answar == "1":
        try:

            activity = input("\nType the activity of your expense: ").lower()
            value = float(input("\nType the value of your expense: "))
            category = input("\nType the category of your expense: ").lower()
            add_expense(activity, value, category)
            create_data_file(expenses, budget_now)

        except ValueError as e:
            print(f"\nError: [{e}] try again later")
            


    elif user_answar == "2":
        valid_dates = ["1","2","3","4","5","6","7","8","9","10","11","12", ""]
        try:
            given_date = input("\nInsert the number of the month wanted from 1 to 12. (if you want all expanses just press enter with no text): ")
            if not given_date in valid_dates:
                raise InvalidDate

            

        except InvalidDate:
            print("\nThe date given is not correct please try something from 1-12")

        else:
            expenses_by_date = filter_expenses(given_date, "")
            spent, remaining = calculate_total(expenses_by_date)
            show_expenses(expenses_by_date)
            

                
            if spent == 0:
                print("\nNo expenses")


            elif spent > budget_now:
                print("\nYou have exceeded the budget! Be carefull")

            print(f"\nTotal spent [€{spent:.2f}]") 

        
    elif user_answar == "3":
        valid_category = []
        for i in expenses:
            valid_category.append(i['category'])

        try:

            category = input("\nType the category of your expense: ").lower()
            if category not in valid_category:
                raise InvalidCategory
            
        except InvalidCategory:
            print("\nThe given category is incorrect please try again later")

        else:
            expenses_by_category = filter_expenses("", category)
            spent, remaining = calculate_total(expenses_by_category)
            show_expenses(expenses_by_category)
            print(f"\nTotal spent ->€{spent:.2f},Remaining €{remaining:.2f}")

    elif user_answar == "4":
        try:
            budget_given = float(input("\nWhat is the new budget: "))
            

        except ValueError as e:
            print(f"Error: [{e}] please try again later")
        else:    
            budget_now = set_budget(budget_given)
            
            create_data_file(expenses, budget_now)
            
            
        
    elif user_answar == "5":
        print(budget_now)
        spent , remaining = calculate_total(expenses)
        print(f"\nTotal budget: {budget_now:.2f}") 
        print(f"Total spent: {spent:.2f}")
        print(f"Total remaining: {remaining:.2f}")
        
    elif user_answar == "6":
        exit()

    else:
        print("Invalid choice please try a number from 1 to 6")






def func_tion():
    print(a)
a = 23
func_tion()

if __name__ == "__main__":

    expenses_dict = load_data()
    
    
    expenses = expenses_dict["expenses"]
    budget_now = expenses_dict["budget"]
    print(budget_now)
    print(expenses)
    
    #final_data = {"expenses": expenses, "budget":budget}
    #create_data_file(final_data)
    while True:
        menu()


