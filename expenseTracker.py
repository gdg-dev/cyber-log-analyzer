#This is my project to track the expenses of the user. 
from datetime import datetime

budget = 0

expenses = []

def add_expense(activity, value, category):
    #this function add's a expense to expenses with a activity and a value given
    date = datetime.now()

    expenses.append({"activity": activity, "value": value, "category": category, "date": date.strftime("%x")})   #<-- does not need to return because append already returns None

def show_expenses():
    #this function shows all the expenses in the expense list and sum all expenses
    for i in expenses:
        print(f"{i['activity']} --> €{i['value']:.2f}[{i['category'].lower()}] {i['date']}")


def show_category(category):
    #this function prints the expenses of a specific category
    total = 0
    for i in expenses:
        if i['category'] == category:
            print(f"{i['activity']} --> €{i['value']:.2f}[{i['category'].lower()}]")
            total += i['value']
    print(f"\nTotal: €{total:.2f}")

def set_budget(value):
    #this function changes the value of budget evendough using global is not the bette way
    global budget
    budget = value



def caclulate_total():
    #this function calculates the money spent and remaing from the user
    total_spent = 0
    for i in expenses:
        total_spent += i['value']

    remainig = budget - total_spent
    return total_spent, remainig, budget


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

    
  
    user_answar = input("what is your choice: ")

    if user_answar == "1":
        try:

            activity = input("\nType the activity of your expense: ").lower()
            value = float(input("\nType the value of your expense: "))
            category = input("\nType the category of you expense: ").lower()
            add_expense(activity, value, category)

        except ValueError as e:
            print(f"\nError: [{e}] try again later")
            


    elif user_answar == "2":
        show_expenses()
        spent, remaining, budget = caclulate_total()
        print(f"\nTotal spent [€{spent:.2f}]")

    elif user_answar == "3":
        category = input("\nType the category of your expense: ").lower()
        show_category(category)

    elif user_answar == "4":
        try:
            budget_given = float(input("what is the new budget: "))
            

        except ValueError as e:
            print(f"Error: [{e}] please try again later")
        else:    
            set_budget(budget_given)
            
        
    elif user_answar == "5":
        spent , remaining, budget = caclulate_total()
        print(f"\nTotal budget: {budget:.2f}") 
        print(f"Total spent: {spent:.2f}")
        print(f"Total remaining: {remaining:.2f}")
        
    elif user_answar == "6":
        exit()

    else:
        print("Invalid choice please try a number from 1 to 6")


while True:
    menu()
    print(expenses)


