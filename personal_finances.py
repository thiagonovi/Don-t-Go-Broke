# os is for the cleanConsole() and datetime is fot getting the date of today for new expenses and gains
import os
import datetime
from datetime import timedelta

prompt = "> "


# Function to clear the console everytime you change screens
def cleanConsole():
    command = "clear"
    os.system(command)

# Function to read your current balance.
# It will always be in the first line of the statement.txt
def read_balance():
    cleanConsole()
    with open("statement.txt") as statement:
        lines = statement.readlines()
    print(f"You current balance is R${lines[0]}")
    input("Press any key to go back to the menu.")
    menu()

# Function to register a new gain in the statement.txt
def register_gain(gain, description):
    with open("statement.txt") as statement:
        lines = statement.readlines()
    prev_balace = lines[0].rstrip('\n')
    new_balance = str((float(prev_balace) + gain)) + '\n'
    lines[0] = new_balance

    # Appends first the datetime, then the description in the next line and then the gain in the next
    lines.append(str(datetime.date.today()) + '\n')
    lines.append(description + '\n')
    lines.append(str(gain) + '\n')

    with open("statement.txt", 'w') as statement:
        for line in lines:
            statement.write(line)

    input("\nNew gain registered successfully! Press any key to go back to the menu.")
    menu()

# Function to register a new expense in the statement.txt
def register_expense(expense, description):
    with open("statement.txt") as statement:
        lines = statement.readlines()
    prev_balace = lines[0].rstrip('\n')
    new_balance = str((float(prev_balace) - expense)) + '\n'
    lines[0] = new_balance

    # Appends first the datetime, then the description in the next line and then the expense in the next
    lines.append(str(datetime.date.today()) + '\n')
    lines.append(description + '\n')
    lines.append(str(- expense) + '\n')

    with open("statement.txt", 'w') as statement:
        for line in lines:
            statement.write(line)

    input("\nNew expense registered successfully! Press any key to go back to the menu.")
    menu()

def statement_function(days_behind):
    date = datetime.date.today() - timedelta(days=days_behind)
    with open("statement.txt") as statement:
        lines = statement.readlines()
    while (str(date) + '\n') not in lines:
        date = date + timedelta(days=1)
    date_index = lines.index(str(date) + '\n')
    n = date_index
    cleanConsole()
    print(f"Your statement from the last {days_behind} days:\n")
    while n <= (len(lines) - 3):
        print(lines[n].rstrip('\n') + '  ',
        lines[n + 1].rstrip('\n') + '  ',
        lines[n + 2].rstrip('\n') + '  ')
        n += 3

# Function to check your whole statement
def check_statement():
    with open("statement.txt") as statement:
        lines = statement.readlines()
    balance_statement = lines[0]
    print("""Choose the time period for you statement:
    > Last 2 days
    > Last 5 days
    > Last 30 days
    > Last 60 days\n""")
    statement_period = input(prompt)
    if statement_period == "2":
        statement_function(2)
    if statement_period == "5":
        statement_function(5)
    if statement_period == "30":
        statement_function(30)
    if statement_period == "60":
        statement_function(60)
    print(f"\nBalance: R${balance_statement}")
    input("Press any key to go back to the menu.")
    menu()

# Function of the menu
def menu():
    cleanConsole()
    print("""Welcome to Don\'t go broke!\n
What do you want do do?
    1. Check my balance
    2. Register an expense
    3. Register a gain
    4. Check you statement
    5. CLose the app""")
    response = input(prompt)

    if response == "1":
        read_balance()
    elif response == "2":
        cleanConsole()
        print("What is the value of this new expense?")
        expense = float(input(prompt + "R$"))
        description = input("\nAdd a description to this expense\n" + prompt)
        register_expense(expense, description)
    elif response == "3":
        cleanConsole()
        print("What is the value of this new gain?")
        gain = float(input(prompt + "R$"))
        description = input("\nAdd a description to this gain\n" + prompt)
        register_gain(gain, description)
    elif response == "4":
        cleanConsole()
        check_statement()
    elif response == "5":
        cleanConsole()
        print("Are you sure you want to closse the app? [y/n]")
        close_response = input(prompt)
        if (close_response == 'Y') or (close_response == 'y'):
            exit()
        else:
            menu()
    else:
        input(f"'{response}' isn't a valid option! Please, press any key to go back to the menu.")
        menu()

# Start of the program
menu()
