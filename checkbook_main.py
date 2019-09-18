import sys
    
def first_page():
    print(f''' 
    Welcome back,{username}.
    _____________________________________
    |           TRANSACTIONS            |
    |   1 - View current balance        |
    |   2 - Record a credit (deposit)   |
    |   3 - Record a debit (withdraw)   |
    |   4 - Exit                        |
    _____________________________________
    ''')

    user_input = input("    Please select your desired transaction: ")
    user_input = int(user_input)
    
    if user_input == 1:
        view_balance()
    elif user_input == 2:
        deposit()
    elif user_input == 3:
        withdraw()
    elif user_input == 4:
        exit_program()
    else:
        print("    Sorry, we could not process your selection. If you wish to continue, please select the number of your desired transaction.")
        print()
        home_page()

def home_page():
    print(f''' 
    _____________________________________
           {username}'s Checkbook       
    _____________________________________
    |   1 - View current balance        |
    |   2 - Record a credit (deposit)   |
    |   3 - Record a debit (withdraw)   |
    |   4 - Exit                        |
    _____________________________________
    ''')

    user_input = input("    Please select your desired transaction: ")
    user_input = int(user_input)
    
    if user_input == 1:
        view_balance()
    elif user_input == 2:
        deposit()
    elif user_input == 3:
        withdraw()
    elif user_input == 4:
        exit_program()
    else:
        print("    Sorry, we could not process your selection. If you wish to continue, please select the number of your desired transaction.")
        print()
        home_page()
        
### Functions to normalize values

def make_positive(n):
    return abs(float(n))
    
def make_negative(n):
    n = float(n)
    n *= -1.0
    return n

def remove_special(n):
    n_to_list = [i for i in n if i not in "!@#$%^&*()[]{;}:/<>?\|`~-=_+"]
    n = "".join(n_to_list)
    return n
    
### Transaction Functions

def view_balance():
    vb_credit = 0
    vb_debit = 0

    with open('user_transactions.txt') as ut:
        t_reader = ut.readlines()
        for item in t_reader:
            item = item.strip()
            if item.startswith('-'):
                item = item.strip('-')
                vb_debit += float(item)
            else:
                vb_credit += float(item)

    current_balance = vb_credit - vb_debit
    print(f"""
    _____________________________________
          Your Current Balance is:      
            {current_balance}          
    _____________________________________
    """
    )
    continue_transaction()

def deposit():
    deposit_amount = input("    How much would you like to deposit? $")
    
    if deposit_amount.isalpha() == False:
        deposit_amount = make_positive(remove_special(deposit_amount))
        with open('user_transactions.txt', 'a+') as ut:
            ut.write(str(deposit_amount) + '\n')
            print("    You've successfully made a deposit. Thank you for your business.")
    else:
        print("    Incorrect value was received. Please try again.")
    
    continue_transaction()

def withdraw():
    withdrawal_amount = input("    How much would you like to withdraw? $")
    
    if withdrawal_amount.isalpha() == False:
        withdrawal_amount = make_negative(remove_special(withdrawal_amount))
        with open('user_transactions.txt', 'a+') as ut:
            ut.write(str(withdrawal_amount) + '\n')
            print("    Withdrawal has successfully been made. Thank you for your business.")
    else:
        print("    Incorrect value was received. Please try again.")
 
    continue_transaction()

def exit_program():
    exit_choice = input ("    Are you sure you want to exit? Y/N: ")
    exit_choice = exit_choice.lower()
    
    if exit_choice == "y":
        sys.exit()
    elif exit_choice == "n":
        home_page()
    else:
        print("Invalid input")
        home_page()

def continue_transaction():
    continue_choice = input ("    Do you want to make another transaction? Y/N: ")
    continue_choice = continue_choice.lower()
    
    if continue_choice == "y":
        home_page()
    elif continue_choice == "n":
        exit_program()
    else:
        print("Invalid input")
        home_page()

username = input("    Enter you name: ")
first_page()