import os

prompt = "> "

def cleanConsole():
    command = "clear"
    os.system(command)

def read_balance():
    cleanConsole()
    with open("statement.txt") as statement:
        lines = statement.readlines()
    print(f"You current balance is R${lines[0]}")
    input("Press any key to go back to the menu.")
    menu()

def register_gain(gain):
    with open("statement.txt") as statement:
        lines = statement.readlines()
    prev_balace = lines[0].rstrip('\n')
    new_balance = str((int(prev_balace) + gain)) + '\n'
    lines[0] = new_balance
    lines.append(str(gain) + '\n')
    with open("statement.txt", 'w') as statement:
        for line in lines:
            statement.write(line)

    input("\nNew gain registered successfully! Press any key to go back to the menu.")
    menu()

def register_expense(expense):
    with open("statement.txt") as statement:
        lines = statement.readlines()
    prev_balace = lines[0].rstrip('\n')
    new_balance = str((int(prev_balace) - expense)) + '\n'
    lines[0] = new_balance
    lines.append(str(expense) + '\n')
    with open("statement.txt", 'w') as statement:
        for line in lines:
            statement.write(line)

    input("\nNew expense registered successfully! Press any key to go back to the menu.")
    menu()



def menu():
    cleanConsole()
    print("""What do you want do do?
    1. Check my balance
    2. Register an expense
    3. Registe a gain
    4. CLose the app""")
    response = input(prompt)

    if response == "1":
        read_balance()
    elif response == "2":
        cleanConsole()
        print("What is the value of this new expense?")
        expense = int(input(prompt + "R$"))
        register_expense(expense)
    elif response == "3":
        cleanConsole()
        print("What is the value of this new gain?")
        gain = int(input(prompt + "R$"))
        register_gain(gain)
    elif response == "4":
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

menu()
