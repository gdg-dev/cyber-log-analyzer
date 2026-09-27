#This is my project to track the expenses of the user. 
from datetime import datetime



budget = 0

expenses = []


class InvalidDate(Exception):
    """This error just refers to the valid dates (1-12) """

def add_expense(activity, value, category):
    #this function add's a expense to expenses with a activity and a value given
    date = datetime.now()

    expenses.append({"activity": activity, "value": value, "category": category, "date": date.strftime("%d/%m/%Y")})   #<-- does not need to return because append already returns None

def show_expenses(i):
    #this function shows all the expenses in the expense list and sum all expenses

    print(f"{i['activity']} --> €{i['value']:.2f}[{i['category'].lower()}] {i['date']}")
    
        


def show_category(category):
    #this function prints the expenses of a specific category
    total = 0
    for i in expenses:
        if i['category'] == category:
            print(f"{i['activity']} --> €{i['value']:.2f}[{i['category'].lower()}] {i['date']}")
            total += i['value']
    print(f"\nTotal: €{total:.2f}")

def set_budget(value):
    #this function changes the value of budget evendough using global is not the bette way
    global budget
    budget = value



def calulate_total(date=""):
    #this function calculates the money spent and remaing from the user and also calls the show_expenses function to show only the expenses of the month choosen
    total_spent = 0
    date_format = "%m/%d/%y"
    for i in expenses:
        date_to_str = datetime.strptime(i['date'], date_format)
        month_date = date_to_str.month


        if date == "":
            total_spent += i['value']
            show_expenses(i)
            

        elif date == str(month_date):
            total_spent += i['value']
            show_expenses(i)

    remainig = budget - total_spent
    return total_spent, remainig


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
        
        except InvalidDate as e:
            print("\nThe date given is not correct please try something from 1-12")

        else:
            spent, remaining = calulate_total(given_date)
                
            if spent == 0:
                print("\nNo expenses")


            elif spent > budget:
                print("\nYou have exceeded the budget! Be carefull")

            print(f"\nTotal spent [€{spent:.2f}]") 

        
    elif user_answar == "3":
        category = input("\nType the category of your expense: ").lower()
        show_category(category)

    elif user_answar == "4":
        try:
            budget_given = float(input("\nWhat is the new budget: "))
            

        except ValueError as e:
            print(f"Error: [{e}] please try again later")
        else:    
            set_budget(budget_given)
            
        
    elif user_answar == "5":
        print(budget)
        spent , remaining = calulate_total()
        print(f"\nTotal budget: {budget:.2f}") 
        print(f"Total spent: {spent:.2f}")
        print(f"Total remaining: {remaining:.2f}")
        
    elif user_answar == "6":
        exit()

    else:
        print("Invalid choice please try a number from 1 to 6")


while True:
    menu()
   


