#This is my project to track the expenses of the user. 

expenses = [
    {"activity": "coffee", "value": 1.20, "category": "food"},

]

def add_expense(activity, value, category):
    #this function add's a expense to expenses with a activity and a value given
    expenses.append({"activity": activity, "value": value, "category": category})   #<-- does not need to return because append already returns None

def show_expenses():
    #this function shows all the expenses in the expense list and sum all expenses
    total = 0
    for i in expenses:
        print(f"{i['activity']} --> €{i['value']:.2f}[{i['category'].lower()}]")
        total += i['value']

    print(f"\nTotal: €{total:.2f}")

def show_category(category):
    #this function prints the expenses of a specific category
    total = 0
    for i in expenses:
        if i['category'] == category:
            print(f"{i['activity']} --> €{i['value']:.2f}[{i['category'].lower()}]")
            total += i['value']
    print(f"\nTotal: €{total:.2f}")


def menu():
    #this function works as a menu for the user
    print(f"""
--Menu--

1- Add Expenses;
2- Show Expenses;
3- Show Category;
4- Exit
""")

    user_answar = input("what is your choice: ")


    if user_answar == "1":
        activity = input("\nType the activity of your expense: ")
        value = int(input("\nType the value of your expense: "))
        category = input("\nType the category of you expense: ")
        add_expense(activity, value, category)




menu()