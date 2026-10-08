#This is my project to track the expenses of the user. 
from datetime import datetime
import json



budget = 0




def load_data():
    try:
        with open("expenses_data.json", "r") as file:
            x = json.load(file)

    except FileNotFoundError:
        print("Error the file wanted is not found. -creating a new file...")
        create_data_file()
    else:
        return x
    

    
def create_data_file(data):
    with open("expenses_data.json", "w") as file:
        json.dump(data, file, indent=4)

   
class InvalidDate(Exception):
    """This error just refers to the valid dates (1-12) """


class InvalidCategory(Exception):
    """This error is created to the invalid categories"""


def add_expense(activity, value, category):
    #this function add's a expense to expenses with a activity and a value given
    date = datetime.now()

    expenses.append({"activity": activity, "value": value, "category": category, "date": date.strftime("%d/%m/%Y")})   #<-- does not need to return because append already returns None

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
            


def menu(expenses_data):
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

    
    print(budget)
    user_answar = input("what is your choice: ")

    if user_answar == "1":
        try:

            activity = input("\nType the activity of your expense: ").lower()
            value = float(input("\nType the value of your expense: "))
            category = input("\nType the category of your expense: ").lower()
            add_expense(activity, value, category)

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
            expenses_by_date = filter_expenses(given_date, "sport")
            spent, remaining = calculate_total(expenses_by_date)
            show_expenses(expenses_by_date)
            

                
            if spent == 0:
                print("\nNo expenses")


            elif spent > budget:
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
            set_budget(budget_given)
            
        
    elif user_answar == "5":
        print(budget)
        spent , remaining = calculate_total()
        print(f"\nTotal budget: {budget:.2f}") 
        print(f"Total spent: {spent:.2f}")
        print(f"Total remaining: {remaining:.2f}")
        
    elif user_answar == "6":
        create_data_file(expenses)
        print("Data successfully saved")
        exit()

    else:
        print("Invalid choice please try a number from 1 to 6")

expenses = load_data()
print(expenses)
while True:
    menu(expenses)
   


    




